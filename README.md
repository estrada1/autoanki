# autoAnki
Some simple python scripts to assist creating Anki flashcards with images and audio of pronunciation by native speakers. 

### Libraries
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [google-images-download](https://google-images-download.readthedocs.io/en/latest/index.html)
- requests

### Getting Started

If this is your first time running the code, install the required python packages

```bash
pip3 install -r requirements.txt
```

Source the virtual environment

```bash
source venv/bin/activate
````

Run the main script

```bash
python3 main.py
```

### Notes

Apprently google changed its API, so other sare having the same [issue](https://github.com/hardikvasa/google-images-download/issues/302) downloading images as well. 

Google offers a [translation API](https://cloud.google.com/translate/docs/basic/setup-basic) which would be a pertinent alternative.

Another nice functionality is [Quizlet's](https://quizlet.com/) auto translation and pronunciation. 

[genaki](https://github.com/kerrickstaley/genanki) package.

Third party [word reference api](https://github.com/fega/wordreference-api) scripted in js.