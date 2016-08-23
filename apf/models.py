from flask_sqlalchemy import SQLAlchemy
#from flask_admin.contrib.sqla import ModelView
#from flask_admin import Admin
#from config import app
#
db = SQLAlchemy(app)
#
#   Tabla de impuesto
#
class Ispt(db.Model): 
   id = db.Column(db.Integer, primary_key=True) 
   fin = db.Column('fecha_fin',db.String(10)) 
   ini = db.Column('fecha_ini',db.String(10)) 
   tipo = db.Column('tipo',db.String(10)) 
   linferior = db.Column('linferior',db.Float) 
   superior = db.Column('superior',db.Float) 
   bruto = db.Column('bruto',db.Float) 
   cuota = db.Column('cuota',db.Float) 
   excedente = db.Column('excedente',db.Float) 
   subsidio = db.Column('subsidio',db.Float) 
#
#    Tabla de reglas de calculo
#
class Reglasc(db.Model):
   id = db.Column(db.Integer, primary_key=True) 
   calculo = db.Column('calculo',db.String(20)) 
   tipo = db.Column('tipo',db.String(1)) 
   concepto = db.Column('concepto',db.String(2))
   var = db.Column('var',db.String(20))
   orden = db.Column('orden',db.Integer)
   val = db.Column('val',db.Float) 
   desc = db.Column('desc',db.String(30)) 
   formula = db.Column('formula',db.String(50)) 
   jerarquia = db.Column('jerarquia',db.String(25))
   nivel = db.Column('nivel',db.String(25))
   nombramiento = db.Column('nombramiento',db.String(25))
   variable = db.Column('variable',db.String(1))

