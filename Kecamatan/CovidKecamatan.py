import streamlit as st 
import pandas as pd 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from Kecamatan.category import *

def Kecamatan(): 
    #Setting URL for the app and read list records from Data
    url = 'https://data.covid19.go.id/public/api/kecamatan_rawan.json'
    x = requests.get(url)
    List_Data = json_normalize(x.json())
    
    top_row = pd.DataFrame({'title':['Pilih Kecamatan'], 'kategori':['Empty']})

    df = pd.concat([top_row, List_Data]).reset_index(drop=True)
    
    st.sidebar.subheader('Search by Kecamatan')
    kec = st.sidebar.selectbox('Kecamatan',df.title)
    kec2 = st.sidebar.selectbox('Compare with another Kecamatan',df.title)
    
    if kec != 'Pilih Kecamatan' :
        kategori = kate_data(kec)
        if kec2 == 'Pilih Kecamatan' :
            st.write("""# Result """)
            st.write("""* **Kecamatan     : ** """+str(kec))
            st.write("""* **Kasus     : ** """+str(kategori))
        elif kec2 != kec and kec2 != 'Pilih Kecamatan' :
            kategori2 = kate_data(kec2)
            st.write("""# Result """)
            st.write("""* **Kecamatan     : ** """+str(kec))
            st.write("""* **Kasus     : ** """+str(kategori))
            st.write("""-------------------------""")
            st.write("""* **Kecamatan     : ** """+str(kec2))
            st.write("""* **Kasus     : ** """+str(kategori2))
    
        
            

        