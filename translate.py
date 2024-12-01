import streamlit as st
import pandas as pd
import numpy as np
from st_login_form import *
from supabase import create_client

def Char(id:int):
    char = client.table('characters').select('*',count=None).eq('id',id)
    char = char.execute()
    user = client.table('users').select('*',count=None).eq('username',st.session_state["username"])
    user = user.execute()
    uid = user.data[0]['id']
    text = client.table('texts').select('*',count=None).eq('character_id',char.data[0]['id'])
    text = text.execute()
    charname = char.data[0]['name']
    if char.data[0]['assigned_user'] == uid:
        with st.expander(charname):
                for t in text.data:
                    with st.container(border=True):
                        st.text_input(label='Angol',value=t['eng_text'],disabled=True,key=str(t['id'])+"_eng")
                        st.text_input(label="Magyar",value=t['hun_text'],disabled=True,key=str(t['id'])+"_hun")
                        st.write("Eredeti hang:")
                        st.audio(client.get_public_url(charname,str(t['filename'])+'.mp3'))
                        st.write("Magyar hang:")
                        st.audio(client.get_public_url(charname,"hun/"+t['filename']+".wav"))
                        a = st.audio_input(label='a',label_visibility='collapsed',key=t['filename'])                            
                        if st.button("Feltöltés",key=t['filename']+'_button'):
                            if a:
                                    client.upload(charname,source='local',destination_path="hun/"+t['filename']+".wav",file=a,overwrite='true')
                                    st.toast("✅ Sikeres feltöltés")
                            else: 
                                    st.toast("❌ Nincs feltölthető hanganyag")
                    
            
                     

if st.session_state["authenticated"]:
    client = st.connection(name="supabase", type=SupabaseConnection)
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
