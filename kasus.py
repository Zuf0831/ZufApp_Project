import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
d = json_normalize(x.json())

def case(input):
    for item in d['list_data'] :
        for s in range(len(item)):
            city = item[s]["key"]
            kasus = item[s]["jumlah_kasus"]
            if input == city :
                return kasus