import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from PIL import Image
from kasus import *
from death import *
from sembuh import *
from rawat import *

def Vaksin(): 
    #Setting URL for the app and read list records from Data
    url = 'https://data.covid19.go.id/public/api/prov.json'
    x = requests.get(url)
    List_Data = json_normalize(x.json(),['list_data'])

    #Using DataFrame to filter some records
    top_row = pd.DataFrame({'key':['Pilih Provinsi'], 'jumlah_kasus':['Empty'], 'jumlah_sembuh':['Empty'], 'jumlah_meninggal:':['Empty'], 'jumlah_dirawat' : ['Empty']})

    #Mixing Dafaframe and reset the index or values
    df = pd.concat([top_row, List_Data]).reset_index(drop=True)

    #Create sidebar for search feature
    st.sidebar.subheader('Type')
    type = st.sidebar.selectbox('Features',('Default','Pemeriksaan','Vaksinasi'))
    
    #Rerun Data or Source Code.
    if st.sidebar.button('Refresh Data'):
        raise Refresh(Try(None))

    #Call some data from data list


    if type != 'Vaksinasi' :
        url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
        x = requests.get(url)
        d = json_normalize(x.json()['vaksinasi'])
        jenis_vak = st.sidebar.selectbox('Jenis Vaksin',('Default','Vaksin 1','Vaksin 2'))
        if jenis_vak == 'Vaksin 1' :
            data1 = d['penambahan']
            total_data1 = d['total']
            #Get data for Penambahan Vaksin 1 
            for item in data1['jumlah_vaksinasi_1'] :
                vak1 = item
            #Get total data for vaksin
            for item in total_data1['jumlah_vaksinasi_1'] :
                total_vak1 = item
                
            #Display Vaccine Data 1
            st.write("""# Vaksin 1""")
            st.write("""* **Penambahan : **"""+str(vak1))
            st.write("""* **Total      : **"""+str(total_vak1))
            
        elif jenis_vak == 'Vaksin 2' :
            data2 = d['penambahan']
            total_data2 = d['total']
            #Get data for Penambahan Vaksin 1 
            for item in data2['jumlah_vaksinasi_2'] :
                vak2 = item
            #Get total data for vaksin
            for item in total_data2['jumlah_vaksinasi_2'] :
                total_vak2 = item
            
            #Display Vaccine Data 2
            st.write("""# Vaksin 2""")
            st.write("""* **Penambahan : **"""+str(vak2))
            st.write("""* **Total      : **"""+str(total_vak2))
        
            
    st.sidebar.subheader("""Created by Zuf : [Git Hub Repo](https://github.com/Zuf0831/ZufApp_Project.git)""")
    st.sidebar.image('kid.jpg', width = 300)
        
            

        