from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
#
Base = declarative_base()
#
#   Tabla de impuesto
#
class Ispt(Base):
  __tablename__ = 'ispt'
  
  id = Column(Integer, primary_key=True) 
  fecha_fin = Column(String(10))
  fecha_ini = Column(String(10)) 
  tipo = Column(String(10)) 
  linferior = Column(Float) 
  superior = Column(Float) 
  bruto = Column(Float) 
  cuota = Column(Float) 
  excedente = Column(Float) 
  subsidio = Column(Float) 
#
#    Tabla de reglas de calculo
#
class Reglas(Base):
   __tablename__ = 'reglas'

   id = Column(Integer, primary_key=True) 
   calculo = Column(String(20)) 
   tipo = Column(String(1)) 
   concepto = Column(String(2))
   var = Column(String(20))
   orden = Column(Integer)
   val = Column(Float) 
   desc = Column(String(30)) 
   formula = Column(String(50)) 
   jerarquia = Column(String(25))
   nivel = Column(String(25))
   nombramiento = Column(String(25))
   variable = Column(String(1))

