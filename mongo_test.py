from pymongo import MongoClient 

# Conexão ao servidor MongoDB
client = MongoClient('127.0.0.1', 27017)

# Acessar o banco 
db = client['admin']

# acessar a coleção "system.users"
users_collection = db['system.users']

# recuperando documentos (usuários)
users = users_collection.find()

# imprimindo os usuários 

for user in users:
	print(user)

# fechando conexão
client.close()

