from config import sesion, fecfinal
from models import Ispt, Reglas
from sqlalchemy import desc
from constantes import CONSTANTES_CALC
import collections

def existe(clave, param):
    ret = False
    for p in param:
       if p == clave:
          ret = True
          break
    return ret

def validaconcepto(nivel, regla):
    ret =  False

    if regla['jerarquias'] == 'todos':
       ret = True
    elif nivel.jerarquia.upper() in regla['jerarquias'].upper():
       ret = True
    else:
       ret = False

    if regla['nombramientos'] == 'todos':
       ret = True
    elif nivel.nombramiento.upper() in regla['nombramientos'].upper():
       ret = True
    else:
       ret = False

    if regla['niveles'] == 'todos':
       ret = True
    elif nivel.nivel[:1] in regla['niveles']:
       ret = True
    else:
       ret = False

    return ret

def evalua(expresion):
    try:
        valor = eval(expresion)
        return valor
    except (NameError, SyntaxError):
        print "Error: Al evaluar la expresion " + expresion
        return 0

def calc(pago, lstreglas):

    # AGREGA CONSTANTES
    var_s = {}
    var_s.update(CONSTANTES_CALC)

    # AGREGA CONCEPTOS INICIALES
    var_s.update({'sueldo': pago.sueldo})
    var_s.update({'compensacion': pago.compensacion})
    var_s.update({'incentivo': pago.sobresueldo})
    # falta incentivo

    # EVALUA Y AGREGA CONCEPTOS FIJOS
    for r in lstreglas:
        #print r
        if r['tipo_calc'] == 'fijo' and r['orden'] == 0 :
            clave = r['variable']
            ex = r['formula'].format(**var_s)
            valor = evalua(ex)
            if not validaconcepto(pago, r):
                valor = 0
            var_s.update({clave:valor})

    # RECUPERA LOS CONCEPTOS VARIABLES Y SU VALOR
    variables = {}
    for c in pago.conceptospago:
        clave = c['tipocpto'] + c['cpto']
        if is_number(c['porcentaje']):
            if c['porcentaje'] > 0:
                valor = c['porcentaje'] / 100.00
            else:
                valor = 0
        else:
            valor = c['monto']
        variables.update({clave: valor})

    # EVALUA Y AGREGA CONCEPTOS VARIABLES
    for r in lstreglas:
        # print r
        if r['tipo_calc'] == 'variable' and r['orden'] == 0 :
            clavevariable = r['variable']
            claveconcepto = r['tipo'] + r['concepto']
            if existe(claveconcepto,variables):
                # EVALUA CONCEPTO
                var_s.update({'valor': variables[claveconcepto]})
                ex = r['formula'].format(**var_s)
                valor = evalua(ex)
            else:
                valor = 0
            if not validaconcepto(pago, r):
                valor = 0
            var_s.update({clavevariable:valor})

    # EVALUA Y AGREGA CONCEPTOS DE CALCULO
    for r in lstreglas:
        # print r
        if r['tipo_calc'] == 'calculo' and r['orden'] == 0 :
            clavevariable = r['variable']
            ex = r['formula'].format(**var_s)
            valor = evalua(ex)
            if not validaconcepto(pago, r):
                valor = 0
            var_s.update({clavevariable:valor})

    # GUARDA RESULTADOS EN ARREGLO DE PAGADOS
    resul = {}
    n = 1
    for r in lstreglas:
        try:
            v = round(var_s[r['variable']],2)
            resul.update({ n: {'Descripcion': r['descripcion'], 'Valor':v, 'Concepto': r['codigosalida']}})
            n = n + 1
        except:
            pass
    return collections.OrderedDict(sorted(resul.items()))

#####################################################

def calcula(pago):
  var_s = {}
  
  opcion = 'nomina'

  reglas = sesion.query(Reglas).filter_by(\
  	        calculo=opcion).\
           order_by(Reglas.orden).\
           all()
  maximo = sesion.query(Reglas).filter_by(\
  	        calculo=opcion).\
  	        order_by(desc(Reglas.orden)).\
  	        first() 
  var_s.update(variablesBase(pago))

  variables = {}

  for c in pago.conceptospago:
    clave = c['tipocpto'] + c['cpto']
    if is_number(c['porcentaje']):
        if c['porcentaje'] > 0:
            valor = c['porcentaje'] / 100.00
        else:
            valor = 0
    else:  
      valor = c['monto']
    #print clave, valor
    variables.update({clave: valor})

  var_s.update(cptosvariables(reglas, variables, pago))

  #  CODIGO QUE EVALUA LAS FORMULAS DE LA BASE DE DATOS
  for o in range(1,maximo.orden+1):
      for r in reglas:
         if r.orden == o:
            clave = r.var
            ex = r.formula.format(**var_s)
            valor = eval(ex)
            if not validaNivel(pago, r):
               valor = 0
            var_s.update({clave:valor})
  
  reg = sesion.query(Reglas).filter_by(\
  	        calculo=opcion).\
           order_by(Reglas.orden).\
           all()  
  
  resul = {}
  n = 1
  for r in reg:
      v = var_s[r.var]
      resul.update({ n: {'Descripcion': r.desc, 'Valor':v, 'Concepto': r.tipo + r.concepto}})
      n = n + 1
  return collections.OrderedDict(sorted(resul.items()))

def cptosvariables(reglas, param, nivel):
    variables = {}
    for r in reglas:
       if r.orden == 0:
          clavevariable = r.var
          claveconcepto = r.tipo + r.concepto
          if r.variable == 'S':
             if existe(claveconcepto,param):
                valor = param[claveconcepto]
             else:
                valor = r.val
          else:
             valor = r.val
          if not validaNivel(nivel, r):
             valor = 0
          variables.update({clavevariable:valor})
    return variables

def variablesBase(nivel):
    variables = {}
    clave = 'sueldo'
    valor = nivel.sueldo
    variables.update({clave:valor})
    clave = 'compensacion'
    valor = nivel.compensacion
    variables.update({clave:valor})
    clave = 'sobreSueldo'
    valor = nivel.sobresueldo
    variables.update({clave:valor})
    return variables

def validaNivel(nivel, regla):
    ret =  False
    if regla.jerarquia == 'todos':
       ret = True
    elif nivel.jerarquia.upper() in regla.jerarquia.upper():
       ret = True
    else:
       ret = False
    if regla.nombramiento == 'todos':
       ret = True
    elif nivel.nombramiento.upper() in regla.nombramiento.upper():
       ret = True
    else:
       ret = False
    if regla.nivel == 'todos':
       ret = True
    elif nivel.nivel[:1] in regla.nivel:
       ret = True
    else:
       ret = False
    return ret

def ispt(monto):
   res = 0.0
   rango = sesion.query(Ispt).filter_by(\
            tipo='ispt', \
            fecha_fin=fecfinal).\
            order_by(Ispt.id).\
            all()
   if rango: 
      for r in rango:
         if r.linferior <= monto and r.superior >= monto:
            res = (monto-r.linferior)*r.excedente/100.0+r.cuota
            return res
   else:
      return res

def bruto(monto):
   res =0.0
   rango = sesion.query(Ispt).filter_by(\
            tipo='bruto', \
            fecha_fin = fecfinal).\
            order_by(Ispt.id).\
            all()
   if rango:
      for r in rango:
         if r.linferior <= monto and r.superior >= monto:
            res = (monto-r.cuota)/r.bruto
            return res
   else:
      return res

def ibruto(base, monto):
   isr = ispt(base)
   isrs = bruto(base-isr+monto)
   return isrs-base-monto

def is_number(s):
  n=0
  try:
     n=float(s)
     return n
  except ValueError:
     return n


