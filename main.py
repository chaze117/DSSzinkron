import streamlit as st
import pandas as pd
import numpy as np
from st_login_form import *



pg = st.navigation([
        st.Page("dsr.py", title="Dark Souls Remastered"), 
        st.Page("translate.py", title="Fordítás"),
        #st.Page("test.py", title="Teszt")
        ])

pg.run()
with st.sidebar:
        client = login_form(
                title="Bejelentkezés",
                user_tablename="users",
                allow_guest=False,
                create_title=  ":material/add_circle: Regisztráció",
                login_title= ":material/login: Bejelentkezés",
                create_username_label="Felhasználónév",
                create_password_label="Jelszó",
                login_username_label="Felhasználónév",
                login_password_label="Jelszó",
                create_submit_label=":material/add_circle: Regisztál",
                login_submit_label=":material/login: Bejelentkezés",
                login_error_message = ":material/lock: Hibás felhasználónév vagy jelszó!",
                password_constraint_check_fail_message= """:material/warning: A jelszónak legalább 8 karakternek kell lennie, 
                                                        tartalmaznia kell legalább egy nagy betűt, 
                                                        legalább egy kisbetűt, egy számot és egy speciális karaktert (`@$!%*?&_^#- `).""",
                constrain_password=False,
    
        )
        if st.session_state["authenticated"]:
                        if st.session_state["username"]:
                                st.success(f"Üdvözlet {st.session_state['username']}!")
                                with st.expander("Profilkép"):
                                        uploaded_file = st.file_uploader("pp",label_visibility='collapsed')
                                        if uploaded_file is not None:
                                                client.upload("profilepics",source='local',destination_path=st.session_state['username'],file=uploaded_file,overwrite='true')
                        else:
                                st.success("Welcome guest")
        else:
                        st.error("Nem vagy bejelentkezve!")
        st.warning("Az oldal átalakítás alatt egyes funkciók hibásan működhetnek!")
