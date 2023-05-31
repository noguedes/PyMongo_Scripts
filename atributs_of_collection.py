# !/usr/bin/python3 

from pymongo import MongoClient 
from pprint import pprint 

client = MongoClient('127.0.0.1', 27017)

with client:

	db = client.sbu 
	collection = db.apolices

	# obtendo todos os ducumentos da coleção 
	documents = collection.find()

	# Quantidade de documentos 
	qtd_docs = collection.count()
	pprint(f"Esta coleção tem: {qtd_docs} documentos")

	# conjunto de campos únicos 
	unic_keys = set()

	# Iterando sobre os ducumentos e coletando os campos únicos 
	for document in documents:
		unic_keys.update(document.keys())

	# campos encontrados 
	pprint(f"Campos encontrados na coleção:")
	for field in unic_keys:
		pprint(field)

	client.close()
