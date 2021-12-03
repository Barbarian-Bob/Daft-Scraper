#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
import tabulate



geturls = ['https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=180'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=20'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=40'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=60'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=80'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=100'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=120'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=140'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=160'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=180'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=200'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=220'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=240'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=260'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=280'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=300'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=300'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=320'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=340'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=360'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=380'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=400'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=420'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=440'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=460'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=480'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=500'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=500'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=520'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=540'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=560'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=580'
,'https://www.daft.ie/dublin/property-for-sale/?s%5Badvanced%5D=1&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=sale&offset=600'
] 



urls = [] 

for page in geturls:
    page = urllib.request.urlopen(page) # conntect to website
    soup = BeautifulSoup(page, 'html.parser') 
    Link = soup.findAll("a", {"class": "PropertyInformationCommonStyles__addressCopy--link"})
    for link in Link:
        link = link.get('href')
        httplink = ("https://www.daft.ie" + link)
        urls.append(httplink)


df = pd.DataFrame(columns=[
     "Date"
    ,"Daft_URL"
    ,"Propert_Type"
    ,"Address"
    ,"Eircode"
    ,"Bedrooms"
    ,"Bathrooms"
    ,"M2"
    ,"Price"
    ,"Price_per_M2"
   ]) 




for index,url in enumerate(urls):

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    Date_Posted_List = soup.find("div", {"class": "PropertyStatistics__iconData"})
    Date_Posted_List = Date_Posted_List.getText() if Date_Posted_List else 'Null'
    Date_Posted_List = Date_Posted_List.replace('.', '/')
    print(Date_Posted_List)
       
    link = url
    print(url)

    Propert_Type = soup.find("div", {"class": "QuickPropertyDetails__propertyType"})
    Propert_Type = Propert_Type.getText() if Propert_Type else 'Null'
    Propert_Type = Propert_Type.strip()
    print(Propert_Type)
    
    Address = soup.find("h1", {"class": "PropertyMainInformation__address"})
    address = Address.getText() if Address else 'Null'
    address = address.replace('\n', '')
    address = address.replace('\xa0', '')
    address = address.replace('\n', '')
    print(address)
    
    Eircode = soup.find("div", {"class": "PropertyMainInformation__eircode"})
    eircode = Eircode.getText() if Eircode else 'Null'
    eircode = eircode.replace('Eircode: ','')
    eircode = eircode.replace('\n', '')
    eircode = eircode.replace('\xa0', ' ')
    eircode = eircode.replace('\n', '')
    eircode = eircode.strip()
    print(eircode)
    
    Bed = soup.find("div", {"class": "QuickPropertyDetails__iconCopy"})
    Bed = Bed.getText() if Bed else 'Null'
    
    Bath = soup.find("div", {"class": "QuickPropertyDetails__iconCopy--WithBorder"})
    Bath = Bath.getText() if Bath else 'Null'
    
    Size = soup.find("div", {"class": "PropertyOverview__propertyOverviewDetails"})
    size = Size.getText() if Size else 'Null'
    size = size.replace('Overall Floor Area:','')
    size = size.replace('For Sale by Private Treaty','')
    size = size.replace(' m2','')
    size = size.strip()
    size = size.strip()
    print(size)
    
    Price = soup.find("strong", {"class": "PropertyInformationCommonStyles__costAmountCopy"})
    Price = Price.getText() if Price else 'Null'
    Price = Price.replace('€','')
    Price = Price.replace(',','')
    Price = Price.strip()
    print(Price)
    
    try:
        Price_M2 = round(float(Price)/float(size),2)  if Price else 'Null'
    except:
        Price_M2 = "Null"
    
#    Price_M2 = float(Price)/int(size) if Price is not 'Null' else 'Null'
#    print(Price_M2)
    
    row = [Date_Posted_List, link, Propert_Type, address, eircode, Bed, Bath, size, Price, Price_M2 ]
    print(row)    
    
    a_series = pd.Series(row, index = df.columns)
    df = df.append(a_series, ignore_index=True)


print(Price_M2)
print(row)


data = pd.read_csv('/Users/roberthobbs/Documents/Daft2.csv')

df2 = pd.concat([data, df])
df2 = df2.drop_duplicates(keep=False)

print(df2)

with open('/Users/roberthobbs/Documents/Daft2.csv', 'w') as f:
    df2.to_csv(f, header=True, index=False, encoding='utf-8')

print('helloworld3')

#with open('/Users/Hobbs/Documents/Daft.html', 'a') as f:
#    df.to_html(f, header=False)

