import csv

# lee un archivo .csv y devuelve un reader
def read_file_to_reader(file):
   try:
      fdat = open(file)
      reader = csv.reader(fdat, quoting=csv.QUOTE_NONNUMERIC)
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
            if type(r[k]) is not float:
              valor = r[k].strip()
            else:
              valor = r[k]
            dic.update({llave[k].strip():valor})  # Agrega al diccionario
         if key == None:
            lstdata.append(dic)  # Si no hay filtro agrega renglon
         else:    
            if dic[key] == value:   # Si hay filtro agrega renglon que cumple
               lstdata.append(dic)
   return lstdata

