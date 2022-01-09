import streamlit as st 
import pandas as pd 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try


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
            # TEST 1
        if kec2 == 'Pilih Kecamatan' :
            # TEST 2 
        elif kec2 != kec and kec2 != 'Pilih Kecamatan' :
            #TEst 3
    
        
            

        