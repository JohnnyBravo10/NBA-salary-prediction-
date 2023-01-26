#imports modules
import classes as cl

cl.setInitialPageConf() #setting up the page configurations

contacts = cl.ContactContainer() #creation of the Contact container for this page

#adding and displaying stuff inside of the page
title = cl.Text("h1", "Team Project", "center")
title.setMargins("0px", "160px", "0px", "0px")
contacts.addItem(title)

contacts.displayEntity()

urlProfilePicture = "https://avatars.githubusercontent.com/u/115782494?v=4"
name_surname = "Giovanni Zanin"
occupation = "Student of <b>University of Trieste</b>"
course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
github_link = "https://github.com/JohnnyBravo10"
contact1 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link) #contact 1 creation

urlProfilePicture = "https://avatars.githubusercontent.com/u/67149530?v=4"
name_surname = "Federico Pellizzaro"
occupation = "Student of <b>University of Trieste</b>"
course = "Course - <b>COMPUTER & ELECTRONIC ENGINEERING</b><br>Curr. <b>Informatica</b>"
github_link = "https://github.com/Fedrosauro"
contact2 = cl.Contact(urlProfilePicture, name_surname, occupation, course, github_link) #contact 2 creation

contact_list = [contact1, contact2]
contacts.displayColumns(2, "large", contact_list) #displaying contacts

    


  
        






