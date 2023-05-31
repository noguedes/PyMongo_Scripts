# !/usr/bin/python3

from pymongo import MongoClient 
from pprint import pprint 

client = MongoClient('127.0.0.1', 27017)

with client: 

	db = client.admin

	status = db.command("serverStatus")
	pprint(status)

client.close()


