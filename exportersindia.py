# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import urllib2 as lib2

#url that are the pages interesting
mainurl="exportersindia.com/indian-suppliers/"
# source of urls
baseurl= "http://www.exportersindia.com/indian-manufacturers/plant-seed.htm"
#open the page with urlib2
page = lib2.urlopen(baseurl)
#read the content of the base url
content = page.read()
#use regex to find all urls on page content
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
#array empty
urls_interesteds = []
#find the urls interesting for us who has a seeds 
for i in urls:
    if mainurl in i:
        urls_interesteds.append(i)
        print i
        