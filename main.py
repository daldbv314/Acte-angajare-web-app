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
st.title('Creează actele pentru angajare (SRL | perioadă nedeterminată):')

#--- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def var_dictionary():
    var_dict = {
        'nr_oferta': nr_oferta,
        'data_oferta': data_oferta,

        'companie': companie,
        'cui': cui,
        'nr_inreg': nr_inreg,
        'loc_sed': loc_sed,
        'str_sed': str_sed,
        'nr_sed': nr_sed,
        'bl_sed': bl_sed,
        'sc_sed': sc_sed,
        'et_sed': et_sed,
        'ap_sed': ap_sed,
        'cam_sed': cam_sed,
        'jud_sed': jud_sed,
        'tara_sed': tara_sed,
        'adm_nume': adm_nume,

        'ang_nume': ang_nume,
        'ang_cetatean': ang_cetatean,
        'ang_data_n': ang_data_n,
        'ang_loc_n': ang_loc_n,
        'ang_jud_n': ang_jud_n,
        'ang_tara_n': ang_tara_n,
        'loc_dom': loc_dom,
        'str_dom': str_dom,
        'nr_dom': nr_dom,
        'bl_dom': bl_dom,
        'sc_dom': sc_dom,
        'et_dom': et_dom,
        'ap_dom': ap_dom,
        'jud_dom': jud_dom,
        'tara_dom': tara_dom,

        'ang_cnp': ang_cnp,
        'ang_tip_act': ang_tip_act,
        'ang_serie_act': ang_serie_act,
        'ang_nr_act': ang_nr_act,
        'ang_act_elib_d': ang_act_elib_d,
        'ang_data_elib': ang_data_elib,
        'ang_data_exp': ang_data_exp,

        'ang_functie': ang_functie,
        'cod_functie': cod_functie,
        'data_incep_activ': data_incep_activ,
        'ang_sal_brut': ang_sal_brut,
        'nr_h_zi': nr_h_zi,
        'nr_h_sapt': nr_h_sapt,
        'data_semn_cim': data_semn_cim,
        'nr_cim': nr_cim

    }
    return var_dict


def doc01():
    doc01_path = Path.cwd() / "Templates" / "01-acord-confidentialitate.docx"
    doc01_doc = DocxTemplate(doc01_path)
    context = var_dictionary()
    doc01_doc.render(context)
    doc01_bytes = BytesIO()
    doc01_doc.save(doc01_bytes)
    return doc01_bytes.getvalue()


def doc02():
    doc02_path = Path.cwd() / "Templates" / "02-acord-GDPR.docx"
    doc02_doc = DocxTemplate(doc02_path)
    context = var_dictionary()
    doc02_doc.render(context)
    doc02_bytes = BytesIO()
    doc02_doc.save(doc02_bytes)
    return doc02_bytes.getvalue()


def doc03():
    doc03_path = Path.cwd() / "Templates" / "03-cim.docx"
    doc03_doc = DocxTemplate(doc03_path)
    context = var_dictionary()
    doc03_doc.render(context)
    doc03_bytes = BytesIO()
    doc03_doc.save(doc03_bytes)
    return doc03_bytes.getvalue()


def doc04():
    doc04_path = Path.cwd() / "Templates" / "04-declaratie-de-sanatate.docx"
    doc04_doc = DocxTemplate(doc04_path)
    context = var_dictionary()
    doc04_doc.render(context)
    doc04_bytes = BytesIO()
    doc04_doc.save(doc04_bytes)
    return doc04_bytes.getvalue()


def doc05():
    doc05_path = Path.cwd() / "Templates" / "05-declaratie-propria-raspundere-functia-de-baza.docx"
    doc05_doc = DocxTemplate(doc05_path)
    context = var_dictionary()
    doc05_doc.render(context)
    doc05_bytes = BytesIO()
    doc05_doc.save(doc05_bytes)
    return doc05_bytes.getvalue()


def doc06():
    doc06_path = Path.cwd() / "Templates" / "06-fisa-postului-Programator-de-sistem-informatic.docx"
    doc06_doc = DocxTemplate(doc06_path)
    context = var_dictionary()
    doc06_doc.render(context)
    doc06_bytes = BytesIO()
    doc06_doc.save(doc06_bytes)
    return doc06_bytes.getvalue()


def doc07():
    doc07_path = Path.cwd() / "Templates" / "07-imputernicire-schimbare-parola-itm.docx"
    doc07_doc = DocxTemplate(doc07_path)
    context = var_dictionary()
    doc07_doc.render(context)
    doc07_bytes = BytesIO()
    doc07_doc.save(doc07_bytes)
    return doc07_bytes.getvalue()


def doc08():
    doc08_path = Path.cwd() / "Templates" / "08-oferta-de-angajare.docx"
    doc08_doc = DocxTemplate(doc08_path)
    context = var_dictionary()
    doc08_doc.render(context)
    doc08_bytes = BytesIO()
    doc08_doc.save(doc08_bytes)
    return doc08_bytes.getvalue()


def create_zip_archive():
    # Generate the content for each document
    doc01_content = doc01()
    doc02_content = doc02()
    doc03_content = doc03()
    doc04_content = doc04()
    doc05_content = doc05()
    doc06_content = doc06()
    doc07_content = doc07()
    doc08_content = doc08()

    # Create an in-memory zip file
    with io.BytesIO() as zip_buffer:
        with ZipFile(zip_buffer, 'w') as zipf:
            # Add each doc to the archive
            zipf.writestr(f"{companie}-01-acord-confidentialitate.docx", doc01_content)
            zipf.writestr(f"{companie}-02-acord-GDPR.docx", doc02_content)
            zipf.writestr(f"{companie}-03-cim.docx", doc03_content)
            zipf.writestr(f"{companie}-04-declaratie-de-sanatate.docx", doc04_content)
            zipf.writestr(f"{companie}-05-declaratie-propria-raspundere-functia-de-baza.docx", doc05_content)
            zipf.writestr(f"{companie}-06-fisa-postului-Programator-de-sistem-informatic.docx", doc06_content)
            zipf.writestr(f"{companie}-07-imputernicire-schimbare-parola-itm.docx", doc07_content)
            zipf.writestr(f"{companie}-08-oferta-de-angajare.docx", doc08_content)
        # Get the zip archive content as bytes
        zip_bytes = zip_buffer.getvalue()
    return zip_bytes

with st.form("Angajare", clear_on_submit=False):

        col1, col2 = st.columns(2, gap="small")
        nr_oferta = col1.text_input('Nr. ofertă:', value="", key='nr_oferta', placeholder='e.g. 21', max_chars=None)
        data_oferta = col2.date_input('Data ofertă:', datetime.date.today(), key='data_oferta', help=None, format="DD.MM.YYYY")

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
        tara_sed = col2.text_input('Țara sediu:', value="România", key='tara_sed', placeholder='e.g. România', max_chars=None)
        adm_nume = col3.text_input('Reprezentant legal', key='adm_nume', placeholder='e.g. POPESCU ANDREI')

        st.divider()

        st.subheader('Angajat:')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        ang_nume = col1.text_input('Nume angajat:', key='ang_nume', placeholder='e.g. MIHĂESCU ȘTEFAN')
        ang_cetatean = col2.text_input('Cetațean:', value="român", key='ang_cetatean', placeholder='e.g. român')
        
        col1, col2, col3, col4 = st.columns(4, gap="small")
        ang_data_n = col1.date_input('Data naștere:', datetime.date.today(), key='ang_data_n', help=None, format="DD.MM.YYYY")
        ang_loc_n = col2.text_input('Localitate naștere:', value="", key='ang_loc_n', max_chars=None)
        ang_jud_n = col3.text_input('Județ/sector naștere:', value="", key='ang_jud_n', max_chars=None)
        ang_tara_n = col4.text_input('Țara naștere:', value="România", key='ang_tara_n', placeholder='e.g. România', max_chars=None)

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
        tara_dom = col2.text_input('Țara domiciliu:', value="România", key='tara_dom', placeholder='e.g. România', max_chars=None)

        col1, col2, col3, col4, col5, col6, col7 = st.columns([0.12, 0.13, 0.065, 0.18, 0.245, 0.13, 0.13], gap="small")
        ang_cnp = col1.text_input('CNP:', key='ang_cnp', max_chars=13)
        ang_tip_act = col2.selectbox('Tip act identitate:', ("CI", "Pașaport", "Permis de ședere"), key='ang_tip_act', index=0, help=None)
        ang_serie_act = col3.text_input('Serie:', value="", key='ang_serie_act', placeholder='', max_chars=None)
        ang_nr_act = col4.text_input('Nr.:', value="", key='ang_nr_act', placeholder='', max_chars=None)
        ang_act_elib_d = col5.text_input('Eliberat de:', value="", key='ang_act_elib_d', placeholder='e.g. SPCLEP BRAȘOV', max_chars=None)
        ang_data_elib = col6.date_input('Data eliberare:', datetime.date.today(), key='ang_data_elib', help=None, format="DD.MM.YYYY")
        ang_data_exp = col7.date_input('Data expirare:', datetime.date.today(), key='ang_data_exp', help=None, format="DD.MM.YYYY")

        st.divider()

        st.subheader('Elemente contract de muncă:')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        ang_functie = col1.text_input('Funcția:', value="", key='ang_functie', placeholder='', max_chars=None)
        cod_functie = col2.text_input('Cod funcție:', value="", key='cod_functie', placeholder='', max_chars=None)
        data_incep_activ = col3.date_input('Data începere activitate:', datetime.date.today(), key='data_incep_activ', help=None, format="DD.MM.YYYY")
        ang_sal_brut = col4.text_input('Salariu brut:', value="", key='ang_sal_brut', placeholder='', max_chars=None)
        
        col1, col2, col3, col4 = st.columns(4, gap="small")
        nr_h_zi = col1.text_input('Nr. ore pe zi:', value="", key='nr_h_zi', placeholder='', max_chars=None)
        nr_h_sapt = col2.text_input('Nr. ore pe săptamnână:', value="", key='nr_h_sapt', placeholder='', max_chars=None)
        data_semn_cim = col3.date_input('Data semnării CIM:', datetime.date.today(), key='data_semn_cim', help=None, format="DD.MM.YYYY")
        nr_cim = col4.text_input('Nr. CIM:', value="", key='nr_cim', placeholder='', max_chars=None)

        st.divider()

        st.write(' ')
        submitted = st.form_submit_button("Pas 1: Crează documentele", type="primary")


if submitted:
    with st.spinner("Se generează documentele..."):
        zip_archive = create_zip_archive()
    st.success("Succes! Documentele pot fi descărcate acum de mai jos!")
    st.download_button(label="Pas 2: Downloadează", data=zip_archive, file_name=f"{companie}-acte-angajare-{datetime.date.today()}.zip", mime="docx", type="primary")
