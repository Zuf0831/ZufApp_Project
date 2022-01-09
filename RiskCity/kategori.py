import requests
from pandas import json_normalize

url = 'https://data.covid19.go.id/public/api/skor.json'
x = requests.get(url)
d = json_normalize(x.json())

def city_kate(input) :
    for item in d['data']:
        for i in range(len(item)) :
            city = item[i]['kota']
            kategori = item[i]['hasil']
            if city == input :
                return kategori