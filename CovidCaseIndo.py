import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas.io.json import json_normalize
from streamlit.script_runner import StopException, RerunException
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px


#create empty figure and we will creating data into it
fig = go.Figure()

#Make some style using st framework to display it in website
st.title('Covid 19 App')

st.markdown("""This app created to show covid cases status in indonesia 
            * **Python libraries :** base64, pandas, streamlit
            * **Data Source :** [data.covid19.go.id](https://data.covid19.go.id/)
            * **Official Website :** [covid19.go.id](https://covid19.go.id/)""")

st.sidebar.header('Features')