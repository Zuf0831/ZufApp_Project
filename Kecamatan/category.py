import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/kecamatan_rawan.json'
x = requests.get(url)
d = json_normalize(x.json())

def kate(input):
    for item in d :
        for s in range(len(item)):
            city = item[s]["title"]
            kategori = item[s]["kategori"]
            if input == city :
                return kategori