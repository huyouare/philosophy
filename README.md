## Getting to Philosophy: A Wikipedia Phenomenon

You can find the Wikipedia page here: http://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

> Clicking on the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, usually eventually gets you to the Philosophy article. As of May 26, 2011, 94.52% of all articles in Wikipedia lead eventually to the article Philosophy. The remaining 100,000 (approx.) links to an article with no wikilinks or with links to pages that do not exist, or get stuck in loops (all three are equally probable). The median link chain length to reach philosophy is 23.

Following the chain consists of:

1. Clicking on the first non-parenthesized, non-italicized link
2. Ignoring external links, links to the current page, or red links
3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs

### Notes
* Currently defines main text as non-italicized, non-parenthesized text that does not appear inside a table.
* Pages with tables alone will not lead to another page
* By default, getting_to_philosophy.py will use a random Wiki page, generated from http://en.wikipedia.org/wiki/Special:Random
* My last test showed an average of 19 hops, ignoring those that did not have valid links and those that had infinite loops.

### Getting Started
######Install dependencies:  
`pip install -r requirements.txt`

###### Using the script:  
`python getting_to_philosophy.py STARTING_LINK`

###### Example:  
`python getting_to_philosophy.py http://en.wikipedia.org/wiki/Property_(philosophy)`

###### Output:  
`http://en.wikipedia.org/wiki/Property_(philosophy)
http://en.wikipedia.org/wiki/Modern_philosophy
http://en.wikipedia.org/wiki/Philosophy
2 hops`

###### Testing (100 random trials):  
`python test.py`