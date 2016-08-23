from models import Ispt
from antiguedad import *
from models import Reglasc
from sqlalchemy import desc
from datetime import datetime
from config import *
import collections

def ispt(monto):
   res = 0.0
   rango = Ispt.query.filter_by(\
   	        tipo='ispt', \
   	        fin=fecfinal).\
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
   rango = Ispt.query.filter_by(\
   	        tipo='bruto', \
   	        fin = fecfinal).\
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

def calculo(niv, param, opcion):
  var_s = {}
  
  if opcion == 'liquidacion':
     fecini =  datetime.strptime(param['ini'],'%Y-%m-%d').strftime('%d/%m/%Y')
     fecfin =  datetime.strptime(param['fin'],'%Y-%m-%d').strftime('%d/%m/%Y')
     ant = Antiguedad(fecini, fecfin)
     var_s.update({'anios':ant.anios})
     var_s.update({'meses':ant.meses})
     var_s.update({'dias':ant.dias}) 
     
  reglas = Reglasc.query.filter_by(\
  	        calculo=opcion).\
           order_by(Reglasc.orden).\
           all()
  maximo = Reglasc.query.filter_by(\
  	        calculo=opcion).\
  	        order_by(desc(Reglasc.orden)).\
  	        first() 
  var_s.update(variablesBase(niv))
  var_s.update(variablesForm(reglas, param, niv))

  #  CODIGO QUE EVALUA LAS FORMULAS DE LA BASE DE DATOS
  for o in range(1,maximo.orden+1):
      for r in reglas:
         if r.orden == o:
            clave = r.var
            ex = r.formula.format(**var_s) 
            valor = eval(ex)
            if not validaNivel(niv, r):
               valor = 0
            var_s.update({clave:valor})
  
  reg = Reglasc.query.filter_by(\
  	        calculo=opcion).\
           order_by(Reglasc.orden).\
           all()  
  
  resul = {}
  n = 1
  for r in reg:
      v = var_s[r.var]
      resul.update({ n: {'Descripcion': r.desc, 'Valor':v}})
      n = n + 1
  return collections.OrderedDict(sorted(resul.items()))

def existe(clave, param):
    ret = False
    for p in param:
       if p == clave:
          ret = True
          break
    return ret

def variablesForm(reglas, param, nivel):
    variables = {}
    for r in reglas:
       if r.orden == 0:
          clave = r.var
          if r.variable == 'S':
             if existe(clave,param):
                valor = param[clave]
             else:
                valor = r.val
          else:
             valor = r.val
          if not validaNivel(nivel, r):
             valor = 0
          variables.update({clave:valor})
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
    elif nivel.jerarquia in regla.jerarquia:
       ret = True
    else:
       ret = False
    if regla.nombramiento == 'todos':
       ret = True
    elif nivel.nombramiento in regla.nombramiento:
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
