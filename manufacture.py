import streamlit as st

import datetime 
import pytz #timezone


    
def app():
    st.title("Assembly Unit")
    
    button1=st.button("Assemble New Unit")

    if button1:
        
        
        getProduct=entry.pop()
        pid=getProduct['args']['product_id']
        batch_id=getProduct['args']['batch_id']
        pid=pid+1

        timestamp = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
       
        for entry in filter.get_all_entries():
            if entry['args']['timestamp'] == str(timestamp):
                batch_id=int(entry['args']['batch_id'])
                timestamp=str(timestamp)
                
        for entry in filter.get_all_entries():
            pid=entry['args']['product_id']
        batch_id=pid//100
        timestamp=str(timestamp)
       

        st.write('Product Serial ID:',pid,'Batch:',batch_id,'Transaction ID:','timestamp:',timestamp)