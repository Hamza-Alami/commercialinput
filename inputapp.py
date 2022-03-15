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
RV = st.text_input('Rasion de la visite:')

if st.button("Ajouter une visite"):
    get_data().append({"Nom": Nom, "Agence": Agence, "Date": Date, "Raison": RV})

st.write(pd.DataFrame(get_data()))

#DF creation
#df = pd.DataFrame()

#INPUTS
#N of visits

#ndv = st.slider('Combien de visites avez vous effectuer?', 0, 100, 1)
#st.write("I'm ", ndv, 'years old')

#listagent = []
#listagence = []
#listraison = []
#listdate = []


#inagent= st.text_input('Nom:')
#listagent.append(inagent)
#listagentfull = listagent*ndv

#while len(listagence) < ndv:
    #inagence = st.text_input('Agence visité:')
    #listagence.append(inagence)

#while len(listraison) < ndv:
    #inraison = st.text_input('Raison de la visite:')
    #listraison.append(inraison)

#while len(listdate) < ndv:
    #indate = st.date_input("Date de la visite:")
    #listdate.append(indate)
    
#df['Agent'] = listagentfull
#df['Agence'] = listagence
#df['Raison de visite'] = listraison
#df['Date'] = listdate

#st.dataframe(df)
