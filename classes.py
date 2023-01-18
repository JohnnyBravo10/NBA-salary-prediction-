import streamlit.components.v1 as components
import requests
import streamlit as st

class Number:
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
            
    def component(self):
        return components.html(self.text, height = 500, scrolling=True)

class Player:
    def __init__(self, name, surname, salary_asked, salary_predicted, age, w, min_played, fgm, fga, ftm, fta, oreb, dreb, ast, tov, stl, blk, pf, dur):
        self.name = name
        self.surname = surname
        self.salary_asked = salary_asked
        self.salary_predicted = salary_predicted
        self.age = age
        self.w = w
        self.min_played = min_played
        self.fgm = fgm
        self.fga = fga
        self.ftm = ftm
        self.fta = fta
        self.oreb = oreb
        self.dreb = dreb
        self.ast = ast
        self.tov = tov
        self.stl = stl
        self.blk = blk
        self.pf = pf
        self.dur = dur
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getSalaryAsked(self):
        return self.salary_asked
    
    def getSalaryPredicted(self):
        return self.salary_predicted

class Text:
    def __init__(self, titleType, text, align):
        self.titleType = titleType
        self.text = text
        self.align = align
        
    def displayEntity(self):
        content = '''<%s style="text-align: %s;">%s</%s>''' % (self.titleType, self.align, self.text, self.titleType)
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
        
    def displayContact(self):
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
    