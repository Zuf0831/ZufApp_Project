import requests
from pandas import json_normalize


url = 'https://data.covid19.go.id/public/api/skor.json'
# url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
# cd = pd.read_json(d).head()
# z = d['jumlah_kasus']
# print(z)
# d = x.json()
d = json_normalize(x.json())
# to_find = input('Cari Kota : ')
# def search(data) :
#     for item in d['data']:
#         for i in range(len(item)) :
#             city = item[i]['kota']
#             kategori = item[i]['hasil']
#             if city == data :
#                 return kategori
# # print(d)                        
# print("Hasil : ",search(to_find))
for item in d['tanggal'] :
    print(item)