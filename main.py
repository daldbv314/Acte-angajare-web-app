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
    page_title='Angajare', 
    layout='wide',
)
st.title('Creează actele pentru angajare:')

#--- HIDE STREAMLIT STYLE ---
#hide_st_style = """
#            <style>
#            #MainMenu {visibility: hidden;}
#            footer {visibility: hidden;}
#            header {visibility: hidden;}
#            </style>
#            """
#st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form("Angajare", clear_on_submit=False):

        col1, col2 = st.columns(2, gap="small")
        nr_oferta = col1.text_input('Nr. oferta:', value="", key='nr_oferta', placeholder='e.g. 21', max_chars=None)
        data_oferta = col2.date_input('Data oferta:', datetime.date.today(), key='data_oferta', help=None, format="DD.MM.YYYY")

        st.divider()

        st.subheader('Angajator:')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        companie = col1.text_input('Companie', value="", key='companie', placeholder='e.g. ADAKRON (fără "SRL")', max_chars=None, help='nu adaugati "SRL"')
        cui = col2.text_input('CUI', value="", key='cui', placeholder='e.g. 112233', max_chars=None)
        nr_inreg = col3.text_input('Nr. înregistrare', value="", key='nr_inreg', placeholder='JX/XXXX/XX.XX.XXXX', max_chars=None)

        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.24, 0.24, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08], gap="small")
        loc_sed = col1.text_input('Localitate sediu', key='loc_sed', placeholder='e.g. BRAȘOV')
        str_sed = col2.text_input('Strada', key='str_sed', placeholder='e.g. NICOLAE LABIȘ')
        nr_sed = col3.text_input('Nr.', key='nr_sed', placeholder='xx')
        bl_sed = col4.text_input('Bl.', key='bl_sed', placeholder='xx')
        sc_sed = col5.text_input('Sc.', key='sc_sed', placeholder='xx')
        et_sed = col6.text_input('Et.', key='et_sed', placeholder='xx')
        ap_sed = col7.text_input('Ap.', key='ap_sed', placeholder='xx')
        cam_sed = col8.text_input('Camera/birou', key='cam_sed', placeholder='xx')

        col1, col2, col3, col4 = st.columns(4, gap="small")
        jud_sed = col1.text_input('Județ', key='jud_sed', placeholder='e.g. BRAȘOV')
        reprez = col2.text_input('Reprezentant legal', key='reprez', placeholder='e.g. POPESCU ANDREI')

        st.divider()

        st.subheader('Angajat:')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        ang_nume = col1.text_input('Nume angajat:', key='ang_nume', placeholder='e.g. MIHĂESCU ȘTEFAN')
        ang_cetatean = col2.text_input('Cetațean:', key='ang_cetatean', placeholder='român')   ##### confirma ca placeholder-ul se transmite mai departe in template
        
        col1, col2, col3, col4 = st.columns(4, gap="small")
        ang_data_n = col1.date_input('Data naștere:', datetime.date.today(), key='ang_data_n', help=None, format="DD.MM.YYYY")
        ang_loc_n = col2.text_input('Localitate naștere:', value="", key='ang_loc_n', max_chars=None)
        ang_jud_n = col3.text_input('Județ/sector naștere:', value="", key='ang_jud_n', max_chars=None)
        ang_tara_n = col4.text_input('Țara naștere:', value="", key='ang_tara_n', placeholder='România', max_chars=None)

        col1, col2, col3, col4, col5, col6, col7 = st.columns([0.25, 0.25, 0.1, 0.1, 0.1, 0.1, 0.1], gap="small")
        loc_dom = col1.text_input('Localitate domiciliu', key='loc_dom', placeholder='e.g. BRAȘOV')
        str_dom = col2.text_input('Strada domiciliu', key='str_dom', placeholder='e.g. NICOLAE LABIȘ')
        nr_dom = col3.text_input('Nr.', key='nr_dom', placeholder='xx')
        bl_dom = col4.text_input('Bl.', key='bl_dom', placeholder='xx')
        sc_dom = col5.text_input('Sc.', key='sc_dom', placeholder='xx')
        et_dom = col6.text_input('Et.', key='et_dom', placeholder='xx')
        ap_dom = col7.text_input('Ap.', key='ap_dom', placeholder='xx')

        col1, col2, col3, col4 = st.columns(4, gap="small")
        jud_dom = col1.text_input('Județ/sector domiciliu', key='jud_dom', placeholder='e.g. BRAȘOV')
        tara_dom = col2.text_input('Țara domiciliu:', value="", key='tara_dom', placeholder='România', max_chars=None)

        col1, col2, col3, col4, col5, col6, col7 = st.columns([0.12, 0.13, 0.065, 0.18, 0.245, 0.13, 0.13], gap="small")
        ang_cnp = col1.text_input('CNP:', key='ang_cnp', max_chars=13)
        ang_tip_act = col2.selectbox('Tip act identitate:', ("CI", "Pașaport", "Permis de ședere"), key='ang_tip_act', index=0, help=None)
        ang_serie_act = col3.text_input('Serie:', value="", key='ang_serie_act', placeholder='România', max_chars=None)
        ang_nr_act = col4.text_input('Nr.:', value="", key='ang_nr_act', placeholder='România', max_chars=None)
        ang_act_elib = col5.text_input('Eliberat de:', value="", key='ang_act_elib', placeholder='România', max_chars=None)
        ang_data_elib = col6.date_input('Data eliberare:', datetime.date.today(), key='ang_data_elib', help=None, format="DD.MM.YYYY")
        ang_data_exp = col7.date_input('Data expirare:', datetime.date.today(), key='ang_data_exp', help=None, format="DD.MM.YYYY")
