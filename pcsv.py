import csv

def csv_reader_to_list_dict(datos):
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
         lstdata.append(dic)
   return lstdata

fDatos = open("/storage/emulated/0/com.hipipal.qpyplus/scripts/condominios.csv")
datos = csv.reader(fDatos)
 
lstcondominios = []

print csv_reader_to_list_dict(datos)


      
   


