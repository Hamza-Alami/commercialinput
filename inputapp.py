import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os

st.set_page_config(layout='wide')
st.title('Application input des Agents WIA')

#DF creation
df = pd.DataFrame(columns=['Agent','Agence de visite','Raison de visite','Date de visite'])

#INPUTS
#N of visits

ndv = st.slider('Combien de visites avez vous effectuer?', 0, 100, 1)
st.write("I'm ", ndv, 'years old')

listagent = []
listagence = []
listraison = []
listdate = []


inagent= st.text_input('Nom')
listagent.append(inagent)
listagentfull = listagent*ndv

while len(listagence) < ndv:
    inagence = st.text_input('Agence :')
    listagence.append(inagence)

while len(listraison) < ndv:
    inraison = st.text_input('Raison de visite :')
    listraison.append(inraison)

while len(listdate) < ndv:
    indate = st.date_input(
     "Date de la visite :")
    listdate.append(indate)
