#! python3
"""@package docstring
ripWordRef.py
Searches for native pronunciation of French audio on wordreference.com and saves files to computer

More details.
"""

import requests, sys, webbrowser, bs4, os

def ripWordRef(wordquery):
	# print('Querying Word Reference...')

	# url = 'https://forvo.com/word/' + word + '/#fr'
	url = 'http://wordreference.com/fren/' + wordquery

	res = requests.get(url)
	res.raise_for_status()	# Did anything download?

	# TODO: Check - Is this a valid page (i.e. am I on 404 page)?

	#Locate urls
	#soup = bs4.BeautifulSoup(res.text, "lxml") #lxml is just the suggested parser
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	# elementType = 'audio'
	elementType = 'source'
	linkElems = soup.select(elementType)

	if not linkElems:
		print('Could not find audio link.')

		return

	# TODO: Can I just return here?
	else:
		# print('Searching for element type: ' + elementType )
		# print('Number of hits: ' + str(len(linkElems)))

		if linkElems ==[]:
			print('Could not find audio link')
		else:
			audioUrl = 'http://www.wordreference.com' + linkElems[0].get('src')
			# print('Downloading audio %s...' % (audioUrl))
			res = requests.get(audioUrl)
			res.raise_for_status()

			# Save the image to ./audio.

			# print(os.path.basename(audioUrl))
			audioPath = 'downloads/audio/' + wordquery + '.mp3'
			audioFile = open(os.path.join(audioPath), 'wb')

			for chunk in res.iter_content(100000):
				audioFile.write(chunk)
			audioFile.close()

	return audioPath

