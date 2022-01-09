import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/kecamatan_rawan.json'
x = requests.get(url)
d = x.json()

def kate_data(input):
    for item in d:
        kec = item['title']
        kate = item['kategori']
        if kec == input :
            return kate