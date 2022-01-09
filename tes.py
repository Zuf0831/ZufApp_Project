import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/kecamatan_rawan.json'
# url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
# cd = pd.read_json(d).head()
# z = d['jumlah_kasus']
# print(z)
d = x.json()

to_find = input('Cari Kecamatan : ')
def search(data) :
    for item in d:
        x = item['title']
        z = item['kategori']
        if x == data :
            return z
                           
print("Hasil : ",search(to_find))