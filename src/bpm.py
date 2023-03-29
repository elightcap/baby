import requests
import os

from dotenv import load_dotenv

load_dotenv()

URI = ""
TOKEN = ""
OUTFILE = ""
def getBpm():
    hassheaders = {'Authorization': 'Bearer {}'.format(TOKEN)}
    request = requests.get(url=URI, headers=hassheaders)
    mJson = request.json()
    print(mJson)
    bpm = mJson["state"]
    try:
        os.remove(OUTFILE)
    except OSError:
        pass
    with open(OUTFILE, 'w') as f:
        f.write(bpm)