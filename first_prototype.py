import streamlit as st
import ML_functions as MLF
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("NBA Salary Predictor")

with st.form("my_form"):
    
   col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)
    
   with col1:
       age = st.text_input('AGE')
   with col2:
       w = st.text_input('WINS')
   with col3:
       min_layed = st.text_input('MIN')
   with col4:     
       fgm = st.text_input('FGM')
   with col5:    
       fga = st.text_input('FGA')
   with col6:     
       ftm = st.text_input('FTM')
   with col7:     
       fta = st.text_input('FTA')
   with col8:     
       oreb = st.text_input('OREB')
   with col9:    
       dreb = st.text_input('DREB')
   with col10:     
       ast = st.text_input('AST')
   with col11:     
       tov = st.text_input('TOV')
   with col12:    
       stl = st.text_input('STL')
   with col13:    
       blk = st.text_input('BLK')
   with col14:    
       pf = st.text_input('PF')
   with col15:   
       duration = st.text_input('DUR')
   
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("values submitted")
       a = [[int(age), int(w), int(min_layed), int(fgm), int(fga), int(ftm), int(fta), int(oreb), int(dreb), int(ast), int(tov), int(stl), int(blk), int(pf), int(duration)]]
       st.write(MLF.firstPrediction(a))
