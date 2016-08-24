from config import sesion, fecfinal
from models import Ispt
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

