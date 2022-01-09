import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
x = requests.get(url)
d = json_normalize(x.json()['pemeriksaan']['penambahan'])

def people() :
    for item in d['jumlah_orang_pcr_tcm']:
        return item
