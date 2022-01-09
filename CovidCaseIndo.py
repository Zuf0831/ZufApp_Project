import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from PIL import Image
from kasus import *
from death import *
from sembuh import *
from rawat import *


#create empty figure and we will creating data into it
graph = go.Figure()

#Make some style using st framework to display it in website
st.title('Covid 19 Tracking App ')
logo = Image.open('logo.png')
st.image(logo, width = 300)
st.markdown("""Coronavirus is officially a pandemic. Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.
                Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment. However, some will become seriously ill and require medical attention.
                This app created to show and check covid cases status in indonesia!
            """)
st.write("""* **Official Website : ** [covid19.go.id](https://covid19.go.id/)""")
st.write("""* **Data Source : ** [data.covid19.go.id](https://data.covid19.go.id/)""")
st.write("""* **Data Example API : ** [Covid19 API] (https://documenter.getpostman.com/view/16605343/Tzm6nwoS#d35f1c32-56d8-4af1-8d6e-ef3397653f99)""")

#Setting URL for the app and read list records from Data
url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
List_Data = json_normalize(x.json(),['list_data'])

#Using DataFrame to filter some records
top_row = pd.DataFrame({'key':['Pilih Provinsi'], 'jumlah_kasus':['Empty'], 'jumlah_sembuh':['Empty'], 'jumlah_meninggal:':['Empty'], 'jumlah_dirawat' : ['Empty']})

#Mixing Dafaframe and reset the index or values
df = pd.concat([top_row, List_Data]).reset_index(drop=True)

#Create sidebar for search feature
st.sidebar.header('Covid Case in Indonesia')
st.sidebar.subheader('Search by Provence')
city = st.sidebar.selectbox('City',df.key)
city2 = st.sidebar.selectbox('Compare with another City',df.key)

#Rerun Data or Source Code.
if st.sidebar.button('Refresh Data'):
    raise Refresh(Try(None))

#Call some data from data list


if city != 'Pilih Provinsi' :
    date_url = 'https://data.covid19.go.id/public/api/prov.json'
    q = requests.get(date_url)
    date = json_normalize(q.json())
    for key in date['last_date']:
        time = key
    kasus =  case(city)
    sembuh = alive(city)
    meninggal = death(city)
    rawat = hospital(city)
    if city2 == 'Pilih Provinsi' :
        st.write("""# Covid Cases at """+city+""" Pada """+time)
        st.write("""* **Kasus     : ** """+str(kasus))
        st.write("""* **Sembuh    : ** """+str(sembuh))
        st.write("""* **Meninggal : ** """+str(meninggal))
        st.write("""* **DiRawat   : ** """+str(rawat))
            
    elif city2 != city and city2 != 'Pilih Provinsi' :
        kasus2 =  case(city2)
        sembuh2 = alive(city2)
        meninggal2 = death(city2)
        rawat2 = hospital(city2)
        st.write("""# Covid Cases at """+city+""" Pada """+time)
        st.write("""* **Kasus     : ** """+str(kasus))
        st.write("""* **Sembuh    : ** """+str(sembuh))
        st.write("""* **Meninggal : ** """+str(meninggal))
        st.write("""* **DiRawat   : ** """+str(rawat))
        st.write("""# Covid Cases at """+city2+""" Pada """+time)
        st.write("""* **Kasus     : ** """+str(kasus2))
        st.write("""* **Sembuh    : ** """+str(sembuh2))
        st.write("""* **Meninggal : ** """+str(meninggal2))
        st.write("""* **DiRawat   : ** """+str(rawat2))
        
st.sidebar.subheader("""Created by Zuf : [Git Hub Repo](https://github.com/Zuf0831/ZufApp_Project.git)""")
st.sidebar.image('kid.jpg', width = 300)
        
            

        