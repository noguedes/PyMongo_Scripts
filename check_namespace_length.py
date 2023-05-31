# !/usr/bin/python3

from pymongo import MongoClient 
from pprint import pprint 


client = MongoClient('127.0.0.1', 27017)

with client:
	db = client.sbu
	collections = db.list_collection_names()

	namespace_sizes = {}

	for collection_name in collections:
		stats = db.command('collstats', collection_name)
		namespace_size = stats['storageSize']
		namespace_sizes[collection_name] = namespace_size 

	for collection_name, namespace_size in namespace_sizes.items():
		pprint(f"Tamanho do namespace da coleção '{collection_name}': {namespace_size} bytes")

	client.close()
