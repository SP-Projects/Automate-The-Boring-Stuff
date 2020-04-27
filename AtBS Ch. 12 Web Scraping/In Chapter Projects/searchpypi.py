#! python3
# searchpypi.py.py - opens several search results from pypi

'''
Program does the following:

 1. Gets search keywords fro the command line arguments
  - Read command line args from sys.argv
 2. Retrieves the search results page
  - Fetch the search result page with the requests module
 3. Opens a browser tab for each result
  - Find the links to each search result
  - Call the webbrowser.open() function to open the tabs
'''

import requests, sys, webbrowser, bs4

res = requests.get('https://pypi.org/search/?q='\
    + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: retrieve top search result link
#pypi returns results with css class attribute named Package-snippet

soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Get all search results
#This portion may need updating in future.
linkElems = soup.select('.package-snippet')
numToOpen = min(5, len(linkElems))
for i in range(numToOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening ' , urlToOpen)
    webbrowser.open(urlToOpen)