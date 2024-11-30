import streamlit as st
import pandas as pd
import numpy as np
from st_login_form import *



st.logo(image="dsr.png",icon_image="icon.png",size='large')

pg = st.navigation([
        st.Page("home.py", title="Főoldal"), 
        st.Page("user.py", title="Felhasználó")
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
                        else:
                                st.success("Welcome guest")
        else:
                        st.error("Nem vagy bejelentkezve!")
        