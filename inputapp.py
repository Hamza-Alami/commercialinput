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

nombredevisites = st.number_input('Nombres de visites: ')
st.write('Visites éfféctuées: ', nombredevisites)

page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ecoactu.ma%2Fbadreddine-belghiti-nomme-directeur-general-de-wafa-ima-assistance%2F&psig=AOvVaw3O-CrJRv_9DT8a2fYGGD-I&ust=1647461105452000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNCNpYL1yPYCFQAAAAAdAAAAABAR");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

