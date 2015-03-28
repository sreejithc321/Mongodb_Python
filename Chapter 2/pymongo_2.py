import pymongo
import sys

connection = pymongo.MongoClient('mongodb://localhost')
db = connection.school
scores = db.scores

def find():
	query = {'type' : 'exam'}
	## Hide objectid
	projection = {'student_id':1, '_id' :0}
	try:
		## select 'projection' from 'query'
		result = scores.find(query,projection)
		for doc in result:
			print doc
	except	Exception as e:
		print type(e),e
		
find()		
	
