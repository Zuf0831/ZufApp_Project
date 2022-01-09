import streamlit as st 
import pandas as pd 
import requests
from pandas import json_normalize
from Provinsi.kasus import *
from Provinsi.death import *
from Provinsi.sembuh import *
from Provinsi.rawat import *

def Provence(): 
    #Setting URL for the app and read list records from Data
    url = 'https://data.covid19.go.id/public/api/prov.json'
    x = requests.get(url)
    List_Data = json_normalize(x.json(),['list_data'])

    #Using DataFrame to filter some records
    top_row = pd.DataFrame({'key':['Pilih Provinsi'], 'jumlah_kasus':['Empty'], 'jumlah_sembuh':['Empty'], 'jumlah_meninggal:':['Empty'], 'jumlah_dirawat' : ['Empty']})

    #Mixing Dafaframe and reset the index or values
    df = pd.concat([top_row, List_Data]).reset_index(drop=True)

    #Create sidebar for search feature
    st.sidebar.subheader('Search by Provence')
    prov = st.sidebar.selectbox('City',df.key)
    prov2 = st.sidebar.selectbox('Compare with another City',df.key)


    if prov != 'Pilih Provinsi' :
        date_url = 'https://data.covid19.go.id/public/api/prov.json'
        q = requests.get(date_url)
        date = json_normalize(q.json())
        for key in date['last_date']:
            time = key
        kasus =  case(prov)
        sembuh = alive(prov)
        meninggal = death(prov)
        rawat = hospital(prov)
        if prov2 == 'Pilih Provinsi' :
            st.write("""# Covid Cases at """+prov)
            st.write("""### Update : """+time)
            st.write("""* **Kasus     : ** """+str(kasus))
            st.write("""* **Sembuh    : ** """+str(sembuh))
            st.write("""* **Meninggal : ** """+str(meninggal))
            st.write("""* **DiRawat   : ** """+str(rawat))
                
        elif prov2 != prov and prov2 != 'Pilih Provinsi' :
            kasus2 =  case(prov2)
            sembuh2 = alive(prov2)
            meninggal2 = death(prov2)
            rawat2 = hospital(prov2)
            st.write("""# Covid Cases at """+prov)
            st.write("""### Update : """+time)
            st.write("""* **Kasus     : ** """+str(kasus))
            st.write("""* **Sembuh    : ** """+str(sembuh))
            st.write("""* **Meninggal : ** """+str(meninggal))
            st.write("""* **DiRawat   : ** """+str(rawat))
            st.write("""--------------------------------------------""")
            st.write("""# Covid Cases at """+prov2)
            st.write("""### Update : """+time)
            st.write("""* **Kasus     : ** """+str(kasus2))
            st.write("""* **Sembuh    : ** """+str(sembuh2))
            st.write("""* **Meninggal : ** """+str(meninggal2))
            st.write("""* **DiRawat   : ** """+str(rawat2))
            
    
        
            

        