
# A sample Python web script to read data from mongodb and print it in browser

import bottle
import pymongo

# default path of webserver
@bottle.route('/')
def index():
	# mongodb connection
	connection = pymongo.MongoClient('localhost',27017)
	db = connection.test # database
	col_names = db.things # collection 
	item = col_names.find_one()
	return '<b>Hello %s !</b>' %item['name']
	
bottle.run(host='localhost',port=8082)	
	
	
