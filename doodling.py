import os
from importVocabList import import_list, mNote

import csv
from collections import deque


tuple1 = 1, 2, 'five'

a, b, c = tuple1

print(b)

a = "YesFitness"
b = a.rsplit("Yes")

print(b[1])

thisDir = os.getcwd()
print(thisDir)
# dirEntry = os.scandir(thisDir)
# print(type(dirEntry))
exPath = '/Users/Matteo/Documents/Coding/autoAnki/downloads/images/couter 1200px-Briquet_d%C3%A9tail_armure_Vienne.jpg'


# file_in = 'data/testListTiny.txt'

thisNote = mNote('frTest', 'engTest', 'audTest', 'imgTest')

# with open('data/test.txt', 'a', newline='') as tsvfile: # a stands for append
#     writer = csv.writer(tsvfile, delimiter='\t')
#     # print(thisNote.formatrow())
#     writer.writerow([thisNote.fr, thisNote.eng, thisNote.aud, thisNote.img])
# tsvfile.close()




now = datetime.datetime.now()
print(now)