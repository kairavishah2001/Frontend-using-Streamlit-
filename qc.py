import streamlit as st
import datetime 
import pytz #timezone



def app():
    st.title("Quality Control")
    product_id=st.text_input("Product ID")
    officer_name=st.text_input("Officer Name")
    message = st.text_input("Comment")
    grade=st.text_input("Grade(1/0)")

    button1=st.button("Certify")
    if button1:
       
        timestamp = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        
        st.success(f"Certified Product ID:{product_id} at {timestamp}")
        