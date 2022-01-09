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
        st.write('TEST')
        
           

        