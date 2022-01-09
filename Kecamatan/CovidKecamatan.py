import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas import json_normalize
from streamlit.script_runner import RerunException as Refresh
from streamlit.script_request_queue import RerunData as Try
from PIL import Image

def Kecamatan(): 
    #Setting URL for the app and read list records from Data
    url = 'https://data.covid19.go.id/public/api/prov.json'
    x = requests.get(url)
    List_Data = json_normalize(x.json(),['list_data'])

    st.write('ZONK')
            

        