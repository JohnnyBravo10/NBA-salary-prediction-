#import libraries
import classes as cl

cl.setInitialPageConf() #setting initial page configurations

desc = cl.DescriptionContainer() #Creating the container for the Description Page

#creating, adding and displaying items in the web application
title = cl.Text("h1", "Project Description", "center")
title.setMargins("0px", "100px", "0px", "0px")
desc.addItem(title)

content ='''This web application is a <b>University Project for the course 224MI</b>. In particular
this web application is a tool that, with the help of <b><i>Machine Learning</i></b>, helps to decide which
should be the <u>salary price</u> of a NBA Player. <br><br>'''

text = cl.Text("p", content, "justify")
text.setMargins("20px", "0px", "200px", "200px")
desc.addItem(text)

content ='''The project Core is in the MainPage page, in which the user is asked to insert some values
(of the player) in order to make the salary prediction. After inserting those values the button <i>"Submit"</i> 
has to be clicked. After some seconds the user will be able to see the <b>salary predicted</b> for the player. <br><br>'''

text = cl.Text("p", content, "justify")
text.setMargins("0px", "0px", "200px", "200px")
desc.addItem(text)

content ='''In the MainPage page there are also 3 more sections, 2 of them are just for news entertainment, to see
the latest tweets about NBA player stats or NBA. The other section is a list to keep the data of the
player that has just been searched.'''

text = cl.Text("p", content, "justify")
text.setMargins("0px", "0px", "200px", "200px")
desc.addItem(text)

desc.displayEntity()





