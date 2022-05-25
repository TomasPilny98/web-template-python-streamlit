import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie

from resources import *

st.set_page_config(page_title='Hello world page', page_icon=':earth_americas:', layout='wide')


def load_lottie_url(url: str) -> json:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("static/style.css")

# header
with st.container():
    st.title("Robotické sekačky o d A do Z")
    st.subheader("Ahoj moje jméno je Jakub Mádl a chci bejt brzo rentiér  :wave:")

# what i do
with st.container():
    st.write("---")
    left_col, right_col = st.columns((1, 3))
    with left_col:
        st.header("Co vám mohu nabídnout")
        st.header("##")
        st.write(
            """
            - Široký výběr robotických sekaček
            - Autorizovaný servis po dobu záruční doby
            - Amway sezení pokud budete mít zájem
            - Nevim nějakej text, netušim co sem napsat
            """
        )
    with right_col:
        st_lottie(load_lottie_url(MOWER_LOTTIE), height=230, key='mower')

with st.container():
    st.write("---")
    st.header("Nabízené modely sekaček")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("GOLEM")
    st.image(MOWER1)
    with st.expander(INFO):
        st.write("""
            - informace č. 1
            - informace č. 2
            - informace č. 3
            - cena: xxx ,- Kč
            """)

with col2:
    st.subheader("MADONA")
    st.image(MOWER4)
    with st.expander(INFO):
        st.write("""
            - informace č. 1
            - informace č. 2
            - informace č. 3
            - cena: xxx ,- Kč
        """)

with col3:
    st.subheader("KAKTAJM")
    st.image(MOWER3)
    with st.expander(INFO):
        st.write("""
            - informace č. 1
            - informace č. 2
            - informace č. 3
            - cena: xxx ,- Kč
        """)

with st.container():
    st.write("---")
    st.header("Kontaktujte mě")
    st.write("##")
    contact_form: str = """
                        <form action="https://formsubmit.co/tiger.pilnas@seznam.cz" method="POST">
                        <input type="hidden" name="_captcha", value="False">
                        <input type="text" name="name" placeholder="Vaše jméno" required>
                        <input type="email" name="email" placeholder="Váš e-mail" required>
                        <textarea name="message" placeholder="Vaše zpráva" required></textarea>
                        <button type="submit">Odeslat</button>
                        </form>"""
    left_col, right_col = st.columns((1,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()

