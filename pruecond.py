from pymongo import MongoClient
from classcond import Condominio, Condomino, Cuenta

uri = 'mongodb://adcon_user:valeria1@ds021895.mlab.com:21895/adcon'

client = MongoClient(uri)
db = client.adcon

collection = db.Condominios

lstcondominos = []
lstcuentas = []

c1 = Condomino('A303', 'Daniel Cruz', '-','-',0)
lstcondominos.append(c1.toDbCollection())

cta1 = Cuenta('Bancomer','1234567890','012180001234567890','Victoria Gonzalez',0,'-')
lstcuentas.append(cta1.toDbCollection())


c = Condominio('OLIMPO','Carrillo Puerto 34', lstcondominos, lstcuentas)

r = c.toDbCollection()

collection.insert(r)

client.close()
