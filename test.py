import streamlit as st
from st_login_form import *
from supabase import create_client
st.title("Audio Recorder")
client = st.connection(name="supabase", type=SupabaseConnection)
a = st.audio_input('Teszt')
    
if st.button('Upload'):
    if a:
        client.upload("profilepics",source='local',destination_path="hun/teszt",file=a,overwrite='true')
        st.success("done")
    else: 
        st.error('No file')
