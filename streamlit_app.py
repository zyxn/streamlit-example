import plotly.express as px
import streamlit as st

import pandas as pd

option_x = st.selectbox(
    'Apa yang mau kamu cari?',
    (' gdppercap ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' Country ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
st.write('X :', option_x)

option_y = st.selectbox(
    'Apa yang mau kamu cari?',
    (' lifeexpectatbirth ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' Country ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
st.write('Y :', option_y)

option_size = st.selectbox(
    'Apa yang mau kamu cari?',
    (' population ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' Country ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
st.write('Size :', option_size)

option_color = st.selectbox(
    'Apa yang mau kamu cari?',
    (' birthrate ', '  Area ', ' Country ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
st.write('Color :', option_color)

df = pd.read_csv('data.csv')
fig = px.scatter(
    x=df[option_x],
    y=df[option_y],
    size=df[option_size],
    color=df[option_color],
    size_max=60,
)
# print(list(df.columns.values))
# print(df[' gdppercap '].head(5))

st.plotly_chart(fig, theme="streamlit", use_container_width=True)



#hallo do