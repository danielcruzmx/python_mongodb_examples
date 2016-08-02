class Cuenta:

   def __init__(self ,banco ,cuenta ,clabe ,titular ,saldo ,fechasaldo):
      self.banco = banco
      self.cuenta = cuenta
      self.clabe = clabe
      self.titular = titular
      self.saldo = saldo
      self.fechasaldo = fechasaldo

   def toDbCollection(self):
      return {
      	   "banco": self.banco,
      	   "cuenta": self.cuenta,
      	   "clabe": self.clabe,
      	   "titular": self.titular,
      	   "saldo": self.saldo,
      	   "fechasaldo": self.fechasaldo
      }
   
   def __str__(self):
      return "%s %s" % (self.cuenta, self.titular)
      
class Condomino:

   def __init__(self, depto, poseedor, referencia, ultdeposito, adeudo):
      self.depto = depto
      self.poseedor = poseedor
      self.referencia = referencia
      self.ultdeposito = ultdeposito
      self.adeudo = adeudo

   def toDbCollection(self):
      return {
      	   "depto": self.depto,
      	   "poseedor": self.poseedor,
      	   "referencia": self.referencia,
      	   "ultdeposito": self.ultdeposito,
      	   "adeudo": self.adeudo
      	}   	
      	
   def __str__(self):
      return "%s %s" % (self.depto, self.poseedor)
      
class Condominio:

   def __init__(self, nombre, direccion, lstcondominos, lstcuentas, administrador, correo_admin):
      self.nombre = nombre
      self.direccion = direccion
      self.condominos = lstcondominos
      self.cuentas = lstcuentas
      self.administrador = administrador
      self.correo_admin = correo_admin

   def toDbCollection(self):
      return {
      	   "nombre": self.nombre,
      	   "direccion": self.direccion,
      	   "condominos": self.condominos,
      	   "cuentas": self.cuentas,
      	   "administrador": self.administrador,
      	   "correo": self.correo_admin
      }

   def __str__(self):
      return "%s" % (self.nombre)

