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
import logging

######################################
# Import and output files

FILE_IN = 'data/input/fr-test.txt'
FILE_OUT = 'data/test_output.txt'

######################################
# Language settings
LANG = 'fr'
ANKI_PREFIX = 'autoanki-'+LANG+'-'  # tag all media files in case I have to delete them later
MEDIA_DIR = 'downloads/images/'
AUD_DIR = 'audio/'

# logging.basicConfig(level='DEBUG')

# TODO: automate importing data / passing directories (e.g. saving decks and media)
# TODO: test accents in spelling
# TODO: rip photos
# TODO: add capability for priority/usage frequency
# TODO: interface to help pick photos
# TODO: gender (color coding possible)

######################################

print(Fore.GREEN + '\nautoAnki\n' + Style.RESET_ALL) 

print(Fore.RED + "Testing import and scraping" + Style.RESET_ALL)
french_dict = AnkiDictionary(FILE_IN, 'fr')
french_dict.scrape_deck(['translation', 'audio'])

french_dict.print_deck()

# find images and fill in url
cwd = os.getcwd()
leading = cwd + "/" + MEDIA_DIR

# imgFiles = files(MEDIA_DIR  )

