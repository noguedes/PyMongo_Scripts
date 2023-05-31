# !/usr/bin/python3

from pymongo import MongoClient

def check_invalid_parameters(database_name, collection_name):

	client = MongoClient('127.0.0.1', 27017)

	db = client[database_name]

	collection = db[collection_name]


	try:
		cursor  = collection.find({"seu_parametro": {"invalid_operator": "valor"}})
		for document in cursor:
			print(document)

	except Exception as e:
		print(f"Erro ao executar a consulta: {e}")

	client.close()

database_name = input("Digite o nome do banco de dados: ")
collection_name = input("Digite o nome da coleção: ")

check_invalid_parameters(database_name, collection_name)
