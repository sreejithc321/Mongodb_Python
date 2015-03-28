import pymongo
import sys

DB_NAME = 'school'
COLLECTION_NAME = 'scores'

# Connect to DB
connection = pymongo.MongoClient("mongodb://localhost")
database = connection[DB_NAME]
collection = database[COLLECTION_NAME]

def find_one():
	query = {'student_id':15}
	try:
		doc = collection.find_one(query)
		print doc
	except Exception as e:
		print type(e),e
		
def find():
	query = {'type':'quiz'}
	try:
		doc = collection.find(query)
		for item in doc:
			print item
	except Exception as e:
		print type(e),e	
		
find_one()		
find()
