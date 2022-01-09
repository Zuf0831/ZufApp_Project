import streamlit as st 
import pandas as pd 
import requests
from pandas import json_normalize
from RiskCity.kategori import *
from RiskCity.prov import *
from RiskCity.city_code import *

def City(): 
    #Setting URL for the app and read list records from Data
    url = 'https://data.covid19.go.id/public/api/skor.json'
    x = requests.get(url)
    List_Data = json_normalize(x.json(),['data'])

    #Using DataFrame to filter some records
    top_row = pd.DataFrame({'kota':['Pilih Kota'], 'prov':['Empty'], 'hasil':['Empty'], 'kode_kota':['Empty']})

    #Mixing Dafaframe and reset the index or values
    df = pd.concat([top_row, List_Data]).reset_index(drop=True)

    #Create sidebar for search feature
    st.sidebar.subheader('Search by City')
    kota = st.sidebar.selectbox('City',df.kota)
    kota2 = st.sidebar.selectbox('Compare with another City',df.kota)


    if kota != 'Pilih Kota' :
        date_url = 'https://data.covid19.go.id/public/api/skor.json'
        q = requests.get(date_url)
        date = json_normalize(q.json())
        for key in date['tanggal']:
            time = key
        kategori =  city_kate(kota)
        kode_kota = city_code(kota)
        prov_kota = city_prov(kota)
        if kota2 == 'Pilih Kota' :
            st.write("""# Covid Cases """)
            st.write("""### Update : """+time)
            st.write("""* **Kota     : ** """+str(kota))
            st.write("""* **Provinsi    : ** """+str(prov_kota))
            st.write("""* **Kode Kota : ** """+str(kode_kota))
            st.write("""* **Kategori   : ** """+str(kategori))
                
        elif kota2 != kota and kota2 != 'Pilih Kota' :
            kategori2 =  city_kate(kota2)
            kode_kota2 = city_code(kota2)
            prov_kota2 = city_prov(kota2)
            st.write("""# Covid Cases 1""")
            st.write("""### Update : """+time)
            st.write("""* **Kota     : ** """+str(kota))
            st.write("""* **Provinsi    : ** """+str(prov_kota))
            st.write("""* **Kode Kota : ** """+str(kode_kota))
            st.write("""* **Kategori   : ** """+str(kategori))
            st.write("""---------------------------------""")
            st.write("""# Covid Cases 2""")
            st.write("""### Update : """+time)
            st.write("""* **Kota     : ** """+str(kota2))
            st.write("""* **Provinsi    : ** """+str(prov_kota2))
            st.write("""* **Kode Kota : ** """+str(kode_kota2))
            st.write("""* **Kategori   : ** """+str(kategori2))
            
    
        
            

        