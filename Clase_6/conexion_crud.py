#https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient
from pprint import pprint#make the output look more pretty
client = MongoClient(port=27017)#<<MONGODB URL>>)
db=client.hospital
# Buscar un solo documento en mongo
# dra = db.doctores.find_one({'apellido': "Strange"})
# pprint(dra)

# Consultar varios documentos
# for y una variable que va air iterando, : e indicamis con una tabulacion todas las sentencias
# for d in db.doctores.find():
#     pprint(d)

# db.doctores.insert_one({"nombre":"Shaun","apellido":"Murphy", "edad":30,
#                        "puesto":"asistente quirurgico",
#                        "origen":"Vancouver,Canada"})

# Actualizas un documento
# $set para actualizar algun campo sin perder el documento
# db.doctores.update_one({"nombre":"Shaun"},{"$set":{"origen":"Natrona"}})

# Elimina al que se llama Shaun
# db.doctores.delete_one({"nombre":"Shaun"})
# db.doctores.delete_one({"_id":'ObjectId("636680c2a275951be243564a")'})

# Es como el for pero con una lista
doctores=list(db.doctores.find())
pprint(doctores)