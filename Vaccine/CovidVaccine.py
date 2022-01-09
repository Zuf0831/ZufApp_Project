import streamlit as st 
import pandas as pd 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from PIL import Image
from Vak1 import *
from totVak1 import *


def Vaksin(): 
    #Create sidebar for search feature
    st.sidebar.subheader('Type')
    type = st.sidebar.selectbox('Features',('Default','Pemeriksaan','Vaksinasi'))
    
    

    #Control the input
    if type == 'Vaksinasi' :
        url = 'https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json'
        x = requests.get(url)
        d = json_normalize(x.json()['vaksinasi'])
        jenis_vak = st.sidebar.selectbox('Jenis Vaksin',('Default','Vaksin 1','Vaksin 2'))
        if jenis_vak == 'Vaksin 1' :
            vaksin1 = vak1()
            total_vak1 = tot_vak1()
                
            #Display Vaccine Data 1
            st.write("""# Vaksin 1""")
            st.write("""* **Penambahan : **"""+str(vaksin1))
            st.write("""* **Total      : **"""+str(total_vak1))
            
        # elif jenis_vak == 'Vaksin 2' :
        #     data2 = d['penambahan']
        #     total_data2 = d['total']
        #     #Get data for Penambahan Vaksin 1 
        #     for item in data2['jumlah_vaksinasi_2'] :
        #         vak2 = item
        #     #Get total data for vaksin
        #     for item in total_data2['jumlah_vaksinasi_2'] :
        #         total_vak2 = item
            
        #     #Display Vaccine Data 2
        #     st.write("""# Vaksin 2""")
        #     st.write("""* **Penambahan : **"""+str(vak2))
        #     st.write("""* **Total      : **"""+str(total_vak2))
    
    elif type == "Pemeriksaan"  :
        st.write('TEST')
        
        
    #Rerun Data or Source Code.
    if st.sidebar.button('Refresh Data'):
        raise Refresh(Try(None))      
    st.sidebar.subheader("""Created by Zuf : [Git Hub Repo](https://github.com/Zuf0831/ZufApp_Project.git)""")
    st.sidebar.image('kid.jpg', width = 300)
        
            

        