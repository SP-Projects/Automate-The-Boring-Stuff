#! python3
# downloadXKCD: downloads all XKCD comics.

#Download pages with the requests module


#find the url of the comic image for a page
#using beautiful soup

#Download and save the comic image to the hard drive
#with iter_content

#Find the URL of the Previous comic and repeat

import os, sys, bs4, requests
from pathlib import Path

download_loc = Path.home() / 'Downloads/XKCD'
try:
    os.mkdir(download_loc)
except FileExistsError:
    print("This really isn't how this should be done")

print(download_loc)
xkcd_url = 'https://xkcd.com'

while not xkcd_url.endswith('#'):
    #download the webpage
    print('Downloading page %s' % xkcd_url)
    res_xkcd = requests.get(xkcd_url)
    res_xkcd.raise_for_status()

    #create bs4 object and parse HTML
    soup_xkcd = bs4.BeautifulSoup(res_xkcd.text, 'html.parser')
    #look for img contained in space with "comic" id
    comic_elem = soup_xkcd.select('#comic img')
    #remember: .select() returns list of html elements

    if comic_elem == [] or 'img' not in comic_elem[0].get('src'):
        print('Could not find comic image')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        print('Downloading image %s...' %comic_url)
        res_xkcd = requests.get(comic_url)
        res_xkcd.raise_for_status()

        xkcd_file = download_loc / os.path.basename(comic_url)
        print(xkcd_file)
        if xkcd_file.exists():
            #if the file exists, it has been downloaded before
            break
        else:
            #save the image to file
            imageFile = open(xkcd_file, 'wb')
            for chunk in res_xkcd.iter_content(1000000):
                imageFile.write(chunk)
            imageFile.close()
    #get the previous buttons url
    prev_link = soup_xkcd.select('a[rel="prev"]')[0]
    xkcd_url = 'https://xkcd.com' + prev_link.get('href')

