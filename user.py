import streamlit as st
import pandas as pd
import numpy as np
from st_login_form import *
from supabase import create_client
import json
def Char(id:int):
    char = client.table('characters').select('*',count=None).eq('id',id)
    char = char.execute()
    user = client.table('users').select('*',count=None).eq('username',st.session_state["username"])
    user = user.execute()
    uid = user.data[0]['id']
    texts = client.table('texts').select('*',count=None).eq('character_id',char.data[0]['id'])
    texts = texts.execute()
    charname = char.data[0]['name']
    if char.data[0]['assigned_user'] == uid:
        with st.expander(charname):
                # col1, col2,col3,col4 = st.columns(4)
                # with col1: st.write('Fájlnév')
                # with col2: st.write('Angol')
                # with col3: st.write('Magyar')
                # with col4: st.write('Eredeti hang')
                # for t in texts.data:
                #     with st.container(border=True,height=100):
                #         with col1: st.write(t['filename'])
                #         with col2: st.write(t['eng_text'])
                #         with col3: st.write(t['hun_text'])
                row = st.columns(4)
                for t in texts.data:
                    row[0].container(height=100).write(t['filename'])
                    row[1].container(height=100).write(t['eng_text'])
                    row[2].container(height=100).write(t['hun_text'])
                    row[3].container(height=100).audio(client.get_public_url(char.data[0]['name'],str(t['filename'])+'.mp3'))
                
                    
            
                     


if st.session_state["authenticated"]:
    client = st.connection(name="supabase", type=SupabaseConnection)
    with st.expander("Profilkép"):
        uploaded_file = st.file_uploader("")
        if uploaded_file is not None:
            client.upload("profilepics",source='local',destination_path=st.session_state['username'],file=uploaded_file,overwrite='true')
        
        if client.get_public_url("profilepics",st.session_state['username']) != None:
            st.image(client.get_public_url("profilepics",st.session_state['username']))
    
    if st.session_state["username"] == "Chaze":
        with st.expander("Felhasználók karakterhez rendelése"):
            characters = client.table("characters").select('*',count=None).order("id")
            characters = characters.execute()
            users = client.table("users").select('*',count=None).order("username")
            users = users.execute()
            Users = []
            for u in users.data:
                Users.append(str(u['id']) + '. '+u['username'])
            for r in characters.data:
                
                
                   with st.form(r['name']):
                    def Save(values):
                        st.warning(values)
                    option =  st.selectbox(r['name'],Users)
                    cID = r['id']
                    id = str(option).split('.')[0]
                    query = client.table('characters').update({"assigned_user":id},count=None).eq("id",cID)
                    submit = st.form_submit_button("Mentés")
                    if submit:
                        query.execute()

    for i in range(1,42):
        Char(i)
else:
    st.error("Nem vagy bejelentkezve!")
