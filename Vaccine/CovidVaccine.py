import streamlit as st 
import pandas as pd 
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from Vaccine.Vak1 import *
from Vaccine.totVak1 import *
from Vaccine.Vak2 import *
from Vaccine.totVak2 import *
from Vaccine.lastDate import *
from Vaccine.pcr_add import *
from Vaccine.pcr_people import *
from Vaccine.total_pcr_add import *
from Vaccine.total_pcr_people import *


def Vaksin(): 
    #Create sidebar for search feature
    st.sidebar.subheader('Data Type')
    type = st.sidebar.selectbox('Choose',('Default','Pemeriksaan','Sudah Vaksin'))
    
    

    #Control the input
    if type == 'Sudah Vaksin' :
        jenis_vak = st.sidebar.selectbox('Jenis Vaksin',('Default','Vaksin 1','Vaksin 2'))
        last_date = Date()
        if jenis_vak == 'Vaksin 1' :
            vaksin1 = vak1()
            total_vak1 = tot_vak1()
                
            #Display Vaccine Data 1
            st.write("""# Vaksin 1""")
            st.write(""" Update : """+last_date)
            st.write("""* **Penambahan : **"""+str(vaksin1)+""" Pasien""")
            st.write("""* **Total      : **"""+str(total_vak1)+""" Pasien""")
        
        elif jenis_vak == 'Vaksin 2' :
            vaksin2 = vak2()
            total_vak2 = tot_vak2()
                
            #Display Vaccine Data 2
            st.write("""# Vaksin 2""")
            st.write(""" Update : """+last_date)
            st.write("""* **Penambahan : **"""+str(vaksin2)+""" Pasien""")
            st.write("""* **Total      : **"""+str(total_vak2)+""" Pasien""")
        
    
    elif type == "Pemeriksaan"  :
        jenis = st.sidebar.selectbox('Jenis Spesimen',('Default','PCR','Antigen'))
        if jenis == 'PCR' :
            data_add = add()
            data_people = people()
            total_data_add = tot_add()
            total_data_people = tot_people()
            st.write("""# Spesimen PCR""")
            # st.write(""" Update : """+last_date)
            st.write("""* **Penambahan Jumlah Spesimen : **"""+str(data_add))
            st.write("""* **Penambahan Penerima PCR    : **"""+str(data_people)+""" Pasien""")
            st.write("""* **Total Jumlah Spesimen : **"""+str(total_data_add))
            st.write("""* **Total Penerima PCR    : **"""+str(total_data_people)+""" Pasien""")
        elif jenis == 'Antigen' :
            st.write('TEST')
        