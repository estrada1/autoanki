# autoAnki
Simple python scripts to assist creating [Anki](https://apps.ankiweb.net/) flashcards with images and audio of pronunciation by native speakers. 

### Libraries
If this is your first time running the code, install the required python packages

```bash
pip3 install -r requirements.txt
```

- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [google-images-download](https://google-images-download.readthedocs.io/en/latest/index.html)
- [requests](https://requests.readthedocs.io/en/master/)
- + others as I tinker

### Getting Started

Run the main script

```bash
python3 main.py
```

### Notes

- Apprently google images changed its API, so others are having the same [issue](https://github.com/hardikvasa/google-images-download/issues/302) downloading images as well, this part doesn't work at the moment.  
- Google offers a [translation API](https://cloud.google.com/translate/docs/basic/setup-basic) which would be a pertinent alternative.
- Another nice functionality is [Quizlet's](https://quizlet.com/) auto translation and pronunciation. 
- [genaki](https://github.com/kerrickstaley/genanki) package.
- Third party [word reference api](https://github.com/fega/wordreference-api) scripted in js.
