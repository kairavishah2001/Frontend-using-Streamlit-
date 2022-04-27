import streamlit as st


def app():
    st.title("Retailer")
    retailer = st.text_input("Retailer ID")

    distributer = st.text_input("Distributer ID")
    option = st.selectbox(
        'Distributor', ('Suresh Modi', 'Manoj Patel', 'Raj Tiwari'))
    st.write('You selected:', option)

    button1 = st.button("Order")