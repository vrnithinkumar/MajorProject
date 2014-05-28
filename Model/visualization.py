'''
Created on 28-Apr-2014

@author: vr
'''
import pylab as pl



import creatingDictionary
import actorRating
import directorRating
import genreRating
import mpaaRating
import productionHouseRating
import writerRating
import Global

def createMatrix(atribute):
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
        if(atribute in features):
            temp.append(eval(atribute)[film[atribute]])  
        else :
            # elif (feature not in ['BoxOffice', 'Film', 'imdbVotes', 'tomatoUserRating', 'tomatoReviews', 'tomatoFresh', 'tomatoRotten', 'tomatoUserRating', 'tomatoUserReviews']) :
            temp.append(float(film[atribute]))
                               
                

        temp.append(float(film['BoxOffice']))
        numericaldata.append(temp)


    return numericaldata

def draw(atribute):
    data = createMatrix(atribute)
    Y = [i[0] for i in data ]
    X = [i[1] for i in data ]
    pl.scatter(X, Y, c='r',marker='x', label='Movies',alpha=.75)
    pl.ylabel(atribute)
    pl.xlabel('BoxOffice')
    pl.title(atribute+" VS "+'BoxOffice')
    pl.legend()
    pl.savefig(atribute)
    pl.show()

def main():
    for atribute in Global.Atributes:
        draw(atribute)
if __name__ == '__main__':
    #-------------------------------------------------------------------- main()

