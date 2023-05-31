from pymongo import MongoClient 

def check_validator_coll(database_name, collection_name)

	client = MongoClient('127.0.0.1', 27017)

	db = client[database_name]

	collection = client[collection_name]
