#!/usr/bin/env python3
'''
mcb.pyw: Saves and loads pieces of text to the clipboard
usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
       py.exe mcb.pyw list - Loads all keyword to clipboard
       py.exe mcb.pyw delete [<keyword>] deletes a keyword from the shelf.
       if left blank, deletes all keywords
'''
import shelve, pyperclip, sys

#Create Shelf to save content
mcbShelf = shelve.open('mcb')
#TODO: Save clipboard content
try:
    if len(sys.argv) == 3:
        #check two possible commands
        if sys.argv[1].lower() == 'save':
            #sys.argv[2] is the keyword to be saved.
            #save contents of clipboard to shelf file, with keyword
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete':
            del mcbShelf[sys.argv[2]]
    #TODO: List keyword and load content
    elif len(sys.argv) == 2:
        #2 arguments; probably a list, or a keyword
        if sys.argv[1].lower() == 'list':
            #load list to clipboard
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            #delete ALL keywords
            for key in list(mcbShelf.keys()):
                del mcbShelf[key]
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('Unknown argument: ' + str(sys.argv[1]))
except KeyValueError:
    print('Unknown keyword: ' + str(sys.argv[2]))
mcbShelf.close()