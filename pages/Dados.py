import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

image = Image.open('1.png')
st.set_page_config(
    page_title="Site teste", 
    page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # Este é o site teste.
         """
     })

Var = st.sidebar.slider('Controle de porcentagem (%)',  min_value=1, max_value=50, step=1, value=1)
location = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
Var2 = [5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000]
Var3 = []
Var4 = []
title = 10

for i in range(31):
     a = Var2[i]*Var/100
     Var3.append(a)

for i in range(31):
     a = Var2[i]-Var3[i]
     Var4.append(a)

df = pd.DataFrame({'5 porcento do original': Var2,
                   'Valor de referência': Var3,
                   'Quanto sobra': Var4})

df = df.astype('int')

st.subheader('Valores tabelados')
st.dataframe(df, 1800, 1122)