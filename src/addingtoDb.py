import pymongo
import json
import os
from collections import Counter
import operator 

dirs="/home/vr/Main_Project/Yearwise_nongit/data2010/"
#Finished 2000,2001,
# Adding Connection to Db
con=pymongo.Connection('localhost',27017)
filmdb=con.filmsDb
DataCol=filmdb.DatasDb 

# DataCol.remove()

def addingBypath(path):
    print "No of Files to be added %d" %(len(os.listdir(path)))
    for jFile in os.listdir(path):
        with open (path+jFile) as dataFile:
            try:
                data = json.load(dataFile)
                DataCol.insert(data)
            except ValueError:
                print jFile
    print "Success fully added"
# addingBypath(dirs)
# DataCol.remove({"Response":"False"})
print DataCol.find().count()
directorList=[]
print DataCol.find_one({"Title":"Munich"})
for i in list(DataCol.find({"Language":"English"})):
    print i["Title"].encode('ascii', 'ignore') #to avoid ascii error
    directorList.append(i["Director"].encode('ascii', 'ignore'))
print DataCol.find_one({"Director":"Aamir Khan, Amole Gupte"})
W_C=Counter()
W_C.update(directorList)
    #print page.extractText()+"----------"
S_W_C= sorted(W_C.iteritems(), key=operator.itemgetter(1))
print S_W_C