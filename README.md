# Covid Status App
This app created to get some information about current status of covid cases and vaccination rates in Indonesia
- Data Source API : [Here](https://documenter.getpostman.com/view/16605343/Tzm6nwoS)
- Indonesian Covid Web Official : [Here](https://covid19.go.id/)

## Tech
- Language : Python
- Modules : streamlit, pandas, requests

## Modules Installation
- Streamlit (Remember to use Python Version 64-bit)
```bash
  pip install streamlit
  > streamlit hello  ### To check streamlit on cmd
  > streamlit run [app_name].py  ### Run python file
```
- pandas
```bash
  pip install pandas
```
- requests
```bash
  pip install requests
```

# Modules Explanation

## Streamlit
- On this App Project i'm using Streamlit as a Framework to show my Python code.
- Streamlit can also be installed in a virtual environment on Windows, Mac, and Linux.
Example
```javascript
import streamlit as st

st.title('Hello')
```

## Requests
- The requests module allows us to send HTTP requests using python and get some data from url
Example
```javascript
import requests

url = 'https://data.covid19.go.id/public/api/kecamatan_rawan.json'
x = request.get(url)
```

## Pandas
- i'm using this module to read json file 
Example
```javascript
import requests
from pandas import json_normalize

url = 'https://data.covid19.go.id/public/api/skor.json'
x = requests.get(url)
d = json_normalize(x.json())
```

## Covid Status App Features
- Check Covid Cases by Provence
- Check Vaccination and Testing
- Check City Risk Score
- Check Districts Risk Score

## Covid App Demo 
Example
![](Covid App.gif)
