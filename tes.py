import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
d = json_normalize(x.json())
# cd = pd.read_json(d).head()
# z = d['jumlah_kasus']
# print(z)

ids = []
to_find = input('Cari kasus by kota : ')

def search_case(citu):
    for item in d['list_data'] :
        for s in range(len(item)):
            city = item[s]["key"]
            kasus = item[s]["jumlah_kasus"]
            if citu == city :
                return kasus

print(" Hasil : ", search_case(to_find))

        
