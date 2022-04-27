import streamlit as st
import manufacture, qc, track, retailer, distributer

st.sidebar.title("Navigation")
PAGES = {
    "Assembly": manufacture,
    "Quality Control": qc,
    "Track Product":track,
    "RETAILER": retailer,
    "DISTRIBUTER": distributer
}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()