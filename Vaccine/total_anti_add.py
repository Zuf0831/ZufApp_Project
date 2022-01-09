import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
x = requests.get(url)
d = json_normalize(x.json()['pemeriksaan']['total'])

def tot_add_2() :
    for item in d['jumlah_spesimen_antigen']:
        return item
