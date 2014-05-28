import sys
import pymongo
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
	"""Connection testing"""
	try:
		c = Connection(host="localhost", port=27017)
		print "Connection Success"
	except ConnectionFailure, e:
		sys.stderr.write("Could Not Connect: %s" % e)
		sys.exit(1)
	# Get a Database handle to a database named "mydb"
	dbh = c["mydb"]
	print "Db handle created Successfully"
	assert dbh.connection == c
	# Addinng a file to Collection called Chikcs
	# fileObj={
	# 	"fName":"Amy",
	# 	"sName":"Oliver",
	# 	"chickRate":6,
	# 	"rank":32
	# }
	# safe=True ensures that your write
	# will succeed or an exception will be thrown
	# dbh.chicks.insert(fileObj,safe=True)
	#--------------

	# print pymongo.DESCENDING
	# to count the result use count()
	# print 	dbh.chicks.find().count()
	# {"$and":[{"fName":"Amy"},{"rank":{"$gt":4}}]} used for AND in mongodb
	# To sort sort("Atribute",1 or -1) eg:find().sort("rank",-1) == find(sort=[("rank",-1)])
	# .limit(2) is used to limit the result
	for i in dbh.chicks.find(sort=[("rank", -1)]).limit(4):
		print i["sName"]
		print i["rank"]

	dbh.chicks.update({"fName":"Natalie"}, {"$set":{"sName":"Coochisdsad", "rank":254}})
	for i in dbh.chicks.find(sort=[("rank", -1)]):
		print i["sName"]
		print i["rank"]






if __name__ == "__main__":
	main()
