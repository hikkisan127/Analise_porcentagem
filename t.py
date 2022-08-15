from ctypes.wintypes import RGB
import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import pandas as pd
import cufflinks as cf
import plotly.graph_objects as go
from plotly.subplots import make_subplots as ms
import altair as alt
from vega_datasets import data
 
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

st.title('Web App de teste')

Var = st.sidebar.slider('Controle de porcentagem (%)',  min_value=1, max_value=50, step=1, value=1)

location = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
title = 10
Var2 = [5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000]
Var3 = []
Var4 = []

for i in range(31):
     a = Var2[i]*Var/100
     Var3.append(a)

for i in range(31):
     a = Var2[i]-Var3[i]
     Var4.append(a)

fig = go.Figure()
fig.add_traces(go.Scatter(x=location,
                          y=Var2,
                          marker_color='white',
                          line_width=3,
                          name='Valor original')
                    )
fig.add_traces(go.Scatter(x=location,
                          y=Var3,
                          line_width=3,
                          marker_color='red',
                          name='Porcentagem')
                    )
fig.add_traces(go.Scatter(x=location,
                          y=Var4,
                          line_width=3,
                          marker_color='royalblue',
                          name='Original menos porcentagem')
                    )
fig.update_layout(plot_bgcolor='white',
                  legend=dict(x=0.02, y=0.9, 
                              orientation='h'),
                  xaxis=dict(tickfont_color='grey',
                             showline=True,
                             linewidth=1,
                             linecolor='lightgrey'),
                  yaxis=dict(tickfont_color='grey',
                             showline=True,
                             linewidth=1,
                             linecolor='lightgrey'),
                    )
fig.update_layout(legend=dict(orientation='h',y=-0.1,x=0,xanchor='left'),
                  template='plotly_dark',
                  margin=dict(t=60,b=40),
                  title=dict(text='Grafico de linha',font=dict(size=20,color='white'),yanchor='top'),
                  plot_bgcolor='RGB(39,39,49)'
                  )

fig4 = ms(rows=1,cols=1,specs=[[{'secondary_y':True}]])
fig4.add_scatter(x=location,y=Var4,name='Valor restante',stackgroup=1)
fig4.add_scatter(x=location,y=Var3,name='Valor proposto',stackgroup=1)
fig4.update_layout(legend=dict(orientation='h',y=-0.1,x=0,xanchor='left',traceorder='normal'),template='plotly_dark',margin=dict(t=60,b=40))
fig4.update_yaxes(title_text='Relação porcentagem/lucro',row=1,col=1,secondary_y=False)

st.subheader('Comparação entre as porcentagens')

col = st.columns(2)
col[0].plotly_chart(fig)
col[1].plotly_chart(fig4)

col = st.columns(1)
st.write('Dado original se refere aos 5 porcentos do valor original (100k - 400k)')
st.caption('A porcentagem calculada pode ser variada de com a barra do menu lateral')

fig2 = ms(rows=1,cols=1,specs=[[{'secondary_y':True}]])
fig2.add_bar(x=location,y=Var4,name='Valor restante',offsetgroup=1)
fig2.add_bar(x=location,y=Var3,name='Valor proposto',offsetgroup='two')
fig2.update_layout(legend=dict(orientation='h',y=-0.1,x=0,xanchor='left'),
                   template='plotly_dark',
                   margin=dict(t=60,b=40),
                   title=dict(text='grafico de barras 1',font=dict(size=20,color='white'),yanchor='top'))
fig2.update_yaxes(title_text='Relação porcentagem/lucro')

fig3 = ms(rows=1,cols=1,specs=[[{'secondary_y':True}]])
fig3.add_bar(x=location,y=Var4,name='Valor restante',offsetgroup=1)
fig3.add_bar(x=location,y=Var3,name='Valor proposto',offsetgroup=1,base=Var4)
fig3.update_layout(legend=dict(orientation='h',y=-0.1,x=0,xanchor='left'),
                   template='plotly_dark',margin=dict(t=60,b=40),
                   title=dict(text='grafico de barras 2',font=dict(size=20,color='white'),yanchor='top'))
fig3.update_yaxes(title_text='Relação porcentagem/lucro')

col = st.columns(2)

col[0].plotly_chart(fig2)
col[1].plotly_chart(fig3)

teste = st.number_input(label='digite um número aleatório', value=0)
teste2 = st.number_input(label='digite segundo número aleatório', value=0)
teste3 = st.number_input(label='digite número aleatório diferente de zero', value=1)

teste4 = (teste-teste2)*(teste+teste2)/(teste3*teste3)

st.write('foi feito o calculo meio complicado')

st.write('resposta = ', teste4)
