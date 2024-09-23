import os
import io
import datetime
import streamlit as st
from zipfile import ZipFile
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from io import BytesIO
import locale

locale.setlocale(locale.LC_ALL, 'ro_RO')

st.set_page_config(
    page_title='Inventariere', 
    layout='wide',
)
st.title('Creează actele pentru angajare:')




