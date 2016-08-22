#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import csv

def read_file_to_reader(file):
   try:
      fdat = open(file)
      reader = csv.reader(fdat)
      return reader
   except IOError:
      print "Error: No se pudo abrir el archivo" + file
      return None   

# devuelve una lista de diccionarios
def reader_to_list_dict(reader, key, value):
   llave = []
   lstdata = []
   for r in reader:
      if reader.line_num == 1:
         llave = r  # El primer renglon tiene las llaves
      else:
         dic = {}
         for k in range(0,len(r)):  # Ciclo sobre columnas
            valor = r[k].strip()
            dic.update({llave[k].strip():valor})  # Agrega al diccionario
         if key == None:
            lstdata.append(dic)  # Si no hay filtro agrega renglon
         else:    
            if dic[key] == value:   # Si hay filtro agrega renglon que cumple
               lstdata.append(dic)
   return lstdata

class Administrador():

   def __init__(self, dicc):
      if dicc != None: 
         self.nombre=dicc['nombre']
         self.alias=dicc['alias']
         self.mail=dicc['mail']
         self.telefono=dicc['telefono']
         self.condominios=dicc['condominios']

   def fromdict(self, datadict):
      self.nombre=datadict['nombre']
      self.alias=datadict['alias']
      self.mail=datadict['mail']
      self.telefono=datadict['telefono']
      self.condominios=datadict['condominios']

   def setcondominios(self, condominios):
      self.condominios=condominios

   def toDbCol(self):
      return {
            "nombre": self.nombre,
            "alias": self.alias,
            "mail": self.mail,
            "telefono": self.telefono,
            "condominios": self.condominios
      }

   def __str__(self):
      return "%s" % (self.alias)      

class Condominio:
   
   '''def __init__(self , nombre, domicilio, regimen, condominos, cuentas, cuotas):
      self.nombre=nombre
      self.domicilio=domicilio
      self.regimen=regimen
      self.condominos=condominos
      self.cuentas=cuentas
      self.cuotas=cuotas
   '''   

   def __init__(self):
      pass

   def fromdict(self, datadict):
      self.nombre=datadict['nombre']
      self.domicilio=datadict['domicilio']
      self.regimen=datadict['regimen']
      self.condominos=datadict['condominos']
      self.cuentas=datadict['cuentas']
      self.cuotas=datadict['cuotas']

   def toDbCol(self):
      return {
            "nombre": self.nombre,
            "domicilio": self.domicilio,
            "regimen": self.regimen,
            "condominos": self.condominos,
            "cuentas": self.cuentas,
            "cuotas": self.cuotas
      }

   def __str__(self):
      return "%s" % (self.nombre)      

class Condomino:      

   ''' def __init__(self , depto, poseedor, referencia, mail, adeudo, fechaadeudo):
      self.depto=depto
      self.poseedor=poseedor
      self.referencia=referencia
      self.mail=mail
      self.adeudo=adeudo
      self.fechaadeudo=fechaadeudo
   '''

   def __init__(self):
      pass   

   def fromdict(self, datadict):
      self.depto=datadict['depto']
      self.poseedor=datadict['poseedor']
      self.referencia=datadict['referencia']
      self.mail=datadict['mail']
      self.adeudo=datadict['adeudo']
      self.fechaadeudo=datadict['fechaadeudo']

   def toDbCol(self):
      return {
            "depto": self.depto,
            "poseedor": self.poseedor,
            "referencia": self.referencia,
            "mail": self.mail,
            "adeudo": self.adeudo,
            "fechaadeudo": self.fechaadeudo
      }

   def __str__(self):
      return "%s %s" % (self.dpto, self.poseedor)      
     
class Cuenta:

   def __init__(self ,banco ,cuenta ,clabe ,titular ,saldo , fechasaldo, situacioncuenta):
      self.banco=banco
      self.cuenta=cuenta
      self.clabe=clabe
      self.titular=titular
      self.saldo=saldo
      self.fechasaldo=fechasaldo
      self.situacioncuenta=situacioncuenta

   def toDbCol(self):
      return {
            "banco": self.banco,
            "cuenta": self.cuenta,
            "clabe": self.clabe,
            "titular": self.titular,
            "saldo": self.saldo,
            "fechasaldo": self.fechasaldo,
            "situacioncuenta": self.situacioncuenta
      }

class Cuota:

   def __init__(self, num, tipocuota, fechainicio, fechatermino, monto, montopena):
      self.num=num
      self.tipo=tipocuota
      self.fechainicio=fechainicio
      self.fechatermino=fechatermino
      self.monto=monto
      self.montopena=montopena

   def toDbCol(self):
      return {
            "num": self.num,
            "tipocuota": self.tipocuota,
            "fechainicio": self.fechainicio,
            "fechatermino": self.fechatermino,
            "monto": self.monto,
            "montopena": self.montopena
      }

class Catalogo:

   def __init__(self, banco, tipomovimiento, tiposervicio, situacioncuenta, tipocuota):
      self.banco=banco
      sell.tipomovimiento=tipomovimiento
      self.tiposervicio=tiposervicio
      self.situacioncuenta=situacioncuenta
      self.tipocuota=tipocuota

   def toDbCol(self):
      return {
            "banco": self.banco,
            "tipomovimiento": self.tipomovimiento,
            "tiposervicio": self.tiposervicio,
            "situacioncuenta": self.situacioncuenta,
            "tipocuota": self.tipocuota
      }

class Movimiento:

   def __init__(self, num, clabe, fecha, tipomovimiento, descripcion, retiro, deposito, condomino, tiposervicio, recibos):
      self.num=num
      self.clabe=self.clabe
      self.fecha=fecha
      self.tipomovimiento=tipomovimiento
      self.descripcion=descripcion
      self.retiro=retiro
      self.deposito=deposito
      self.condomino=condomino
      self.tiposervicio=tiposervicio
      self.recibos=recibos

   def toDbCol(self):
      return {
            "num": self.num,
            "clabe": self.clabe,
            "fecha": self.fecha,
            "tipomovimiento": self.tipomovimiento,
            "descripcion": self.descripcion,
            "retiro": self.retiro,
            "deposito": self.deposito,
            "condomino": self.condomino,
            "tiposervicio": self.tiposervicio,
            "recibos": self.recibos
      }

class Recibo:

   def __init__(self, folio, fechaexpedicion, notas, concepto):
      self.folio=folio
      self.fechaexpedicion=fechaexpedicion
      self.notas=notas
      self.concepto=concepto

   def toDbCol(self):
      return {
            "folio": self.folio,
            "fechaexpedicion": self.fechaexpedicion,
            "notas": self.notas,
            "concepto": self.concepto
      }

class Proveedor:

   def __init__(self, nombre, tiposervicio, telefonos, domicilio):
      self.nombre=nombre
      self.tiposervicio=tiposervicio
      self.telefonos=telefonos
      self.domicilio=domicilio

   def toDbCol(self):
      return {
            "nombre": self.nombre,
            "tiposervicio": self.tiposervicio,
            "telefonos": self.telefonos,
            "domicilio": self.domicilio
      }

class Polizas(Recibo):

   def __init__(self):
      pass

print "Inicio"

path='C:\\proyectos_open_shift_daniel\\python_mongodb_examples\\'

rdatos = read_file_to_reader(path + "administradores.csv")

ladmins = reader_to_list_dict(rdatos, None, None)

for a in ladmins:
   #print a
   objadmin=Administrador(a)
   #objadmin.fromdict(a)
   print "Administrador -> " + objadmin.alias
   cdatos=read_file_to_reader(path + "condominios.csv")
   lcond = reader_to_list_dict(cdatos, 'administrador', objadmin.alias)
   objadmin.setcondominios(lcond)
   print objadmin.toDbCol()
   

