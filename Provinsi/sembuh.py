import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
d = json_normalize(x.json())

def alive(input):
    for item in d['list_data'] :
        for s in range(len(item)):
            city = item[s]["key"]
            sembuh = item[s]["jumlah_sembuh"]
            if input == city :
                return sembuh