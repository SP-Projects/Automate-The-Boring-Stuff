#!python3 
import webbrowser, sys
import pyperclip

'''
 - 1. Get's a street address from command line or clipboard
 - 2. Opens the web browser to google maps page for address
 
Code does the following:
1. Read command line args from sys.argv
2. Read the clipboard contents
3. Call the webbrowser.open() function
'''

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

