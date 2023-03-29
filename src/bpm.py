import requests
import os

from dotenv import load_dotenv

load_dotenv()

URI = "https://arepo.castleanorak.co:8123/api/states/sensor.owlet_heart_rate"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0YzRlZDlhNDUyODA0ZmM0OTYwYzNiMTBhNWUwZDFkMSIsImlhdCI6MTY4MDA2MzEwOSwiZXhwIjoxOTk1NDIzMTA5fQ.q-u-41l_sN0MInZPWmPTP-ef8cg6DskTavog3RN3m9U"
OUTFILE = "tester.txt"
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