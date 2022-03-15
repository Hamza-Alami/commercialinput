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

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
