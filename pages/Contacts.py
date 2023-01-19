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

title = cl.Text("h1", "Team Project", "center")
title.setMargins("0px", "100px", "0px", "0px")
st.markdown(title.displayEntity(), unsafe_allow_html = True)

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container():
        urlProfilePicture = "https://avatars.githubusercontent.com/u/115782494?v=4"
        name_surname = "Giovanni Zanin"
        occupation = "Student of <b>University of Trieste</b>"
        course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
        github_link = "https://github.com/JohnnyBravo10"
        
        contact1 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link)
        contact1.displayContact()
        
with col2:
    with st.container():
        urlProfilePicture = "https://avatars.githubusercontent.com/u/67149530?v=4"
        name_surname = "Federico Pellizzaro"
        occupation = "Student of <b>University of Trieste</b>"
        course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
        github_link = "https://github.com/Fedrosauro"
        
        contact2 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link)
        contact2.displayContact()
    
    


  
        






