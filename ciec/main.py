#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import csv

# lee un archivo .csv y devuelve un reader
def read_file_to_reader(file):
   try:
      fdat = open(file)
      reader = csv.reader(fdat)
      return reader
   except IOError:
      print "Error: No se pudo abrir el archivo" + file
      return None   

# devuelve una lista de diccionarios apartir de un reader
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

   def __init__(self, datadict):
      if datadict != None: 
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
   
   def __init__(self, datadict):
      if datadict != None:
         self.nombre=datadict['nombre']
         self.domicilio=datadict['domicilio']
         self.regimen=datadict['regimen']
         self.condominos=datadict['condominos']
         self.cuentas=datadict['cuentas']
         self.cuotas=datadict['cuotas']

   def setcondominos(self, condominos):
      self.condominos=condominos

   def setcuentas(self, cuentas):
      self.cuentas=cuentas

   def setcuotas(self, cuotas):
      self.cuotas=cuotas

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

   def __init__(self, datadict):
      if datadict != None:
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

   def __init__(self, datadict):
      if datadict != None:
         self.banco=datadict['banco']
         self.cuenta=datadict['cuenta']
         self.clabe=datadict['clabe']
         self.titular=datadict['titular']
         self.saldo=datadict['saldo']
         self.fechasaldo=datadict['fechasaldo']
         self.situacioncuenta=datadict['situacioncuenta']

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

   def __init__(self, datadict):
      if datadict != None:
         self.num=datadict['num']
         self.tipo=datadict['tipocuota']
         self.fechainicio=datadict['fechainicio']
         self.fechatermino=datadict['fechatermino']
         self.monto=datadict['monto']
         self.montopena=datadict['montopena']

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

   def __init__(self, datadict):
      if datadict != None:
         self.banco=datadict['banco']
         sell.tipomovimiento=datadict['tipomovimiento']
         self.tiposervicio=datadict['tiposervicio']
         self.situacioncuenta=datadict['situacioncuenta']
         self.tipocuota=datadict['tipocuota']

   def toDbCol(self):
      return {
            "banco": self.banco,
            "tipomovimiento": self.tipomovimiento,
            "tiposervicio": self.tiposervicio,
            "situacioncuenta": self.situacioncuenta,
            "tipocuota": self.tipocuota
      }

class Movimiento:

   def __init__(self, datadict):
      if datadict != None:
         self.num=datadict['num']
         self.clabe=datadict['clabe']
         self.fecha=datadict['fecha']
         self.tipomovimiento=datadict['tipomovimiento']
         self.descripcion=datadict['descripcion']
         self.retiro=datadict['retiro']
         self.deposito=datadict['deposito']
         self.condomino=datadict['condomino']
         self.tiposervicio=datadict['tiposervicio']
         self.recibos=datadict['recibos']

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

   def __init__(self, datadict):
      if datadict != None:
         self.folio=datadict['folio']  
         self.fechaexpedicion=datadict['fechaexpedicion']
         self.notas=datadict['notas']
         self.concepto=datadict['concepto']  

   def toDbCol(self):
      return {
            "folio": self.folio,
            "fechaexpedicion": self.fechaexpedicion,
            "notas": self.notas,
            "concepto": self.concepto
      }

class Proveedor:

   def __init__(self, datadict):
      self.nombre=datadict['nombre']
      self.tiposervicio=datadict['tiposervicio']
      self.telefonos=datadict['telefonos']
      self.domicilio=datadict['domicilio']

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
   

