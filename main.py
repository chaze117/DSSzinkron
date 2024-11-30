import streamlit as st
import pandas as pd
import numpy as np



st.logo(image="dsr.png",icon_image="icon.png",size='large')

pg = st.navigation([
        st.Page("home.py", title="Főoldal"), 
        #st.Page("main.py", title="Create your account")
        ])
pg.run()