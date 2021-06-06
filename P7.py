import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
import folium
import matplotlib.pyplot as plt
import seaborn as sns

donation=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/258.Donations.csv')
donor=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/259.Donors.csv')
project=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/260.Projects.csv')
resource=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/261.Resources.csv')
school=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/262.Schools.csv')
teacher=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/263.Teachers.csv')

data=pd.merge(donation,project,how='inner',on='Project ID')
print(1)
data=pd.merge(data,donor,how='inner',on='Donor ID')
print(1)
data=pd.merge(data,school,how='inner',on='School ID')
print(1)
data=pd.merge(data,teacher,how='inner',on='Teacher ID')
print(1)

print(data.head())
print(data.columns)
print(data.shape)
print(data.isnull().sum())

data.to_csv('Complete.csv',index=False)




df=pd.read_csv('D:/udemy_kurs_py/PyProj/P7DS/Complete.csv')

print(df.head())
print(df.columns)
print(df.shape)
print(df.isnull().sum())

s=school.groupby('School State')['School ID'].count().reset_index()
s=s.sort_values(by='School ID', ascending=False)
fig=px.plot(s,x='School State',y='School ID',color='School State',
            title='School State',template='plotly_dark')
fig.show()

s2=df.groupby('School State')['Donation Amount'].mean().reset_index()
s2=s2.sort_values(by='Donation Amount', ascending=False)
fig=px.plot(s2.iloc[:10,:],x='School State',y='Donation Amount',color='School State',
            title='Donation Amount',template='plotly_dark')
fig.show()

ds=df.groupby('Donor State')['Donation ID'].count().reset_index()
ds=ds.sort_values(by='Donation ID', ascending=False)
fig=px.plot(ds.iloc[:10,:],x='Donor State',y='Donation ID',color='Donor State',
            title='Donations',template='plotly_dark')
fig.show()

s=s.set_index('School State')
ds=ds.set_index('Donor State')
full=pd.merge(s, ds, left_index=True, right_index=True)
full.dropna(inplace=True)

sns.countplot(df['Project Type'])
plt.show()
sns.countplot(df['Project Subject Category Tree'].dropna())
plt.show()

fr=df.groupby('Project Type')['Donation Amount'].sum().reset_index()
fr=fr.sort_values(by='Donation Amount', ascending=False)
fig=px.plot(fr.iloc[:10,:],x='Project Type',y='Donation Amount',color='Project Type',
            title='Donations',template='plotly_dark')
fig.show()

df.dropna(inplace=True)
df['Project Posted Date']= pd.to_datetime(df['Project Posted Date'])
df['Project Fully Funded Date']= pd.to_datetime(df['Project Fully Funded Date'])

df['Difference_days'] = (df['Project Fully Funded Date'] - df['Project Posted Date']).dt.days

dd=df.groupby('School State')['Difference_days'].mean().reset_index()
dd=dd.sort_values(by='Difference_days', ascending=False)
fig=px.plot(dd.iloc[:10,:],x='School State',y='Difference_days',color='School State',
            title='Difference_days',template='plotly_dark')
fig.show()
