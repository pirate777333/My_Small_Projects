import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
import folium
import matplotlib.pyplot as plt

##df=pd.read_csv('D:/udemy_kurs_py/PyProj/239.volcano.csv')
##
##print(df.head())
##print(df.columns)
##print(df.shape)
##print(df.isnull().sum())
##
##mapa = folium.Map()
##
##for i,r in df.iterrows():
##    
##    x=folium.FeatureGroup(name='My Map')
##    x.add_child(folium.Marker(location=[r['Latitude'],r['Longitude']],popup=r['Name'],icon=folium.Icon(color='red')))
##    mapa.add_child(x)
##
##mapa.save('Vulkani.html')

df=pd.read_csv('D:/udemy_kurs_py/PyProj/241.us+cities+pop.csv')

print(df.head())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
print(df['pop'].describe())

def markerCol(population):
    if population<10000:
        return 'green'
    elif population<100000:
        return 'blue'
    elif population<1000000:
        return 'orange'
    elif population<10000000:
        return 'red'
    elif population<100000000:
        return 'black'

    

mapa = folium.Map()

for i,r in df.iterrows():
    
    x=folium.FeatureGroup(name='My Map')
    x.add_child(folium.Marker(location=[r['lat'],r['lon']],popup=r['name']+' '+str(r['pop']),icon=folium.Icon(color=markerCol(r['pop']))))
    mapa.add_child(x)

mapa.save('Gradovi.html')
