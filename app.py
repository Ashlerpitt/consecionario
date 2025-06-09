import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Dashboard de Análisis de Vehículos Usados')

# Checkbox para mostrar histograma del odómetro
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para mostrar gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs año del modelo'):
    st.write('Gráfico de dispersión: precio vs. año del modelo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig2, use_container_width=True)
"""

readme_content = """
# Análisis de Vehículos Usados

Este proyecto consiste en el análisis exploratorio de datos de anuncios de venta de coches en los Estados Unidos y el desarrollo de una aplicación web interactiva utilizando Streamlit.