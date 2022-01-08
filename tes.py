import pandas as pd
import requests
from pandas.io.json import json_normalize


url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
d = json_normalize(x.json(),['list_data'])
# cd = pd.read_json(d).head()
z = d['jumlah_kasus']
print(z)
