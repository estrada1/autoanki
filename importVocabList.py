"""@package docstring

Methods to import vocab list from .txt file.
"""
import csv
from collections import deque

def import_list(file_in):
    # use csv library to read in tsv file and return a deck of "mNotes", or Matt Notes

    verbFields = ['fr', 'eng', 'aud', 'misc']
    dNotes = deque()

    # Label columns that are being read in
    with open(file_in, newline='') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t', fieldnames=verbFields)
        for row in reader:
            # print(row)
            thisNote = mNote(row['fr'],row['eng'],row['aud'],[])
            dNotes.append(thisNote)

    return dNotes

# Matt note as he figures out how to interface with Anki
class mNote:
    """Store info (e.g. audio path, english translation) for an Anki Note."""
    def __init__(self,french,english,audiopath,imagepath):
        self.fr = french
        self.eng = english
        self.aud = audiopath
        self.img = imagepath

    def logError(self, txtfile, errormsg):
        """Log error in attempted command in txtfile."""

        with open(txtfile, 'a', newline='') as tsvfile:  # a stands for append

            writer = csv.writer(tsvfile, delimiter='\t')
            logRow = [[self.fr],errormsg]
            writer.writerow(logRow)

        tsvfile.close()
