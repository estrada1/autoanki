#!/usr/bin/python3
""" Test 1 to correctly import genanki, write a deck, and read it in Anki

"""

import genanki

my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')
my_deck.media_files = ['audio/seawave.mp3', 'sunset.jpg']

# Need to copy into directory: /home/estrada/.local/share/Anki2/User 1/collection.media

# You need to pass a model_id so that Anki can keep track of your model. It's important that you use a unique model_id for each Model you define. Use random.randrange(1 << 30, 1 << 31) to generate a suitable model_id, and hardcode it into your Model definition.

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'ImageMedia'},
    {'name': 'AudioMedia'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{ImageMedia}}<br>{{AudioMedia}}',
    },
  ],
  css=[
         {'font-family': 'arial'},
         {'font-size': '20px'},
         {'text-align': 'center'},
         {'color': 'black'},
         {'background-color': 'white'},
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires', '<img src="sunset.jpg">', '[sound:seawave.mp3]'])

my_note2 = genanki.Note(
  model=my_model,
  fields=['Capital of USA', 'Washington DC', '<img src="sunset.jpg">', '[sound:seawave.mp3]'])


print("Hello world ")

my_deck.add_note(my_note)
my_deck.add_note(my_note2)

genanki.Package(my_deck).write_to_file('testing_deck.apkg')
