import creatingDictionary
import actorRating
import directorRating
import genreRating
import mpaaRating
import productionHouseRating
import writerRating
import os, sys
from numpy  import *
from numpy.linalg import inv
from sklearn import linear_model
import matplotlib.pyplot as plt
import FeatureSubset
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

def createMatrix():
    Director = directorRating.assignAverageRevenue()
    Rated = mpaaRating.assignAverageRevenue()
    Genre = genreRating.assignAverageRevenue()
    Actors1 = actorRating.assignAverageRevenue()
    Actors2 = actorRating.assignAverageRevenue()
    Actors3 = actorRating.assignAverageRevenue()
    Production = productionHouseRating.assignAverageRevenue()
    Writer = writerRating.assignAverageRevenue()
    dataset = creatingDictionary.filler()
    features = ['Actors1', 'Actors2', 'Actors3', 'Director', 'Writer', 'Production']
    features = features + ['Genre', 'Rated']
    numericaldata = []
    for film in dataset:
        temp = []
        for feature in film:
            if(feature in features):
                temp.append(eval(feature)[film[feature]])


                
            elif (feature not in ['BoxOffice', 'Film', 'tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating', 'tomatoUserReviews']) :
            # elif (feature not in ['BoxOffice', 'Film', 'imdbVotes', 'tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating', 'tomatoUserReviews']) :
                             
                    temp.append(float(film[feature]))
                               
                

        temp.append(float(film['BoxOffice']))
        numericaldata.append(temp)


    return numericaldata
def createDataSet():
    """
    Function to separate matrix in to 2 lists label list and data list
    """
    mixed = createMatrix()   
    data = []
    label = []         
    for mixedItems in mixed:
        data.append(mixedItems[0:-1])
        label.append([mixedItems[-1]])
    return [data, label]
def getCrossValidationDatasets(featureSet):
    data, label = FeatureSubset.createCustomeDataSet(featureSet)
    crossValidationSet = []
    for i in range(0, 1000, 100):
        validationset = [data[0:i] + data[i + 100:], label[0:i] + label[i + 100:], data[i:i + 100], label[i:i + 100]]
        crossValidationSet.append(validationset)
    return crossValidationSet
    
    
