'''
Created on 12-Mar-2014
Module get budget from budget.txt
@author: vr
'''

    
#--------------------------Global Variables---------------------------------------------------- 
GBudgetFile = "../Data/Budget.txt"  # path to Budget File
#------------------------------------------------------------------------------ 
def getBudgetDic(fileName):
    """To make an Dictionary of budgets"""
    fname = fileName
    with open(fname) as f:
        content = f.readlines()
    dic = {}
    for i in content:
        name = i.split()[0]
        budg = i.split()[1]
        dic[name] = budg
    return  dic

def stringCorrectify(strvalue):
    return strvalue.strip().replace(' ', '_').split('(')[0]

GbudgetDictionary = getBudgetDic(GBudgetFile)  # Global Dictionary

def getBudget(filmName):
    """To return corresponding budget for a film from budget.txt"""
    try:
        return GbudgetDictionary[stringCorrectify(filmName)]
    except:
        return "NIL"

