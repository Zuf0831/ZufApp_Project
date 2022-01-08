import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas.io.json import json_normalize
from streamlit.script_runner import StopException, RerunException
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from PIL import Image


#create empty figure and we will creating data into it
fig = go.Figure()

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



st.sidebar.header('Features')