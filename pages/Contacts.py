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

contacts = cl.ContactContainer() #container for Contacts Page

title = cl.Text("h1", "Team Project", "center")
title.setMargins("0px", "100px", "0px", "0px")
contacts.addItem(title)

contacts.displayEntity()

urlProfilePicture = "https://avatars.githubusercontent.com/u/115782494?v=4"
name_surname = "Giovanni Zanin"
occupation = "Student of <b>University of Trieste</b>"
course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
github_link = "https://github.com/JohnnyBravo10"
contact1 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link)

urlProfilePicture = "https://avatars.githubusercontent.com/u/67149530?v=4"
name_surname = "Federico Pellizzaro"
occupation = "Student of <b>University of Trieste</b>"
course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
github_link = "https://github.com/Fedrosauro"
contact2 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link)

contact_list = [contact1, contact2]
contacts.displayColumns(2, "large", contact_list)

    


  
        






