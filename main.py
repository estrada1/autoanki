#!/usr/bin/python3

"""@package docstring
autoAnki library to help make language flashcards in Anki

Author: Matt Estrada
"""

import os
import datetime
import csv

# import sys
# print(sys.path)
from colorama import Fore, Back, Style # color printouts

from autoAnki import AnkiDictionary, AnkiNote
# from ripWordRef import ripWordRef
# from ripImage import ripImage
# from redundancy import files
import logging

######################################
# Import and output files

FILE_IN = 'data/input/fr-test.txt'
FILE_OUT = 'data/test_output.txt'

######################################
# Language settings
LANG = 'fr'
ANKI_PREFIX = 'autoAnki_'+LANG+' '  # tag all media files in case I have to delete them later
MEDIA_DIR = 'downloads/images/'
AUD_DIR = 'downloads/audio/'

logging.basicConfig(level='DEBUG')

# TODO: generate first anki card
# TODO: scrape first web reference
# TODO: allow program to pick up after an error, perhaps scan through directory?
# TODO: count number of things here
# TODO: add capability for priority/usage frequency
# TODO: graphical interface to help pick photos
# TODO: add proper logging function 
# TODO: male/female? stick the le/la in front of there to help memorize

######################################

print(Fore.GREEN + '\nautoAnki\n' + Style.RESET_ALL) 
french_dict = AnkiDictionary(FILE_IN, 'fr')

test_note = AnkiNote({'fr': 'voiture', 'en': 'car'})
print(Fore.RED + "Testing card class" + Style.RESET_ALL)
test_note.print_note()
test_note.scrape_wordref(['translation'])

# find images and fill in url
cwd = os.getcwd()
leading = cwd + "/" + MEDIA_DIR  

# imgFiles = files(MEDIA_DIR  )

"""
with open(FILE_OUT, 'a', newline='') as tsvfile:  # a stands for append

    for thisNote in thisDict:

        thisFr = thisNote.fr
        print('Word\t'+ Fore.CYAN + thisFr + Style.RESET_ALL)

        # if not redundantWord(thisFr, imgFiles):

        # IMAGE
        imgAbsPath = ripImage(thisFr)

        # If unable to find picture
        if not imgAbsPath:
            print('Error: ' + thisFr + ' did not return an image')
            thisNote.logError('data/errors.txt','Could not find image', datetime.datetime.now())
            continue        # TODO: Possible to handle with with exception?

        imgPathSplit = imgAbsPath.rsplit(leading)
        imgAbsPath2 = leading + ANKI_PREFIX + imgPathSplit[1]
        imgName = ANKI_PREFIX + imgPathSplit[1] # trying this out
        os.rename(imgAbsPath, imgAbsPath2)
        thisNote.img = imgNAnkiDictionary
        # AUDIO
        audPath = ripWordRef(thisFr)

        if not audPath:
            print('Error: ' + thisFr + ' did not return an audio path')
            thisNote.logError('data/errors.txt', 'Could not find audio', datetime.datetime.now())
            continue  # TODO: Possible to handle with with exception?

        audPathSplit = audPath.rsplit(AUD_DIR)
        audName = ANKI_PREFIX + audPathSplit[1]
        audPath2 = AUD_DIR + ANKI_PREFIX + audPathSplit[1]
        os.rename(audPath, audPath2)

        # write new line
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow([thisNote.fr, thisNote.eng, thisNote.aud, thisNote.img])

tsvfile.close()

print("\n" "Output file written to ", FILE_OUT)
  # # os.rename("downloads/images/" + thisImgPath, "downloads2/" + thisImgPath)
    # row.img = thisAbsPath

"""
