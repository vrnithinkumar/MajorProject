'''
Created on 12-Mar-2014

@author: vr
'''
from toaddmore import getBudget 
import pymongo
import json
import os
import sys
from collections import Counter
import operator 
from pymongo import Connection
from pymongo.errors import ConnectionFailure


    # safe=True ensures that your write
    # will succeed or an exception will be thrown
    # dbh.chicks.insert(fileObj,safe=True)
    #--------------

    # print pymongo.DESCENDING
    # to count the result use count()
    # print     dbh.chicks.find().count()
    # {"$and":[{"fName":"Amy"},{"rank":{"$gt":4}}]} used for AND in mongodb
    # To sort sort("Atribute",1 or -1) eg:find().sort("rank",-1) == find(sort=[("rank",-1)])
    # .limit(2) is used to limit the result
    





def budgetConverter(bString):
    """To Convert String value of budget to Float Value"""
    if(bString[0] == '$'):
        bFloat = float(bString[1:-1])
        if(bString[-1] == 'M'):
            bFloat *= 1000000
            return bFloat
        elif(bString[-1] == 'k'):
            bFloat *= 1000
            return bFloat

    else:
        return 0.0

def selectFirst(valueSet):
    return valueSet.split(',')[0]

def stringCorrectify(strvalue):
    return strvalue.strip().replace(' ', '_').split('(')[0]

def valueCorrectify(numvalue):
    splited = numvalue.split(',')
    withoutComma = ""
    for values in splited:
        withoutComma += values
    return withoutComma

def main():
    """Connection testing"""
    try:
        dbConnection = Connection(host="localhost", port=27017)
        print "Connection Success"
    except ConnectionFailure, e:
        sys.stderr.write("Could Not Connect: %s" % e)
        sys.exit(1)
    # Get a Database handle to a database named "dbHandle"
    dbHandle = dbConnection["filmsDb"]
    print dbHandle
    print "Db handle created Successfully"
    assert dbHandle.connection == dbConnection
    # Make an Db Collection named DatasDb
    dbCollection = dbHandle.DatasDb
    # Make an Db Collection Backup named DatasDb
    print dbCollection.find().count()

    for items in dbCollection.find():
        if getBudget(items["Title"].encode('ascii', 'ignore')) != "NIL":
            with open("FilmNames&year&BO.txt", "a") as fileToWrite:
                actorList = items["Actors"].encode('ascii', 'ignore').split(',')
                wbuffer = ""
                #---------------------------------- Things to added to text file
                wbuffer += stringCorrectify(items["Title"].encode('ascii', 'ignore')) + " " 
                wbuffer += items["Year"].encode('ascii', 'ignore') + " "
                wbuffer += stringCorrectify(items["Director"].encode('ascii', 'ignore')) + " "
                wbuffer += stringCorrectify(items["Rated"].encode('ascii', 'ignore')) + " "
                wbuffer += stringCorrectify(selectFirst(items["Genre"].encode('ascii', 'ignore'))) + " "
                wbuffer += stringCorrectify(selectFirst(items["Writer"].encode('ascii', 'ignore'))) + " "
                wbuffer += stringCorrectify(actorList[0]) + " "
                wbuffer += stringCorrectify(actorList[1]) + " "
                wbuffer += stringCorrectify(actorList[2]) + " "
                wbuffer += stringCorrectify(items["Production"].encode('ascii', 'ignore')) + " "
                wbuffer += items["imdbRating"].encode('ascii', 'ignore') + " "
                wbuffer += valueCorrectify(items["imdbVotes"].encode('ascii', 'ignore')) + " "
                wbuffer += items["Metascore"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoMeter"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoUserRating"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoReviews"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoFresh"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoRotten"].encode('ascii', 'ignore') + " "
                wbuffer += items["tomatoUserRating"].encode('ascii', 'ignore') + " "
                wbuffer += valueCorrectify(items["tomatoUserReviews"].encode('ascii', 'ignore')) + " "
                wbuffer += getBudget(items["Title"].encode('ascii', 'ignore')) + " "
                #-------------------------------------------------- End of items
                wbuffer += str(budgetConverter(items["BoxOffice"].encode('ascii', 'ignore'))) + '\n'
                fileToWrite.write(wbuffer)
                #------- with open("TrainingDataLabel.txt", "a") as fileToWrite:
                    # fileToWrite.write(str(budgetConverter(items["BoxOffice"].encode('ascii', 'ignore'))) + '\n')



if __name__ == "__main__":
    main()
    print "Finished"
