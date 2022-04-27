import streamlit as st



def app():
    st.title("Track Product")
    product=st.text_input("Enter Product ID")
    
    
    button1=st.button("Check")