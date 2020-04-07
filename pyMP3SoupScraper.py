from bs4 import BeautifulSoup
import urllib.request
import re
import sys
import os

myPath = "C:/Downloads/"
print("Please enter the website page that contains the mp3 files:")
site_url = input()
url = urllib.request.urlopen(site_url)
content = url.read()
soup = BeautifulSoup(content, features="html.parser")
amount = [a.get(".mp3") for a in soup.findAll('a',href=re.compile('http.*\.mp3'))]
print("Found", len(amount) , "files!")
print("Found these links on the web page:")
for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
    print ("URL:", a['href'])

print("Download all? y/n")
download_allowed = input()
current_item = 0
if download_allowed.lower() == "y":
    for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
        current_item += 1
        print ("(",current_item,"/", len(amount), ") Downloading URL:", a['href'])
        url = a['href']
        filename = url.split("/")[-1]
        fullfilename = os.path.join(myPath, filename)
        urllib.request.urlretrieve(url, fullfilename)
        print("File saved as "+ fullfilename)

    print("Ya done!")
