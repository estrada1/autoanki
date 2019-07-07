"""@package docstring

Some methods to handle words already saved and stored
"""


import os


def files(path):
    file_set = set()
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_set.add(file)
    return file_set


def redundantWord(word,set2check):
    # Checks to see if word is within the provided set
    # returns true/false
    for file in set2check:
        # print(file)
        if file.find(word) > 0:  # .find() method returns -1 if not found, or ind of entry if found
            return file
    return []


def redundantSet(wordSet,set2check):
    # Checks for redundant words within a set of filenames
    # Returns set of words within the set
    redundant_words = set()
    for word in wordSet:
        for file in set2check:
            # print(file)
            if file.find(word) > 0:  # .find() method returns -1 if not found, or ind of entry if found
                redundant_words.add(word)
    return redundant_words


# theseFiles = files("downloads/images")
# wordSet={"serrer", "courir", "listen"}
# print(type(wordSet))
# print(redundantSet(wordSet, theseFiles))
