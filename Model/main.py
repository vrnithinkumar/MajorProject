'''
Created on 24-Apr-2014

@author: vr
'''
import creatingMat
import os, sys
from numpy  import *
from numpy.linalg import inv
from sklearn import linear_model
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import Global
import LinearModel
def makeVisual(Y_test,Y_result,label_string):
        Xaxi = range(1, 50)
        Yaxi = [Global.getAccuracy(Y_test, Y_result, i) for i in Xaxi ]
        plt.axis([0, 70, 0, 52])
        plt.xlabel('Success percentage')
        plt.ylabel('Error Tolerance')
        plt.title('Success percentage Against Error Tolerance ')
        plt.plot(Yaxi, Xaxi, color='red', label=label_string, linewidth=2.5, linestyle="-")
        plt.legend()
        plt.show()
def waste():
    colors = ['red', 'blue', 'green']
    labels = {'red':'SVM-Linear', 'blue':'SVM-Polynomial', 'green':'SVM-RBF'}
    Xaxi = range(1, 50)
    
    #visualization
    plt.axis([0, 70, 0, 52])
    plt.xlabel('Success percentage')
    plt.ylabel('Error Tolerance')
    plt.title('Success percentage Against Error Tolerance ')
    results=0
    Y_test_minmax=0
    for result, colr in zip(results, colors): 
        Y_test = [[i] for i in result]
        Yaxi = [Global.getAccuracy(Y_test_minmax, Y_test, i) for i in Xaxi ]
        plt.plot(Yaxi, Xaxi, color=colr, label=labels[colr], linewidth=2.5, linestyle="-")
        plt.legend()
    plt.show()
    
def svr_models(valSet,is_visual,C_cons=1e3):
    
    min_max_scaler = preprocessing.MinMaxScaler()
    svr_lin = SVR(kernel='linear', C=C_cons)
    
    if valSet == None:
        data, label = creatingMat.createDataSet()
        X_train = data[0:-100]
        Y_train = label[0:-100]
        X_test = data[-100:]
        Y_test = label[-100:]
    else:
        X_train = valSet[0]
        Y_train = valSet[1]
        X_test = valSet[2]
        Y_test = valSet[3]   
        X_minmax = min_max_scaler.fit_transform(X_train + X_test)
        Y_minmax = min_max_scaler.fit_transform(Y_train + Y_test)
        X_train_minmax = array(X_minmax[0:-100])
        Y_train_minmax = array(Y_minmax[0:-100])
        X_test_minmax = array(X_minmax[-100:])
        Y_test_minmax = array(Y_minmax[-100:])
    Y_train_minmax_1d=[i[0] for i in Y_train_minmax ]
    Y_result=svr_lin.fit(X_train_minmax,Y_train_minmax_1d).predict(array(X_test_minmax))
    Y_result_new=[[i] for i in Y_result]
    F_result = Global.getAccuracy(Y_test_minmax, Y_result_new, 20)
    return  Global.getCorrelation(Y_test_minmax, Y_result_new)

def findingCinSVR():
    bestSubSet=[ 'tomatoReviews','Genre','Actors2','Actors3','Writer','Budget','Director']
    validateSet=creatingMat.getCrossValidationDatasets(bestSubSet)
    i=.001
    for j in range(100):
        i=i+.001
        print svr_models(validateSet[0],0,i)
    print i
def linear_model_normal(valSet,is_visual):
    if valSet==None:
        data, label = creatingMat.createDataSet()
        X_train=data[0:-100]
        Y_train=label[0:-100]
        X_test=data[-100:]
        Y_test=label[-100:]
    else:
        X_train = valSet[0]
        Y_train = valSet[1]
        X_test = valSet[2]
        Y_test = valSet[3]
        
    linearModel_normal=LinearModel.myLM()
    linearModel_normal.myLMtrain(X_train , Y_train )   
    Y_result=linearModel_normal.myLMpredict(X_test)
    
    
    if is_visual==True:
        
        #visualization
        makeVisual(Y_test,Y_result,'Linear Regression Using Normal equation')
        Global.getAccuracy(Y_test, Y_result, 20)
    else:
        #----------------------- return Global.getAccuracy(Y_test, Y_result, 20)
        return Global.getCorrelation(Y_test, Y_result)
def linear_model_gradient(valSet,is_visual):
    if valSet==None:
        data, label = creatingMat.createDataSet()
        X_train=data[0:-100]
        Y_train=label[0:-100]
        X_test=data[-100:]
        Y_test=label[-100:]
    else:
        X_train = valSet[0]
        Y_train = valSet[1]
        X_test = valSet[2]
        Y_test = valSet[3]
        
    regr = linear_model.LinearRegression()
    Y_result=regr.fit(X_train,Y_train).predict(X_test)
    if is_visual==True:
        
        #visualization
        makeVisual(Y_test,Y_result,'Linear Regression Using Gradient Descent')
        return Global.getAccuracy(Y_test, Y_result, 20)
    else:
        return Global.getAccuracy(Y_test, Y_result, 20)

    
def crossValdiateLMG():
    bestSubSet=[ 'tomatoReviews','Genre','Actors2','Actors3','Writer','Budget','Director']
    validateSet=creatingMat.getCrossValidationDatasets(bestSubSet)
    total=0.0
    for valSet in  validateSet:
        total+=linear_model_gradient(valSet,0)  
        
    print total/10.0
def crossValdiateSVR():
    bestSubSet=[ 'tomatoReviews','Genre','Actors2','Actors3','Writer','Budget','Director']
    validateSet=creatingMat.getCrossValidationDatasets(bestSubSet)
    total=0.0
    for valSet in  validateSet:
        total+=svr_models(valSet,0,.101)  
    print total/10.0

def crossValdiateLMN():
    bestSubSet=[ 'tomatoReviews','Genre','Actors2','Actors3','Writer','Budget','Director']
    validateSet=creatingMat.getCrossValidationDatasets(bestSubSet)
    total=0.0
    for valSet in  validateSet:
        total+=linear_model_normal(valSet,0)  
    print total/10.0    
    
def main():
    print "Linear regression Using Normal Equation "
    crossValdiateLMN()
    print "Linear regression Using SVR Linear kernal "
    crossValdiateSVR()
    #-------------------------- crossValdiateLMG() #normal Equation linear Model
    
    
#--------------------------------------------------------------- findingCinSVR()
if __name__ == '__main__':
    main()
