"""@package docstring
autoAnki library to help make language flashcards in Anki

Author: Matt Estrada
"""

from importVocabList import import_list
from ripWordRef import ripWordRef
import codecs
from ripImage import ripImage
from redundancy import files, redundantWord
import os
import datetime
import csv




######################################
# Import and save-to files

# import list from .txt file
# file_in = 'data/FrenchVerbsNotes.txt'
file_in = 'data/test_input.txt'
# file_in = 'data/debugCases.txt'
file_out = 'data/test_output.txt'

######################################
# Language settings

lang = 'fr'
ankiPrefix d= 'autoAnki_'+lang+' '  # tag all media files in case I have to delete them later
mediaDir = 'downloads/images/'
audDir = 'downloads/audio/'
# TODO: allow program to pick up after an error, perhaps scan through directory?
# TODO: count number of things here
# TODO: add capability for priority/usage frequency
# TODO: graphical interface to help pick photos
# TODO: male/female? stick the le/la in front of there to help memorize

######################################

thisDict = import_list(file_in)  # returns deque of "mNotes" class

# find images and fill in url
cwd = os.getcwd()
leading = cwd + "/" + mediaDir
imgFiles = files(mediaDir)


with open(file_out, 'a', newline='') as tsvfile:  # a stands for append

    for thisNote in thisDict:

        thisFr = thisNote.fr

        # if not redundantWord(thisFr, imgFiles):

        # IMAGE
        imgAbsPath = ripImage(thisFr)

        # If unable to find picture
        if not imgAbsPath:
            print('Error: ' + thisFr + ' did not return an image')
            thisNote.logError('data/errors.txt','Could not find image', datetime.datetime.now())
            continue        # TODO: Possible to handle with with exception?

        imgPathSplit = imgAbsPath.rsplit(leading)
        imgAbsPath2 = leading + ankiPrefix + imgPathSplit[1]
        imgName = ankiPrefix + imgPathSplit[1] # trying this out
        os.rename(imgAbsPath, imgAbsPath2)
        thisNote.img = imgName



        # else:
        #     print(thisFr + " already has an image")

        # AUDIO
        audPath = ripWordRef(thisFr)

        if not audPath:
            print('Error: ' + thisFr + ' did not return an audio path')
            thisNote.logError('data/errors.txt', 'Could not find audio', datetime.datetime.now())
            continue  # TODO: Possible to handle with with exception?

        audPathSplit = audPath.rsplit(audDir)
        audName = ankiPrefix + audPathSplit[1]
        audPath2 = audDir + ankiPrefix + audPathSplit[1]
        os.rename(audPath, audPath2)

        # write new line
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow([thisNote.fr, thisNote.eng, thisNote.aud, thisNote.img])

tsvfile.close()

print("\n" "Output file written to ", file_out)
  # # os.rename("downloads/images/" + thisImgPath, "downloads2/" + thisImgPath)
    # row.img = thisAbsPath

