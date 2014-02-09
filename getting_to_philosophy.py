#!/usr/bin/python
import sys
import requests, re
from bs4 import BeautifulSoup

MAX_HOPS = 100
count = 0
urlRandom = 'http://en.wikipedia.org/wiki/Special:Random'

if len(sys.argv)==1:
  print("Using http://en.wikipedia.org/wiki/Special:Random")
  url = urlRandom
else:
  url = sys.argv[1]

r = requests.get(url)
soup = BeautifulSoup(r.text)
print(r.url) # Print current url (after redirection)

while soup.find(id='firstHeading').span.text != 'Philosophy':
  if count==MAX_HOPS:
    print("MAX_HOPS reached.")
    break

  content = soup.find(id='mw-content-text')

  paragraph = soup.select('div#mw-content-text > p')[0] # Only DIRECT child
  for s in paragraph.find_all("span"):
    s.replace_with("")
  paragraphText = str(paragraph)
  paragraphText = re.sub(r' \(.*?\)', '', paragraphText)
  # print(paragraphText) # For debugging
  reParagraph = BeautifulSoup(paragraphText)
  firstLink = reParagraph.find(href = re.compile('/wiki/'))

  while firstLink == None:
    # case of disambiguation: use first wiki link in list
    if '(disambiguation)' in url:
      firstLink = content.ul.find(href = re.compile('/wiki/'))
      print(firstLink)

    else:  
      paragraph = paragraph.find_next_sibling("p")
      for s in paragraph.find_all("span"):
        s.replace_with("")
      paragraphText = str(paragraph)
      paragraphText = re.sub(r' \(.*?\)', '', paragraphText)
      reParagraph = BeautifulSoup(paragraphText)
      firstLink = reParagraph.find(href = re.compile('/wiki/'))

  url = 'http://en.wikipedia.org' + firstLink.get('href')
  print(url)
  r = requests.get(url)
  soup = BeautifulSoup(r.text)

  count = count+1

print(str(count) + " hops")