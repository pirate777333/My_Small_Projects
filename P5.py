import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

df=pd.read_csv('D:/udemy_kurs_py/PyProj/214.agri.csv')
df.drop('text',axis=1,inplace=True)
df.drop('category',axis=1,inplace=True)

print(df.head())
print(df.columns)
print(df.shape)
print(df.isnull().sum())

df=df.sort_values(by='total exports',ascending=False)

fig=px.bar(df.iloc[:10,:],x='state',y='total exports',
           color='state',title='Top 10',
           template='plotly_dark')
fig.show()

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['total exports'].astype(float),
    locationmode='USA-states',
    colorscale='Greens',
    autocolorscale=False,
    text=df['state'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="Millions USD"
))

fig.update_layout(
    title_text='USA Agriculture Exports by State',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(0, 0, 255)'),
)

fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    #showland=True, landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
    #showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue"
)

fig.show()

df=pd.read_csv('D:/udemy_kurs_py/PyProj/215.gdp.csv')

print(df.head())
print(df.columns)
print(df.shape)
print(df.isnull().sum())

df=df.sort_values(by='GDP (BILLIONS)',ascending=False)

fig=px.bar(df.iloc[:10,:],x='COUNTRY',y='GDP (BILLIONS)',
           color='COUNTRY',title='Top 10',
           template='plotly_dark')
fig.show()

fig = go.Figure(data=go.Choropleth(
    locations=df['CODE'],
    z=df['GDP (BILLIONS)'].astype(float),
    colorscale='Blues',
    autocolorscale=False,
    text=df['COUNTRY'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="GDP Billions USD"
))

fig.update_layout(
    title_text='World GDP in Billions',
    geo = dict(
        #projection=go.layout.geo.Projection(type = 'albers usa'),
        projection_type='equirectangular',
        showlakes=True, # lakes
        lakecolor='rgb(0, 0, 255)'),
)

fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    #showland=True, landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
    #showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue"
)

fig.show()
