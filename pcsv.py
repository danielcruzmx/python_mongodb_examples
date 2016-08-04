import csv
#from utils import read_file_to_list_dict, reader_to_list_dict
from pymongo import MongoClient

def reader_to_list_dict(datos, key, value):
   llave = []
   lstdata = []
   for r in datos:
      #print r
      if datos.line_num == 1:
         llave = r
      else:
         dic = {}
         for k in range(0,len(r)):
            valor = r[k].strip()
            dic.update({llave[k].strip():valor})
            #print llave[k], valor
         if dic[key] == value:
            lstdata.append(dic)
   return lstdata

def read_file_to_list_dict(file):
   fdat = open(file)
   dat = csv.reader(fdat)
   #lstdata = csv_reader_to_list_dict(dat)
   return dat

def condominio(dictinicial, lstcondominos, lstcuentas):
   condominos = { "condominos" : lstcondominos }
   cuentas = { "cuentas" : lstcuentas }
   dictinicial.update(condominos)
   dictinicial.update(cuentas)
   return dictinicial

admin = 'Victoria Gonzalez'
uri = 'mongodb://adcon_user:valeria1@ds021895.mlab.com:21895/adcon'
tab_path = '/storage/emulated/0/Git/exemplos_python/'
cel_path = '/storage/emulated/0/Android/'

dcondominios = read_file_to_list_dict(tab_path + "condominios.csv")

client = MongoClient(uri)
db = client.adcon

lstcondominios = reader_to_list_dict(dcondominios, 'administrador', admin)
#print lstcondominios

for dcon in lstcondominios:
    nom = dcon['nombre']
    dcondominos = read_file_to_list_dict(tab_path + "condominos.csv")
    lstcondominos = reader_to_list_dict(dcondominos, 'condominio', nom)
    dcuentas = read_file_to_list_dict(tab_path + "cuentas.csv")
    lstcuentas = reader_to_list_dict(dcuentas, 'condominio', nom)
    c = condominio(dcon, lstcondominos, lstcuentas)
    #e = c.toDict()
    #lstcondominos = 
    # hacer collection en mongo Db
    collection = db[nom]
    #print c
    collection.insert(c)

#for banco in bancos:
#   collection.insert(banco.toDbCollection())

client.close()
   


