import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

URI = os.getenv(HASS_URI)
TOKEN = os.getenv(HASS_TOKEN)
OUTFILE = os.getenv('outfile')
def getBpm():
    hassheaders = {'Authorization': 'BEARER {}'.format(TOKEN)}
    request = requests.get(url=URI, HEADERS=hassheaders)
    mJson = request.json
    bpm = mJson["state"]

    with open(OUTFILE, 'w') as f:
        f.write(bpm)