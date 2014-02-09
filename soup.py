import requests, re
from bs4 import BeautifulSoup

MAX_HOPS = 100
count = 0
urlRandom = 'http://en.wikipedia.org/wiki/Special:Random'
#url = urlRandom
url = 'http://en.wikipedia.org/wiki/Mauritius'
r = requests.get(url)
soup = BeautifulSoup(r.text)
print(r.url)

while soup.find(id='firstHeading').span.text != 'Philosophy':
  if count==MAX_HOPS:
    break

  content = soup.find(id='mw-content-text')
  #contect = content.find(class_="dablink").replace_with('') # 'class' is reserved word
  
  # Case of disambiguation or other page
  # firstLink = content.parent.ul.find(href = re.compile('/wiki/'))
  
  # Rather than find which page is of reference, we choose the 
  # first link in the list text
  paragraph = soup.select('div#mw-content-text > p')[0] # Only DIRECT child
  for s in paragraph.find_all("span"):
    s.replace_with("")
  paragraphText = str(paragraph)
  print(paragraphText)
  paragraphText = re.sub(r' \(.*?\)', '', paragraphText)
  #paragraphText = re.sub(r' \(.*?\)', '', paragraphText)

  reParagraph = BeautifulSoup(paragraphText)
  firstLink = reParagraph.find(href = re.compile('/wiki/'))

  while firstLink == None:
    if '(disambiguation)' in url:
      firstLink = content.ul.find(href = re.compile('/wiki/'))
      print(firstLink)

    else:  
      #print(firstLink)
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

print(count)