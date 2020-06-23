"""@package docstring

"""
import csv
from collections import deque
import ipdb
from colorama import Fore, Back, Style  # color printouts
from google_images_download import google_images_download
import unidecode
import requests, sys, webbrowser, bs4, os
import logging
import re


class AnkiDictionary:
    """ Dictionary of AnkiNotes

    """
    def __init__(self, file_in, lang):
        """use csv library to read in tsv file and return a deck of AnkiNotes
        """

        self.note_deque = deque()

        verbFields = ['freq', 'fr', 'en']

        # Label columns that are being read in
        with open(file_in, newline='') as tsvfile:
            reader = csv.DictReader(tsvfile,
                                    delimiter='\t',
                                    fieldnames=verbFields)
            for row in reader:
                this_note = AnkiNote(row)
                self.note_deque.append(this_note)
        print("Imported words: ")
        self.print_deck()

    def print_deck(self):
        """ Iteratively print all notes in the deck 

        """
        for note in self.note_deque:
            note.print_note()

    def scrape_deck(self, fields):
        """ Scrape media and translation for cards

        """
        for note in self.note_deque:
            print('Scraping note: ' + Fore.CYAN + note.fr + Style.RESET_ALL)
            note.scrape_wordref(fields)
            print()

class AnkiNote:
    """Store info (e.g. audio path, english translation) for constructing an Anki
    Note.

    """
    def __init__(self, dict_entry):
        """ Import note

            Parameters:
                dict_entry: Dicitonary entry containing predetermined fields
                    minimum required is the native langue of the word

        """
        self.fr = dict_entry.get('fr')
        self.en = dict_entry.get('en')
        self.freq = []
        self.aud = None
        self.img = None

    def print_note(self):
        """ Print out available information about note

        """

        print("\t" + Fore.CYAN + self.fr + Style.RESET_ALL)

        print("\t\t en: \t\t" + self.en)
        print("\t\t img: \t" + str( self.img ))
        print("\t\t aud: \t" + str( self.aud ))

        print()

    def scrape_wordref(self, fields):
        """ Webscrape translation and grammatical information from Word Reference

            Parameters:
                  fields (string) [varg]: which fields to fill in on the AnkiNote
                    translation
                    audio
                    image
        """
        # print('Querying Word Reference...')

        url = 'http://wordreference.com/fren/' + self.fr

        res = requests.get(url)
        res.raise_for_status()  # Did anything download?

        # TODO: Check - Is this a valid page (i.e. am I on 404 page)?

        #Locate urls
        #soup = bs4.BeautifulSoup(res.text, "lxml") #lxml is just the suggested parser
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        if 'audio' in fields:
            elementType = 'source'
            linkElems = soup.select(elementType)
            soup.find()

            if not linkElems:
                logging.error('Could not find audio link: ' + self.fr)
                return

            else:
                # print('Searching,audiopath,imagepath for element type: ' + elementType )
                # print('Number of hits: ' + str(len(linkElems)))

                if linkElems == []:
                    print('Could not find audio link: ' + self.fr )

                else:
                    audioUrl = 'http://www.wordreference.com' + linkElems[
                        0].get('src')
                    # print('Downloading audio %s...' % (audioUrl))
                    res = requests.get(audioUrl)
                    res.raise_for_status()

                    # Save the image to ./audio.

                    audioPath = 'audio/' + self.fr + '.mp3'
                    audioFile = open(os.path.join(audioPath), 'wb')

                    for chunk in res.iter_content(100000):
                        audioFile.write(chunk)
                    audioFile.close()

                    print('\t\tSaved audio to: ' + audioPath)
                    self.aud = self.fr + '.mp3'

                    # TODO: Can I just return here?

        if 'translation' in fields:
            # grab translation
            """
            <td class="ToWrd">car <em class="tooltip POS2">n<span><i>noun</i>: Refers to person, place, thing, quality, etc.</span></em></td>
            """

            thisString = soup.find_all('td', {'class': 'ToWrd'})[1]
            logging.debug(f"Working with: {thisString} ")
            thatString = re.search('ToWrd\W*([a-zA-Z]*)\W',
                                       str(thisString))
            logging.debug(f"Result from regex: {thatString.group(1)} ")

            print('\t\tTranslation: ' + thatString.group(1))


    def ripImage(self, thisword):

        unicodeString = unidecode.unidecode(
            thisword
        )  # google-images-download throws an error for anything with an accent

        response = google_images_download.googleimagesdownload(
        )  #class instantiation

        arguments = {
            "keywords": unicodeString,
            "limit": 1,
            "print_urls": True,
            "no_numbering": True,
            "prefix": thisword,
            "image_directory": "images",
            "size": ">800*600",
            "format": "jpg",
            "silent_mode": False,
            #"no_directoy":True,
            "print_urls": True
        }  #creating list of arguments

        pathDict = response.download(
            arguments)  # passing the arguments to the function

        indTup = 0
        indDict = 1
        indList = 0
        # TODO make this more explicit
        absPath = pathDict[indTup].popitem()[indDict][
            indList]  # Path stored as Tuple[Dictionary[List[String]]]

        return (absPath)
