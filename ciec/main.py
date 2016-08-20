#-*-coding:utf8;-*-
#qpy:2
#qpy:console

class Administrador:

   def __init__(self, nombre, alias, mail, telefono, condominios):
      self.nombre=nombre
      self.alias=alias
      self.mail=mail
      self.telefono=telefono
      self.condominios=condominios

class Condominio:
   
   def __init__(self , nombre, domicilio, regimen, condominos, cuentas, cuotas)
      self.nombre=nombre
      self.domicilio=domicilio
      self.regimen=regimen
      self.condominos=condominos
      self.cuentas=cuentas
      self,cuotas=cuotas
      
class Cuota:

   def __init__(self, num, tipo, fechainicio, fechatermino, monto, pena):
      self.num=num
      self.tipo=tipo
      :-)

class Condomino:

   def __init__(self , depto, poseedor, referencia, mail, adeudo, fechaadeudo):
      self.depto=depto
      self.poseedor=poseedor
      self.referencia=referencia
      self.mail=mail
      self.adeudo=adeudo
      self.fechaadeudo=fechaadeudo
      
class Cuenta:

   def __init__(self ,banco ,cuenta ,clabe ,titular ,saldo , fechasaldo, situacion):
      self.banco=banco
      self.cuenta=cuenta
      self.clabe=clabe
      self.titular=titular
      self.saldo=saldo
      self.fechasaldo=fechasaldo
      self.situacion=situacion




print "This is console module"
