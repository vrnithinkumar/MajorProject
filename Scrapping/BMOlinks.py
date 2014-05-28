'''
Created on 12-Mar-2014
for Getting info from Boxoffice mojo
@author: vr
'''
from bs4 import BeautifulSoup
import urllib2

def fromPage(pageurl):
    response = urllib2.urlopen(pageurl)
    page_source = response.read()
    soup = BeautifulSoup(page_source)
    p1=soup.find_all('tr',bgcolor="#f4f4ff")
    p2=soup.find_all('tr',bgcolor="#ffffff")
    return [p1,p2]

    
def yearWise(year):
    fName="../Data/BOM%d.txt"%(year)
    for pageNo in range(1,4):
        link="http://www.boxofficemojo.com/daily/?view=bymovie&yr=%d&page=%d&sort=title&order=ASC&p=.htm"%(year,pageNo)
        linkList=fromPage(link)
        for ls in linkList:
            for i in ls:
                lnk=i.contents[0]
                with open(fName, "a") as fileToWrite:
                    linkBuffer = 'http://www.boxofficemojo.com/'+lnk.a['href']+"\n"
                    fileToWrite.write(linkBuffer)
def main():
    for year in range(2003,2014):
        yearWise(year)
    
if __name__ == "__main__":
    main()
    print "Finished"