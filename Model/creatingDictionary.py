import os
# Functions in this file converts the dataset which is in text csv format into
# a list of Python dictionaries.
DATADIR = ""
DATAFILE = "TrainingData.txt"


def parse_file(datafile):
    '''
    This function converts the dataset(comprising of information regarding
    around 2000 films) in csv format to a list of python dictionaries.    
    '''
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        # The header variable is a list which stores the names of the keys
        # in our output list of dictionaries.
        # The first line in the database is the names of the featues separated
        # by commas. ie a python string.
        # Calling split on this string with delimiter comma(",") returns the
        # names of the features as a list
        counter = 0
        for line in f:
            if counter == 1050:
                break
            fields = line.split()
            # The values themselves are separated by spaces in the dataset.
            # Space is the default argument for the split method. So there is no
            # need to provide the parameter here.
            # Now the values of the attributes for a single film is stored as a
            # list in the fields variable
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()
                # Strip method removes the unnecessary whitespaces from the
                # the beginning and end of a string.
                # This for loop populates the list of dictionaries,
                # by assigning the appropriate values
                

            data.append(entry)
            counter += 1

    return data
#------------------------------------------------------------- def getMeanDic():
    #------------------------------------------------------------ filmDic=test()
    #------------------------------------------------------ for film in filmDic:
        #----------------------------------------------------- for feat in film:
            
    

def test():
    # The test function is the driver program.
    # This runs the parse_file method on our input dataset 
    # by calling it with the proper arguments.
    
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    return d
  
test()

def featureMean():
    filmDic = test()
    meanDic = {'tomatoUserRating': '3.4', 'tomatoReviews': '160', 'tomatoUserReviews': '285130', 'tomatoRotten': '51', 'tomatoMeter': '68', 'Metascore': '62', 'BoxOffice': '92900000.0', 'Year': '2000', 'tomatoFresh': '109', 'imdbRating': '7.2', 'imdbVotes': '192547'}
    for item in meanDic:
        total = 0
        count = 0
        for film in filmDic:
           if(film[item] != 'N/A'):
               count += 1
               total += float(film[item])

        meanDic[item] = int(total / count)

    return meanDic

def filler():
    filmDic = test()
    meanDic = featureMean()
    for item in meanDic:
        for film in filmDic:
            if(film[item] == 'N/A'):
                film[item] = meanDic[item]


    return filmDic

def nullcheck():
    filmDic = filler()
    # items=featureMean()
    count = 0
    for film in filmDic:
        for feature in film:
           if(film[feature] == 'N/A'):
               count += 1
    return count

        
    

