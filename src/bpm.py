import requests
import os

from dotenv import load_dotenv

load_dotenv()

HEARTURI = ""
O2URI=""
TOKEN = ""
HEARTOUTFILE = ""
O2OUTFILE=""
def getBpm():
    hassheaders = {'Authorization': 'Bearer {}'.format(TOKEN)}
    heartRequest = requests.get(url=HEARTURI, headers=hassheaders)
    heartJson = heartrequest.json()
    o2Request = requests.get(url=O2URI, headers=hassheaders)
    o2Json = o2Request.json()
    bpm = heartJson["state"]
    o2 = o2Json["state"]
    try:
        os.remove(HEARTOUTFILE)
        os.remove(O2OUTFILE)
    except OSError:
        pass
    with open(HEARTOUTFILE, 'w') as f:
        f.write(bpm)
    with open(O2OUTFILE, "w") as f:
        f.write(o2)