import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os
import xlsxwriter
from io import BytesIO

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
    df = df.drop(index=int(ix))
    
st.write(df)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel(df)
st.download_button(label='📥 Download Current Result',
                                data=df_xlsx ,
                                file_name= 'df_test.xlsx')
