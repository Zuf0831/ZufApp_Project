import streamlit as st 
import pandas as pd 
import numpy as np 
import requests
from pandas import json_normalize
from streamlit.script_runner import StopException, RerunException
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from PIL import Image


#create empty figure and we will creating data into it
graph = go.Figure()

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

#Setting URL for the app and read list records from Data
url = 'https://data.covid19.go.id/public/api/prov.json'
x = requests.get(url)
List_Data = json_normalize(x.json(),['list_data'])

#Using DataFrame to filter some records
top_row = pd.DataFrame({'key':['Pilih Provinsi'], 'jumlah_kasus':['Empty'], 'jumlah_sembuh':['Empty'], 'jumlah_meninggal:':['Empty'], 'jumlah_dirawat' : ['Empty']})

#Mixing Dafaframe and reset the index or values
df = pd.concat([top_row, List_Data]).reset_index(drop=True)

#Create sidebar for search feature
st.sidebar.header('Search Section')
type = st.sidebar.selectbox('Case Type',('Meninggal','Sembuh','Rawat'))
st.sidebar.subheader('Search by Provence')
city = st.sidebar.selectbox('City',df.key)
city2 = st.sidebar.selectbox('Compare with another City',df.key)

if st.sidebar.button('Refresh Data'):
    raise RerunException(st.ScriptRequestQueue.RerunData(None))

#Call some data from data list


if city != 'Pilih Provinsi' :
    # date_url = 'https://data.covid19.go.id/public/api/prov.json'
    # q = requests.get(date_url)
    # date_data = json_normalize(q.json())
    # last_date = df.date_data[df['key']==city].to_string(index=False)[0]
    kasus =  List_Data[df['key']==city].to_string(index=False)[2]
    sembuh = List_Data[df['key']==city].to_string(index=False)[3]
    meninggal = List_Data[df['key']==city].to_string(index=False)[4]
    rawat = List_Data[df['key']==city].to_string(index=False)[5]
    if city2 == 'Pilih Provinsi' :
        st.write("""# Covid Cases at """+city+""" Pada """)
        st.write("""* **Kasus     : ** """+str(kasus))
        st.write("""* **Sembuh    : ** """+str(sembuh))
        st.write("""* **Meninggal : ** """+str(meninggal))
        st.write("""* **DiRawat   : ** """+str(rawat))
        # if type == 'Meninggal' :
        #     layout = go.Layout(
        #         title = city+'\ : '+str(kasus)+ ' Kasus',
        #         xaxis = dict(title = "Kasus"),
        #         yaxis = dict(title = "Meninggal"),
        #     )
        #     graph.update_layout(dict1 = layout, overwrite=True)
        #     graph.add_trace(go.Scatter(x=kasus, y=meninggal, mode='lines', name=city))
            
        #     st.plotly_chart(graph, use_container_width=True)
                
        # elif type == 'Sembuh' :
        #     layout = go.Layout(
        #         title = city+'\ : '+str(kasus)+ ' Kasus',
        #         xaxis = dict(title = "Kasus"),
        #         yaxis = dict(title = "Sembuh"),
        #     )
        #     graph.update_layout(dict1 = layout, overwrite=True)
        #     graph.add_trace(go.Scatter(x=kasus, y=sembuh, mode='lines', name=city))
            
        #     st.plotly_chart(graph, use_container_width=True)
        
        # elif type == 'Rawat' :
        #     layout = go.Layout(
        #         title = city+'\ : '+str(kasus)+ ' Kasus',
        #         xaxis = dict(title = "Kasus"),
        #         yaxis = dict(title = "Rawat"),
        #     )
        #     graph.update_layout(dict1 = layout, overwrite=True)
        #     graph.add_trace(go.Scatter(x=kasus, y=rawat, mode='lines', name=city))
            
        #     st.plotly_chart(graph, use_container_width=True)
    elif city2 != city and city2 != 'Pilih Provinsi' :
        # date_url2 = 'https://data.covid19.go.id/public/api/prov.json'
        # q2 = requests.get(date_url)
        # date_data2 = json_normalize(q2.json())
        # last_date = df.date_data[df['key']==city].to_string(index=False)[0]
        kasus2 =  List_Data[df['key']==city2].to_string(index=False)[2]
        sembuh2 = List_Data[df['key']==city2].to_string(index=False)[3]
        meninggal2 = List_Data[df['key']==city2].to_string(index=False)[4]
        rawat2 = List_Data[df['key']==city2].to_string(index=False)[5]
        st.write("""# Covid Cases at """+city2+""" Pada """)
        st.write("""# Covid Cases at """+city+""" Pada """)
        st.write("""* **Kasus     : ** """+str(kasus2)+""" di """+city2)
        st.write("""* **Sembuh    : ** """+str(sembuh2)+""" di """+city2)
        st.write("""* **Meninggal : ** """+str(meninggal2)+""" di """+city2)
        st.write("""* **DiRawat   : ** """+str(rawat2)+""" di """+city2)
        # layout = go.Layout(
        #         title = city2+'\ : '+str(kasus2)+ ' Kasus',
        #         xaxis = dict(title = "Kasus"),
        #         yaxis = dict(title = "Meninggal"),
        #     )
        # graph.update_layout(dict1 = layout, overwrite=True)
        # graph.add_trace(go.Scatter(x=kasus, y=kasus2, mode='lines', name=city2))
        
        # st.plotly_chart(graph, use_container_width=True)
            

        