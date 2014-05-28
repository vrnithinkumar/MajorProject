import creatingDictionary
import actorRating
import directorRating
import genreRating
import mpaaRating
import productionHouseRating
import writerRating
import Global
import os, sys
from numpy  import *
from numpy.linalg import inv
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib.cbook import tostr
import operator
Atributes = ['Director', 'Rated', 'Genre', 'Writer', 'Actors1', 'Actors2', 'Actors3', 'Production', 'imdbRating', 'imdbVotes', 'Metascore', 'tomatoMeter', 'tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating', 'tomatoUserReviews', 'Budget']

def getAccuracy(orig, pred, error):
    PC = 0
    l = len(orig)
    diff = []
    for i, j in zip(orig, pred):
        EP = (abs(i - j[0]) / j[0]) * 100
        diff.append(EP)
        if abs(EP) < error:
            PC += 1
    # print PC
    return  (float(PC) / l) * 100

def createMatrix(featureSet):
    Director = directorRating.assignAverageRevenue()
    Rated = mpaaRating.assignAverageRevenue()
    Genre = genreRating.assignAverageRevenue()
    Actors1 = actorRating.assignAverageRevenue()
    Actors2 = actorRating.assignAverageRevenue()
    Actors3 = actorRating.assignAverageRevenue()
    Production = productionHouseRating.assignAverageRevenue()
    Writer = writerRating.assignAverageRevenue()
    dataset = creatingDictionary.filler()
    nominalFeatures = ['Actors1', 'Actors2', 'Actors3', 'Director', 'Writer', 'Production']
    nominalFeatures = nominalFeatures + ['Genre', 'Rated']
    
    numericaldata = []
    for film in dataset:
        temp = []
        for feature in featureSet:
            if(feature in nominalFeatures):
                temp.append(eval(feature)[film[feature]])


                
            elif (feature not in ['BoxOffice', 'Film']) :
            # elif (feature not in ['BoxOffice', 'Film', 'imdbVotes', 'tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating', 'tomatoUserReviews']) :
                             
                    temp.append(float(film[feature]))
                               
                

        temp.append(float(film['BoxOffice']))
        numericaldata.append(temp)


    return numericaldata
def createCustomeDataSet(featureList):
    """
    Function to separate matrix in to 2 lists label list and data list
    """
    mixed = createMatrix(featureList)   
    data = []
    label = []         
    for mixedItems in mixed:
        data.append(mixedItems[0:-1])
        label.append([mixedItems[-1]])
    return [data, label]

def getSuccessValue(featureList, tollerance):
    """
        it is for get success ratio of subset 
        Args: list of subset , error tolerance
        Returns: Success rate of corresponding subset
    """
    data, label = createCustomeDataSet(featureList)
    X_train = data[0:-100]
    Y_train = label[0:-100]
    X_test = data[100:]
    Y_test = label[100:]
    regr = linear_model.LinearRegression()
    Y_result = regr.fit(X_train, Y_train).predict(X_test)
    return Global.getAccuracy(Y_test, Y_result, tollerance)

def getinitialSuccess():
    """
    It is used to obtain initail succes of all Attributes
    
    Args:self
    
    Returns:dictionary
    
    Raises:nul
    
    """
    succdic={}
    for feature in Atributes:
        succdic[feature]=getSuccessValue([feature], 20)
    return succdic
def getCorrelationDic():
        corDic={}
        for feature in Atributes:
            x,y=createCustomeDataSet([feature])
            corDic[feature]=Global.getCorrelation(x, y)
        return corDic
    
def backward():
    """
    """
    succdic=getCorrelationDic()
    
    subset=['Director', 'Rated',  'Writer','Genre', 'Actors1', 'Actors2', 'Actors3']
    subset+=['Production', 'imdbRating', 'imdbVotes', 'Metascore', 'tomatoMeter']
    subset+=['tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating']
    subset+=[ 'tomatoUserReviews', 'Budget']
    temp=subset
    old=0.0
    current= getSuccessValue(subset,20)
    for attribut in temp:
        print current
        old=current
        lowest= min(succdic.iteritems(), key=operator.itemgetter(1))[0]
        del (succdic[lowest])
        print lowest
        del (subset[subset.index(lowest )])
        
        current = getSuccessValue(subset,20)
        if(old>current):
            subset+=[lowest]
    print subset
    temp=subset
    for attribut in range(6):
        print current
        old=current
        lowest= min(succdic.iteritems(), key=operator.itemgetter(1))[0]
        del (succdic[lowest])
        print lowest
        del (subset[subset.index(lowest )])
        
        current = getSuccessValue(subset,20)
        if(old>current):
            subset+=[lowest]
    print subset
#-------------------------------------------------------------------- backward()
#----------------------------------------------------- print getCorrelationDic()
# print  getSuccessValue([ 'tomatoReviews','Genre','Actors2','Actors3','Writer','Budget','Director'],20)
        
