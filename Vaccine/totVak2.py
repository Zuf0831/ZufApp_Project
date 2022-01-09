import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
x = requests.get(url)
d = json_normalize(x.json()['vaksinasi']['total'])

def tot_vak2() :
    for item in d['jumlah_vaksinasi_2']:
        return item
