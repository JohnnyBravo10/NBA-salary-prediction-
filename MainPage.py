import streamlit as st
import classes as cl
import ML_functions as MLF
import time
import random as rand

def setInitialPageConf():
    st.set_page_config(
        page_title="NBA Salary Predictor APP",
        page_icon="🏀",
        layout="wide",
    )
    st.markdown('<style>' + open('C:/Users/pelli/Documents/Exam_Project_224MI/style.css').read() + '</style>', unsafe_allow_html=True)

setInitialPageConf()

image1 = cl.Image("https://raw.githubusercontent.com/Fedrosauro/Images/main/nba-logo-transparent.png", "16%", False)
st.markdown(image1.displayEntity(), unsafe_allow_html = True)

title = cl.Text("h1", "Salary Predictor", "center")
st.markdown(title.displayEntity(), unsafe_allow_html = True)

userInput = cl.Text("h3", "User Input", "center")
st.markdown(userInput.displayEntity(), unsafe_allow_html = True)
    
with st.form("my_form"):
   col1, col2, col3 = st.columns(3)
   with col1:
       name = st.text_input("Player Name")
   with col2:
       surname = st.text_input("Player Surname")
   with col3:   
       salary_asked = st.text_input("Salary asked")
    
   col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19 = st.columns(19)
    
   with col1:
       age = st.text_input('AGE')
   with col2:
       w = st.text_input('WINS')
   with col3:
       l = st.text_input('LOSE')
   with col4:
       min_played = st.text_input('MIN')
   with col5:     
       fgm = st.text_input('FGM')
   with col6:    
       fga = st.text_input('FGA')     
   with col7:
       _3pm = st.text_input('3PM')
   with col8:
       _3pa = st.text_input('3PA')      
   with col9:     
       ftm = st.text_input('FTM')
   with col10:     
       fta = st.text_input('FTA')
   with col11:     
       oreb = st.text_input('OREB')
   with col12:    
       dreb = st.text_input('DREB')
   with col13:     
       ast = st.text_input('AST')
   with col14:     
       tov = st.text_input('TOV')
   with col15:    
       stl = st.text_input('STL')
   with col16:    
       blk = st.text_input('BLK')
   with col17:    
       pf = st.text_input('PF')
   with col18:
       plus_min = st.text_input('+/-') 
   with col19:   
       dur = st.text_input('DUR')
       
   submit = st.form_submit_button("Submit")

       
labels1 = ['AGE','W', 'L', 'MIN','FGM','FGA', '3PM']
labels2 = ['3PA', 'FTM','FTA','OREB','DREB','AST']
labels3 = ['TOV','STL','BLK','PF', '+/-', 'DUR']

with st.expander("Glossary"):
    col1, col2, col3 = st.columns(3)

    with col1:
        for label in labels1:
            with st.container():   
                st.markdown("##### " + label)
                if label == "AGE":  
                    st.markdown(">Player age")
                elif label == "W":
                    st.markdown(">Number of Wins (matches)")
                elif label == "L":
                    st.markdown(">Number of lose (matches)")
                elif label == "MIN":
                    st.markdown(">Number of minutes played")
                elif label == "FGM":
                    st.markdown(">Number of team's Field Goals Made")
                elif label == "FGA":
                    st.markdown(">Number of team's Field Goals Attempted")
                elif label == "3PM":
                    st.markdown(">Number of team's 3 Point Field Goals Made")
    
    with col2:
        for label in labels2:
            with st.container():   
                st.markdown("##### " + label)
                if label == "3PA":  
                    st.markdown(">Number of team's 3 Point Field Goals Attempted")
                elif label == "FTM":
                    st.markdown(">Number of team's Free Throws Made")
                elif label == "FTA":
                    st.markdown(">Number of Free Throws Attempted")
                elif label == "OREB":
                    st.markdown(">Number of Offensive Rebounds")
                elif label == "DREB":
                    st.markdown(">Number of feam's Defensive Rebounds")
                elif label == "AST":
                    st.markdown(">Number of Assists")
                    
    with col3:
        for label in labels3:
            with st.container():   
                st.markdown("##### " + label)
                if label == "TOV":
                    st.markdown(">Number of Turnovers")
                elif label == "STL":
                    st.markdown(">Number of team's Steals")
                elif label == "BLK":
                    st.markdown(">Number of Blocks")
                elif label == "PF":
                    st.markdown(">Number of Personal Fouls")
                elif label == "DUR":
                    st.markdown(">Duration of the contract")
                elif label == "+/-":
                    st.markdown(">The point differential when a player or team is on the floor")
          
salary_predicted = None

if submit: 
    inputs = [[int(age), int(w), int(l), int(min_played), int(fgm), int(fga), int(_3pm), int(_3pa), int(ftm), int(fta), int(oreb), int(dreb), int(ast), int(tov), int(stl), int(blk), int(pf), int(plus_min), int(dur)]]
    
    salary_predicted = cl.Number(int(MLF.prediction(inputs)))
            
    deltaValue = cl.Number(salary_predicted.getN() - int(salary_asked))
    
    player = cl.Player(name, surname, int(salary_asked), salary_predicted.getN(), age, w, min_played, fgm, fga, ftm, fta, oreb, dreb, ast, tov, stl, blk, pf, dur)
    
    if "my_list" not in st.session_state:
        st.session_state["my_list"] = []
        st.session_state["my_list"].append(player)
    else:
        st.session_state["my_list"].append(player)

if salary_predicted:
    with st.container():    
        my_bar = st.progress(0)
        time.sleep(0.3)    

        for percent_complete in range(100):
            r = rand.random()
            n = rand.randint(1, 50)
            time.sleep(r/n)
            my_bar.progress(percent_complete + 1)
            
        st.metric(label = "Predicted Salary", value=salary_predicted.getFormattedN(), delta=deltaValue.getFormattedN())
        

st.markdown("---")

col1, col2, col3= st.columns([4,4,8],gap="small")

with col1:
    twitterSectionTitleNBAStats = cl.Text("h3", "NBA stats Tweets", "center")
    st.markdown(twitterSectionTitleNBAStats.displayEntity(), unsafe_allow_html = True)
    
with col2:
    twitterSectionTitleNBA = cl.Text("h3", "NBA Tweets", "center")
    st.markdown(twitterSectionTitleNBA.displayEntity(), unsafe_allow_html = True)
    
with col3:
    recentSearches = cl.Text("h3", "Recent Searches", "center")
    st.markdown(recentSearches.displayEntity(), unsafe_allow_html = True)
    
col1, col2, col3, col4, col5 , col6= st.columns([4,4,2,2,2,2],gap="small")

with col1:
    tweets = cl.Tweets("https://twitter.com/nbastats?&theme=dark&maxheight=480").component()      

with col2:
    tweets = cl.Tweets("https://twitter.com/NBA?&theme=dark&&maxheight=480").component()         
    
with col3:
    if "my_list" in st.session_state:
        st.markdown("**Player Name**")
        for NBA_player in st.session_state["my_list"]:
            st.markdown(NBA_player.getName())
        
with col4:
    if "my_list" in st.session_state:
        st.markdown("**Player Surname**")
        for NBA_player in st.session_state["my_list"]:
            st.markdown(NBA_player.getSurname())
            
with col5:
    if "my_list" in st.session_state:
        st.markdown("**Salary Asked**")
        for NBA_player in st.session_state["my_list"]:
            price = cl.Number(NBA_player.getSalaryAsked())
            st.markdown(str(price.getFormattedN()) + " $")
        
with col6:
    if "my_list" in st.session_state:
        st.markdown("**Salary Predicted**")
        for NBA_player in st.session_state["my_list"]:
            price = cl.Number(NBA_player.getSalaryPredicted())
            if NBA_player.getSalaryAsked() > NBA_player.getSalaryPredicted():
                st.markdown(":red[" + price.getFormattedN() + " $]")
            else:
                st.markdown(":green[" + price.getFormattedN() + " $]")
       