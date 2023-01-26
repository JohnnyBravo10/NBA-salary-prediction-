#import libraries and modules
import streamlit as st
import classes as cl

cl.setInitialPageConf() #setting initial configuration of the webpage

mainPageCont = cl.MainPageContainer() #creation of the MainPage Container that will contain all the other elements

image1 = cl.Image("https://raw.githubusercontent.com/Fedrosauro/Images/main/nba-logo-transparent.png", "16%", False)
title = cl.Text("h1", "<br>Salary Predictor", "center")
userInput = cl.Text("h3", "User Input", "center")

mainPageCont.addItem(image1)
mainPageCont.addItem(title)
mainPageCont.addItem(userInput)
mainPageCont.displayEntity() #display of the image and title of the webpage

mainPageCont.diplayMainProcess() #displaying the MainProcess of the web application

st.markdown("---")

#here we start building the final section of the page with tweets interaction and
#a history of "Recent Searches" made by the user

#building titles of the sections
twitterSectionTitleNBAStats = cl.Text("h3", "NBA stats Tweets", "center")
twitterSectionTitleNBA = cl.Text("h3", "NBA Tweets", "center")
recentSearches = cl.Text("h3", "Recent Searches", "center")
my_list = [twitterSectionTitleNBAStats, twitterSectionTitleNBA, recentSearches]
mainPageCont.displayColumns([4,4,8], "small", my_list, True)

#building the columns of the sections
tweet1 = cl.Tweets("https://twitter.com/nbastats?&theme=dark&maxheight=480")    
tweet2 = cl.Tweets("https://twitter.com/NBA?&theme=dark&maxheight=480")       
column1 = cl.ColumnsBuilder("Player Name")
column2 = cl.ColumnsBuilder("Player Surname")
column3 = cl.ColumnsBuilder("Salary Asked")
column4 = cl.ColumnsBuilder("Prediction")
my_list = [tweet1, tweet2, column1, column2, column3, column4]
mainPageCont.displayColumns([5,5,2,2,2,2], "small", my_list, False) #display columns

#footer section 
st.markdown("---")

footer = cl.Text("footer", "Project developed for university exam. Images used in this project do not belong to me. Languages used: Python, CSS, HTML <a href='https://www.freepik.com/free-vector/3d-colorful-solid-waveform_19445097.htm'>Image by GarryKillian</a> on Freepik", "center")
footer.setColor("#828A95")
footer.setFontSize("14px")
st.markdown(footer.displayEntity(), unsafe_allow_html=True)

st.markdown("---")

       