""" An example of how to connect to MongoDB """
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

uri = 'mongodb://adcon_user:valeria1@ds021895.mlab.com:21895/adcon'

def obt_collection(uri):
   """ Connect to MongoDB """
   col = []
   try:
      con = MongoClient(uri)
      bd = con.adcon
      col = bd.collection_names(include_system_collections=False)
      #print "Connected successfully"
      #return col
      con.close()
   except ConnectionFailure, e:
      sys.stderr.write("No es posible conectar con BD motivo: %s" % e)
   return col

def obt_lst_condominios(admin):
   ret = []
   try:
      con = MongoClient(uri)
      bd = con.adcon
      col = bd[admin]
      res = col.find()
      for c in res:
         try:
            ret.append(c['nombre'])
         except:
            pass
      con.close()
   except ConnectionFailure, e:
      sys.stderr.write("No es posible conectar con BD motivo: %s" % e)
   return ret

col = obt_collection(uri)
for a in col:
   print
   print 'Administrador: %s' % a
   print 'Condominios'
   c = obt_lst_condominios(a)
   print c
  