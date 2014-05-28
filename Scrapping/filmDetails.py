'''
Created on 13-Mar-2014

@author: vr
'''
from bs4 import BeautifulSoup
import urllib2

def fromPage(pageurl):
    response = urllib2.urlopen(pageurl)
    page_source = response.read()
    #--------------------------------------------------------- print page_source
    soup = BeautifulSoup(page_source)
    p1=soup.find_all('td')
    print p1
fromPage("http://www.boxofficemojo.com/movies/?page=daily&id=grind.htm")
