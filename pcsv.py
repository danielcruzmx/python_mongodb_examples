import csv
from utils import read_file_to_list_dict

class Condominio:

   def __init__(self, dictdata, lstcondominos, lstcuentas):
      condominos = { "condominos" : lstcondominos }
      cuentas = { "cuentas" : lstcuentas }
      self.dictdata = {}
      self.dictdata = dictdata      
      self.dictdata.update(condominos)
      self.dictdata.update(cuentas)

   def toDb(self):
      return self.dictdata
      
tab_path = '/storage/emulated/0/Git/exemplos_python/'
cel_path = '/storage/emulated/0/Android/'

lstcondominos = read_file_to_list_dict(tab_path + "condominos.csv")
lstcondominios = read_file_to_list_dict(tab_path + "condominios.csv")
lstcuentas = read_file_to_list_dict(tab_path + "cuentas.csv")

for con in lstcondominios:
    e = Condominio(con,lstcondominos,lstcuentas)
    # hacer collection en mongo Db
    print e.toDb()
    
   


      
   


