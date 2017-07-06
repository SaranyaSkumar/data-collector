# scrapped from grotal.com
#Developed By-Saranya S kumar
# Date - 05-06-2017
# import all the libraries that we are going to use.
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# specify the url
req = urllib2.Request("https://www.grotal.com/Kochi-Ernakulam/Government-Offices-C99/", headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen( req )
# parse the html using beautiful soap and store in variable `soup`
soup=BeautifulSoup(page,'html.parser')
#find name
name=[]
for n in soup.find_all('div',attrs={"class" : "cursor"}):
    name.append(n.text)

print name
#find address
address=[]
for p in soup.find_all('div',attrs={"class" : "address"}):
     address.append(p.text)

print address
#find contactnumber
contact=[]
for c in soup.find_all('div',attrs={"class":"ph-no"}):
    contact.append(c.text)
print contact

result=[]
result=zip(name,address,contact)
#print data
print result
import csv
from datetime import datetime
# Opening CSV file / create
with open('central_govt_offices_in_kochi_list.csv','wb')as csv_file:
    # Write Buffer
	writer=csv.writer(csv_file)
    # Writing Variables to csv file
	for row in result:
	 writer.writerow(row)
