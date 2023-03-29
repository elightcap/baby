import requests
import os

from dotenv import load_dotenv

load_dotenv()

HEARTURI = ""
O2URI=""
TOKEN = ""
HEARTOUTFILE = "heart.txt"
O2OUTFILE="o2.txt"
REL_HEART_PATH = "/usr/src/app/src/files/{}".format(HEARTOUTFILE)
REL_O2_PATH = "/usr/src/app/src/files/{}".format(O2OUTFILE)
def getBpm():
    hassheaders = {'Authorization': 'Bearer {}'.format(TOKEN)}
    heartRequest = requests.get(url=HEARTURI, headers=hassheaders)
    heartJson = heartRequest.json()
    o2Request = requests.get(url=O2URI, headers=hassheaders)
    o2Json = o2Request.json()
    bpm = heartJson["state"]
    o2 = o2Json["state"]
    try:
        os.remove(REL_HEART_PATH)
        os.remove(REL_O2_PATH)
    except OSError:
        pass
    with open(REL_HEART_PATH, 'w') as f:
        f.write(bpm)
    with open(REL_O2_PATH, "w") as f:
        f.write(o2)