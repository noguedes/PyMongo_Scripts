#!/usr/bin/python3 

from pymongo import MongoClient 
from pprint import pprint 

client = MongoClient('127.0.0.1', 27017)

with client: 

	db = client.sbu
	pprint(db.collection_names())

	status = db.command("dbstats")
	pprint("Status do banco:")
	pprint(" ")
	pprint (status)

client.close()
