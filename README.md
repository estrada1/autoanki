# autoAnki
Some simple python scripts to assist creating Anki flashcards with images and audio of pronunciation by native speakers. 

### Libraries
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [google-images-download](https://google-images-download.readthedocs.io/en/latest/index.html)
- requests

### Getting Started 


If this is your first time running the code, install the required python packages 

```
pip3 install -r requirements
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

Using debugger [pdb](https://docs.python.org/3/library/pdb.html) to diagnose problems. Common use is to use `import pdb; pdb.set_trace()` command. 