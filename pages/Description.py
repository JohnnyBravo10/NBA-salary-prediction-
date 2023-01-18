import streamlit as st
import classes as cl

def setInitialPageConf():
    st.set_page_config(
        page_title="NBA Salary Predictor APP",
        page_icon="🏀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    st.markdown('<style>' + open('C:/Users/pelli/Documents/Exam_Project_224MI/style.css').read() + '</style>', unsafe_allow_html=True)

setInitialPageConf()



