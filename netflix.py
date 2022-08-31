import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

st.title('Netflix app')

import codecs
@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text('Cargando datos...')
data = load_data(501)
data_load_state.text("Los datos han sido cargados")


st.sidebar.write("Puedes seleccionar diferentes elementos para visualizar información")

agree = st.sidebar.checkbox("Mostrar todos los filmes")
if agree:
    st.header("Todos los filmes")
    st.dataframe(data)


@st.cache
def load_data_byname(name):
    filtered_data_byname=data[data["name"].str.upper().str.contains(name.upper())]
    
    return filtered_data_byname

myname= st.sidebar.text_input("Título del filme: ")
btnName=st.sidebar.button("Buscar filmes")

if(btnName):
    filterbyname= load_data_byname(myname)

    st.dataframe(filterbyname)


@st.cache
def load_data_bydirector(director):
    filtered_data_bydirector=data[data["director"]==director]
    
    return filtered_data_bydirector

selected_director=st.sidebar.selectbox("Seleccionar Director", data["director"].unique())
btnFilterbyDirector=st.sidebar.button("Filtrar Director")

if(btnFilterbyDirector):
    filterbydirector= load_data_bydirector(selected_director)

    st.dataframe(filterbydirector)


