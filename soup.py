import requests, re
from bs4 import BeautifulSoup

# urlRandom = 'http://en.wikipedia.org/wiki/Special:Random'
# urlRandom = 'http://en.wikipedia.org/wiki/Wikipedia'
url = 'http://en.wikipedia.org/wiki/Aleksandr_Aksyonov'
r = requests.get(url)
soup = BeautifulSoup(r.text)

while soup.find(id="firstHeading").span.text != "Philosophy":
  content = soup.find(id="mw-content-text")

  paragraphText = str(content.p)
  paragraphText = re.sub(r' \(.*?\) ', '', paragraphText)

  paragraph = BeautifulSoup(paragraphText)
  firstLink = paragraph.find(href = re.compile('/wiki/'))
  if firstLink == None:
    # Case of disambiguation or other page
    firstLink = content.ul.find(href = re.compile('/wiki/'))
    # Rather than find which page is of reference, we choose the 
    # first link in the list text
  print(paragraph.text)
  print(firstLink)

  url = firstLink.get('href')
  r = requests.get(url)
  soup = BeautifulSoup(r.text)

