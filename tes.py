import pandas as pd
import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
x = requests.get(url)
d = json_normalize(x.json()['vaksinasi'])
# cd = pd.read_json(d).head()
# z = d['jumlah_kasus']
# print(z)

# to_find = input('Cari kasus by kota : ')

# def search_case(citu):
#     for item in d['list_data'] :
#         for s in range(len(item)):
#             city = item[s]["key"]
#             kasus = item[s]["jumlah_kasus"]
#             if citu == city :
#                 return kasus

# print(" Hasil : ", search_case(to_find))
for item in d :
    print(item)