import streamlit as st 
from Provinsi.CovidCity import *
from Kecamatan.CovidKecamatan import *
from Vaccine.CovidVaccine import *

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
st.write("""* **Risk Level : ** [Here] (https://covid19.go.id/peta-risiko)""")

st.sidebar.header('Covid Case in Indonesia')
type = st.sidebar.selectbox('Choose',('Default','Provinsi','Vaksinasi','Kecamatan'))

if type == 'Provinsi' :
    City()
elif type == 'Kecamatan' :
    Kecamatan()
elif type == 'Vaksinasi' :
    Vaksin()

if st.sidebar.button('Refresh Data'):
        raise Refresh(Try(None))      
st.sidebar.subheader("""Created by Zuf : [Git Hub Repo](https://github.com/Zuf0831/ZufApp_Project.git)""")
st.sidebar.image('kid.jpg', width = 300)
