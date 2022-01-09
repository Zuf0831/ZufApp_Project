import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
x = requests.get(url)
d = json_normalize(x.json()['vaksinasi']['penambahan'])

def vak1() :
    for item in d['jumlah_vaksinasi_1']:
        return item
