from typing import Optional

from fastapi import FastAPI

from datetime import date
from datetime import timedelta


import requests

import json

from pprint import pprint
url = "https://app.officevibe.com/api/v2/engagement"

dates = []
t = date.today()
for i in range(0,7):
	dates.append((t-timedelta(days=i)).strftime('%Y-%m-%d'))

body = {
	"dates": dates
}
headers = {
    "Authorization": "Bearer 978d6683fb74430caac437ddb9dfd7322c0c2807f91a4bd89b255d9a8a74203ccf076ede9fde4fa286f0c81ab24987d1",
    "Content-Type": "application/json"
}

valuearr = []

r = requests.post(url, data=json.dumps(body), headers=headers)
reports = r.json()["data"]["weeklyReports"]



for i in reports:
	for j in i["metricsValues"]:
		j["date"]=i["date"]
		valuearr.append(j)

pprint(valuearr)

app = FastAPI()

'''
@app.post("/")
def read_root():
    return {"Hello": "World"}
'''

