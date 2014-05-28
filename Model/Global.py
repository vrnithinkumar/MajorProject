'''
Created on 29-Apr-2014

@author: vr
'''
import scipy
Atributes=['Year','Director','Rated','Genre','Writer','Actors1','Actors2','Actors3','Production','imdbRating','imdbVotes','Metascore','tomatoMeter','tomatoUserRating','tomatoReviews','tomatoFresh','tomatoRotten','tomatoUserRating','tomatoUserReviews','Budget','BoxOffice']
from scipy.stats.stats import pearsonr
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
    return  (float(PC) / float(l)) * 100

def getCorrelation(xVec, yVec):
    x = scipy.array(xVec)
    y = scipy.array(yVec)
    r_row = pearsonr(x, y)[0]
    return  r_row[0]
