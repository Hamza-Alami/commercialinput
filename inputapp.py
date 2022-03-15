import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os

st.set_page_config(layout='wide')
st.title('Application input des Agents WIA')

@st.cache(allow_output_mutation=True)
def get_data():
    return []

Nom = st.text_input('Nom:')
Agence = st.text_input('Agence visité:')
Date = st.date_input("Date de la visite:")
RV = st.text_input('Raison de la visite:')

if st.button("Ajouter une visite"):
    get_data().append({"Nom": Nom, "Agence": Agence, "Date": Date, "Raison": RV})

df = pd.DataFrame(get_data())

ix = st.text_input('Index de la visite que vous souhaitez supprimer:')

if st.button("Supprimer une visite"):
    df = df.drop(ix)
st.write(df)
    

