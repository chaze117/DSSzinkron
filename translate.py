import streamlit as st
import pandas as pd
import numpy as np
from st_login_form import *
from supabase import create_client
client = st.connection(name="supabase", type=SupabaseConnection)
users = client.table("users").select('*',count=None).order('id').execute()
characters = client.table('characters').select('*',count=None).order('id').execute()
Users = []
Characters = []
Done = {}
for c in characters.data:
    Done[c['name']] = c['done']
for u in users.data:
    Users.append(str(u['id']) + '. '+u['username'])
for c in characters.data:
     Characters.append(str(c['id']) + '. '+c['name'])
def searchUser(data,name):
    for item in data:
        if item['username'] == name:
            return item['id']                    
if len(st.session_state) > 0:
    if st.session_state["authenticated"]:
        if st.session_state["username"] == "Chaze":
            with st.container(border=True):
                st.write('Felhasználók karakterhez rendelése')
                with st.form('assign'):
                    col1, col2 = st.columns(2)
                    with col1:
                        char = st.selectbox('Karakter',Characters)
                    with col2:
                        user = st.selectbox('Felhasználó',Users)
                    if st.form_submit_button("Mentés"):
                        cid = str(char).split('.')[0]
                        uid = str(user).split('.')[0]
                        query = client.table('characters').update({"assigned_user":uid},count=None).eq("id",cid).execute()
                        if query != None: 
                            st.toast("✅ Sikeres hozzárendelés")
                            st.rerun()
                        else: st.toast("❌ Valami hiba történt") 
                st.write('Készültségi állapot módosítása')
                with st.container(border=True):
                    col3,col4 = st.columns(2)
                    with col3:
                        Char = st.selectbox('Karakter',Characters)
                    with col4:
                       num = st.number_input('Kész van', min_value=0,value=(Done[str(Char).split('. ')[1]]))
                    if st.button('Mentés'): 
                        id = str(Char).split('.')[0]
                        q = client.table('characters').update({"done":num},count=None).eq("id",id).execute()
                        if q != None: st.toast("✅ Sikeres hozzárendelés") 
                        else: st.toast("❌ Valami hiba történt") 
        with st.container(border=True):
            uid = searchUser(users.data,st.session_state["username"])
            chars = []
            for c in characters.data:
                if c['assigned_user'] == uid:
                    chars.append(str(c['id']) + '. '+c['name'])
            if len(chars) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    char = st.selectbox("Karakter",chars)
                id = str(char).split('.')[0]
                charname = str(char).split('.')[1].removeprefix(' ')
                texts = client.table('texts').select('id,hun_text',count=None).eq('character_id',id).execute()
                with col2:
                    ids = []
                    for t in texts.data:
                        end = ""
                        if len(t['hun_text']) > 20: end="..."
                        ids.append(str(t['id'])+". - "+t['hun_text'][0:20]+ end)
                    text = st.selectbox("Szöveg",ids)
                ID = str(text).split('.')[0]
                TEXT = client.table('texts').select('*',count=None).eq('id',ID).execute()
                with st.container(border=True):
                    st.text_area(label='Angol',value=TEXT.data[0]['eng_text'],disabled=True)
                    st.text_area(label='Magyar',value=TEXT.data[0]['hun_text'],disabled=True)
                    col3,col4 = st.columns(2)
                    with col3:
                        st.write("Eredeti hang:")
                        st.audio(client.get_public_url(charname,str(TEXT.data[0]['filename'])+'.mp3'))
                    with col4:
                        st.write("Magyar hang:")
                        st.audio(client.get_public_url(charname,"hun/"+str(TEXT.data[0]['filename'])+".wav"))
                    a = st.audio_input(label='a',label_visibility='collapsed')                            
                    if st.button("Feltöltés"):
                        if a:
                                client.upload(charname,source='local',destination_path="hun/"+TEXT.data[0]['filename']+".wav",file=a,overwrite='true')
                                st.toast("✅ Sikeres feltöltés")
                        else: 
                                st.toast("❌ Nincs feltölthető hanganyag")
            else: 
                st.warning('⚠️ Még nem került karakter hozzárendelésre ⚠️')
else:
    st.error("Nem vagy bejelentkezve!")
