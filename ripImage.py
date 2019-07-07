#! python3
# ripImage.py - Searches for native pronunciation of French audio on Forvo.com and saves files to computer
# documentation at https://pypi.org/project/google-images-download/
from google_images_download import google_images_download
import unidecode


def ripImage(thisword):

    unicodeString = unidecode.unidecode(thisword)  # google-images-download throws an error for anything with and accent

    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords":unicodeString,
                 "limit":1,
                 "print_urls":True,
                 "no_numbering":True,
                 "prefix":thisword,
                 "image_directory":"images",
                 "size":">800*600",
                 "format":"jpg",
                 "silent_mode":True,
                 "no_directoy":True}   #creating list of arguments

    pathDict = response.download(arguments)   # passing the arguments to the function

    indTup = 0; indDict = 1; indList = 0; # TODO make this more explicit
    absPath = pathDict[indTup].popitem()[indDict][indList]     # Path stored as Tuple[Dictionary[List[String]]]

    return(absPath)

