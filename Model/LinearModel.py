'''
Created on 24-Apr-2014

@author: vr
'''
from numpy  import *

class myLM:
    #------------------------------------------------------- def __init__(self):
        #-------------------------------------------------------- self.theta=nan
        
    def myLMtrain(self,data, label):
        xxm = mat(data)
        yym = mat(label)
        self.theta = ((((xxm.T * xxm).I)) * xxm.T) * yym
    
    def myLMpredict(self,test):
        rest = test * self.theta
        return rest

    def gettheta(self):
        return self.theta
