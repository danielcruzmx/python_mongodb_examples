__autor__ = 'danielcruzmx'

import csv

def reader_to_list_dict(datos, key, value):
   llave = []
   lstdata = []
   for r in datos:
      if datos.line_num == 1:
         llave = r
      else:
         dic = {}
         for k in range(0,len(r)):
            valor = r[k].strip()
            dic.update({llave[k].strip():valor})
            print dic
         if dic.key == value:
            lstdata.append(dic)
   return lstdata

def read_file_to_list_dict(file):
   fdat = open(file)
   dat = csv.reader(fdat)
   #lstdata = csv_reader_to_list_dict(dat)
   return dat
   
   
