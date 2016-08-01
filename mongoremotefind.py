from pymongo import MongoClient
from bancos import Banco

uri = 'mongodb://adcon_user:valeria1@ds021895.mlab.com:21895/adcon'

client = MongoClient(uri)
db = client.adcon

collection = db.Bancos

cursor = collection.find({"clave":{"$in":["012"]}}) 

for banco in cursor: 
    print banco

client.close()
