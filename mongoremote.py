from pymongo import MongoClient
from bancos import Banco

uri = 'mongodb://adcon_user:valeria1@ds021895.mlab.com:21895/adcon'

client = MongoClient(uri)
db = client.adcon

collection = db.Bancos

bancos = [
   Banco('002','Banamex'),
   Banco('012','BBVA Bancomer'),
   Banco('021','HSBC'),
   Banco('072','Banorte')
]

for banco in bancos:
   collection.insert(banco.toDbCollection())

client.close()