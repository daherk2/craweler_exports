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
        #print i

telephone_list = open('telephone.txt','w')
name_list = open('name.txt','w')
address_list = open('address.txt','w')
email_list = open('email.txt','w')
#for j in urls_interesteds:
print urls_interesteds[0]
page = lib2.urlopen(urls_interesteds[0])
content = page.readlines()
telephone_tag = "icon-phone-alt dif list_dn"
name_tag = "ml0px grid_dn vam si w16px icon-vtrust"
address_tag = "span itemprop"
email_tag = "hig grid_dn"
print 'verificando tags'
for i in content:
    if telephone_tag in i:
        telephone_list.write(i)
    if name_tag in i:
        name_list.write(i)
    if address_tag in i:
        address_list.write(i)
    if email_tag in i:
        email_list.write(i)    

print 'tags verificadas'

telephone_list.close()
name_list.close()
address_list.close()
email_list.close()
