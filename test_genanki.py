#!/usr/bin/python3
""" Test 1 to correctly import genanki, write a deck, and read it in Anki

"""

import genanki

my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')
my_deck.media_files = ['audio/seawave.mp3', 'sunset.jpg']
# Need to copy into directory: /home/estrada/.local/share/Anki2/User 1/collection.media


my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia'},
    {'name': 'MyMedia2'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{MyMedia}}{{MyMedia2}}',
    },
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires', '<img src="sunset.jpg">', '[sound:seawave.mp3]'])
# [sound:seawave.mp3]

print("Hello world ")


my_deck.add_note(my_note)
genanki.Package(my_deck).write_to_file('output.apkg')
# <img src="image.jpg">
