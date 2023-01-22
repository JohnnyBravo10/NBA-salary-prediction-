import streamlit.components.v1 as components
import requests
import streamlit as st
import ML_functions as MLF
import time
import random as rand
import urllib3 

def setInitialPageConf():
    st.set_page_config(
        page_title="NBA Salary Predictor APP",
        page_icon="🏀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    http = urllib3.PoolManager()
    st.markdown('<style>' + http.request('GET','https://raw.githubusercontent.com/Fedrosauro/NBA-salary-prediction-/main/style.css').data.decode('utf-8') + '</style>', unsafe_allow_html=True)

class Container:
    def __init__(self):
        self.internalList = []
        
    def addItem(self, item):
        self.internalList.append(item)
        
    def displayEntity(self):
        for item in self.internalList:
            st.markdown(item.displayEntity(), unsafe_allow_html=True)
        self.internalList = []

class MainPageContainer(Container):
    def __init__(self):
        super().__init__()
        
    def diplayMainProcess(self):
        mainProcess = MainProcess()
        mainProcess.displayEntity()
        
    def displayColumns(self, n, col_gap, items_list, use_markdown):
        cols = []
        if type(n) == list:
            cols = st.columns(n, gap=col_gap)
        else:
            cols = ["col" + str(x) for x in range(n)]
            cols = st.columns(n, gap=col_gap)
        i = 0
        
        for column in cols:
            if use_markdown:
                with column:
                    st.markdown(items_list[i].displayEntity(), unsafe_allow_html=True)
            else:
                with column:
                    items_list[i].displayEntity()
            i += 1

class MainProcess:
    def displayEntity(self):
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
        
        label_list = [labels1, labels2, labels3]
        
        glossary = Glossary(label_list)
        glossary.displayEntity()
                  
        salary_predicted = None
        my_list = [age, w, l, min_played, fgm, fga, _3pm, _3pa, ftm, fta, oreb, dreb, ast, tov, stl, blk, pf, plus_min, dur, salary_asked]
        
        valueChecker = ValuesChecker()
        
        if submit:
            if valueChecker.inputChecker(my_list):
                if int(age) > 0 and int(w) < 98 and int(fgm) < int(fga) and int(ftm) < int(fta) and int(_3pm) < int(_3pa) and int(dur) > 0: 
                    inputs = [[int(age), int(w), int(l), int(min_played), int(fgm), int(fga), int(_3pm), int(_3pa), int(ftm), int(fta), int(oreb), int(dreb), int(ast), int(tov), int(stl), int(blk), int(pf), int(plus_min), int(dur)]]
                                
                    salary_predicted = Result(int(MLF.prediction(inputs)))
                            
                    deltaValue = Result(salary_predicted.getN() - int(salary_asked))
                    
                    player = Player(name, surname, int(salary_asked), salary_predicted.getN())
                    
                    if "my_list" not in st.session_state:
                        st.session_state["my_list"] = []
                        st.session_state["my_list"].append(player)
                    else:
                        st.session_state["my_list"].append(player)
                else:
                    st.error("Some of the given inputs are not valid", icon="🔥")
            else:
                st.error("Some of the given inputs are not valid", icon="🔥")
        
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

class ColumnsBuilder:
    def __init__(self, col_name):
        self.col_name = col_name
        
    def displayEntity(self):
        if "my_list" in st.session_state:
            st.markdown("**" + self.col_name + "**")
            if self.col_name == "Player Name":
                for NBA_player in st.session_state["my_list"]:
                    st.markdown(NBA_player.getName())
                
            elif self.col_name == "Player Surname":
                for NBA_player in st.session_state["my_list"]:
                    st.markdown(NBA_player.getSurname())
                    
            elif self.col_name == "Salary Asked":
                for NBA_player in st.session_state["my_list"]:
                    price = Result(NBA_player.getSalaryAsked())
                    st.markdown(str(price.getFormattedN()) + " $")
                    
            elif self.col_name == "Salary Predicted":
                for NBA_player in st.session_state["my_list"]:
                    price = Result(NBA_player.getSalaryPredicted())
                    if NBA_player.getSalaryAsked() > NBA_player.getSalaryPredicted():
                        st.markdown(":red[" + price.getFormattedN() + " $]")
                    else:
                        st.markdown(":green[" + price.getFormattedN() + " $]")
 
class Glossary:
    def __init__(self, label_list):
        self.label_list = label_list
    
    def displayEntity(self):
        with st.expander("Glossary"):
            col1, col2, col3 = st.columns(3)

            with col1:
                for label in self.label_list[0]:
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
                for label in self.label_list[1]:
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
                for label in self.label_list[2]:
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
        

class ValuesChecker:
    def notANumber(self, item):
        return not item.isnumeric() or item[0] == '0'
    
    def inputChecker(self, my_list):
        result = True
        for item in my_list:
            if item == '' or self.notANumber(item):
                print("daads")
                result = False
                break
        
        return result
    
class ContactContainer(Container):
    def __init__(self):
        super().__init__()
        
    def displayColumns(self, n, col_gap, contact_list):
        cols = ["col" + str(x) for x in range(n)]
        cols = st.columns(n, gap=col_gap)
        i = 0
        for column in cols:
            with column:
                contact_list[i].displayEntity()
                i += 1

class DescriptionContainer(Container):
    def __init__(self):
        super().__init__()

class Result:
    def __init__(self, n):
        self.n = n
        n_copy = '{:,}'.format(n)
        self.nformatted = ""
        for c in n_copy:
            if c == ',':
                self.nformatted += "."
            else:
                self.nformatted += c
                
    def getN(self):
        return self.n
    
    def getFormattedN(self):
        return self.nformatted

class Tweets:
    def __init__(self, s, embed_str=False):
        if not embed_str:
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s
            
    def displayEntity(self):
        components.html(self.text, height = 500, scrolling=True)

class Player:
    def __init__(self, name, surname, salary_asked, salary_predicted):
        self.name = name
        self.surname = surname
        self.salary_asked = salary_asked
        self.salary_predicted = salary_predicted
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getSalaryAsked(self):
        return self.salary_asked
    
    def getSalaryPredicted(self):
        return self.salary_predicted

class Text:
    def __init__(self, textType, text, align):
        self.textType = textType
        self.text = text
        self.align = align
        self.color = None
        self.fontSize = None
        self.mTop= None
        self.mBottom = None
        self.mLeft = None
        self.mRight = None
        
    def setColor(self, color):
        self.color = color
        
    def setFontSize(self, fontSize):
        self.fontSize = fontSize
        
    def setMargins(self, top, bottom, left, right):
        self.mTop= top
        self.mBottom = bottom
        self.mLeft = left
        self.mRight = right
        
    def displayEntity(self):
        content = '''<%s style="text-align:%s;''' % (self.textType, self.align)
        if self.color is not None:
            content += '''color:%s;''' % (self.color)
        if self.fontSize is not None:
            content += '''font-size:%s;''' % (self.fontSize)
        if self.mTop is not None:
            content += '''margin-top:%s;''' % (self.mTop)
        if self.mBottom is not None:
            content += '''margin-bottom:%s;''' % (self.mBottom)
        if self.mLeft is not None:
            content += '''margin-left:%s;''' % (self.mLeft)
        if self.mRight is not None:
            content += '''margin-right:%s;''' % (self.mRight)
        
        content += '''">%s</%s>''' % (self.text, self.textType)
        return content
    
    
class Image:
    def __init__(self, path, width, curve):
        self.path = path
        self.width = width
        self.curve = ""
        if curve is True:
            self.curve = "50%"
        else:
            self.curve = "0%"
        
    def displayEntity(self):
        content = '''<img src="%s" style="display: block; margin-left: auto; margin-right: auto; width: %s; border-radius: %s">''' % (self.path, self.width, self.curve)
        return content
    
class Contact:
    def __init__(self, urlProfilePicture, name_surname, occupation, course, github_link):
        self.urlProfilePicture = urlProfilePicture
        self.name_surname = name_surname
        self.occupation = occupation
        self.course = course
        self.github_link = github_link
        
    def displayEntity(self):
        image1 = Image(self.urlProfilePicture, "17%", True)
        st.markdown(image1.displayEntity(), unsafe_allow_html = True)
        
        NS = Text("h3", self.name_surname, "center")
        st.markdown(NS.displayEntity(), unsafe_allow_html = True)
        
        occupation = Text("p", self.occupation, "center")
        st.markdown(occupation.displayEntity(), unsafe_allow_html = True)
        
        course = Text("p", self.course, "center")
        st.markdown(course.displayEntity(), unsafe_allow_html = True)
        
        gitHub_link = "<a href='" + self.github_link + "' style='text-decoration: none; color:lightblue'>GitHub Page</a>"
        linkText1 = Text("p", gitHub_link, "center")
        st.markdown(linkText1.displayEntity(), unsafe_allow_html = True)
    