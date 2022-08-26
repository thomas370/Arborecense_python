from asyncio.windows_events import NULL
from importlib.metadata import files
import sys
import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


def fichierindex():
    if type.current() == 0:
        os.mkdir(entree0.get()), os.chdir(entree0.get()), os.mkdir("assets"),
        os.chdir("assets"),  # On se place dans le dossier assets
        os.mkdir("images"),  # On crée le dossier images
        os.mkdir("css"),
        os.mkdir("js"),
        os.chdir("css"),  # On se place dans le dossier css
        open("style.css", "w+"),  # On crée le fichier style.css
        os.chdir(".."),  # On se place dans le dossier assets
        os.chdir("js"),  # On se place dans le dossier js
        open('script.js', 'w+'),
        os.chdir("../.."),
        fileshtml = open("index.html", "w+")
        fileshtml.write("<!DOCTYPE html>\n<html lang=\"en\">\n\t<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<link rel=\"stylesheet\" href=\"assets/css/style.css\">\n")

        if btn3.get() == 1:
            fileshtml.write("\t<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css\" integrity=\"sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\"/> \n")

        if btn1.get() == 1:
            fileshtml.write("\t<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor\" crossorigin=\"anonymous\">\n")
        fileshtml.write("\t\t<title>" + str(entree1.get()) + "</title>\n\t</head>\n\n\t<body>\n\t\t<section>\n\t\t\t<h2>" + str(
            entree1.get()) + "</h2>\n\t\t\t<p>c'est un paragraphe</p>\n\t\t</section>\n\n\t<script src=\"assets/js/script.js\"></script>\n")

        if btn2.get() == 1:
            fileshtml.write("\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js\" integrity=\"sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\"></script>\n")
        fileshtml.write("\t</body>\n</html>")
        fileshtml.close()
        os.system("code .")

    elif type.current() == 1:
        os.mkdir(entree0.get()), os.chdir(entree0.get()), os.mkdir("assets"),
        os.chdir("assets"),  # On se place dans le dossier assets
        os.mkdir("images"),  # On crée le dossier images
        os.mkdir("css"),
        os.mkdir("js"),
        os.chdir("css"),  # On se place dans le dossier css
        open("style.css", "w+"),  # On crée le fichier style.css
        os.chdir(".."),  # On se place dans le dossier assets
        os.chdir("js"),  # On se place dans le dossier js
        open('script.js', 'w+'),
        os.chdir("../..")
        open('index.php', 'w+'),
        fileshtml = open("index.php", "w+")
        fileshtml.write("<?php \n?>")

        if btn4.get() == 1:
            os.mkdir("controllers")
            os.mkdir("models")
            os.mkdir("views")
            os.chdir("controllers")
            open("Controller_test.php", "w+")
            os.chdir("..")
            os.chdir("models")
            open("Model_test.php", "w+")
            os.chdir(".."),
            os.chdir("views")
            open("View_test.php", "w+")
            os.chdir(".."),
        fileshtml.close()
        os.system("code .")

    elif type.current() == 2:
        os.system("iwr -useb get.scoop.sh | iex")
        os.system("scoop install symfony-cli")
        os.system("scoop update symfony-cli")
        os.system("composer create-project symfony/website-skeleton " + str(entree1.get()))
        os.chdir(str(entree1.get()))
        os.system("symfony serve -d")
        os.system("code .")

    elif type.current() == 3:
        os.mkdir(entree0.get()), os.chdir(entree0.get())
        open('script.py', 'w+'),
        os.system("code .")
        
        
    elif type.current() == 4:
        os.system("npm install -g @vue/cli")#a revoir pour installer les packages
        os.system("vue create " + str(entree1.get()))


    elif type.current() == 5:
        os.system("npx create-react-app" + str(entree1.get()))#a tester
        os.chdir(str(entree1.get()))
        os.system("npm start")
        os.system("code .")
    return None

   


def modifaffichage(event):
    a = type.get()
    if a == "html":
        cbtn1.pack()
        cbtn2.pack()
        cbtn3.pack()
        cbtn4.pack_forget()
        return
    elif a == "php":
        cbtn1.pack_forget()
        cbtn2.pack_forget()
        cbtn3.pack_forget()
        cbtn4.pack()
        return
    elif a == "symfony-project":
        cbtn1.pack_forget()
        cbtn2.pack_forget()
        cbtn3.pack_forget()
        cbtn4.pack_forget()
        return
    elif a == "python":
        cbtn1.pack_forget()
        cbtn2.pack_forget()
        cbtn3.pack_forget()
        cbtn4.pack_forget()
        return
    return


fenetre = Tk()
# Création d'un label pour le nom du projet
label0 = Label(fenetre, text="Entrez le nom du projet: ")
value = StringVar()
value.set("name_projet")
entree0 = Entry(fenetre, width=50)


# Création d'un label pour le titre du site
label1 = Label(fenetre, text="Entrez le titre du site: ")
value = StringVar()
value.set("titre_site")
entree1 = Entry(fenetre, width=50)

# Création d'un label pour le nom du fichier
label2 = Label(fenetre, text="Entrez le type de fichier (html/php): ")
selection = StringVar()
type = ttk.Combobox(fenetre, values=["html", "php", "symfony-project", "python", "vue-project", "react-project"], textvariable=selection)

btn1 = IntVar()
btn2 = IntVar()
btn3 = IntVar()
btn4 = IntVar()

label3 = Label(fenetre, text="Selectionner les outils: ")

cbtn1 = Checkbutton(fenetre, text="Bootstrap", variable=btn1, )
cbtn2 = Checkbutton(fenetre, text="Jquery", variable=btn2)
cbtn3 = Checkbutton(fenetre, text="Fontawesome", variable=btn3)
cbtn4 = Checkbutton(fenetre, text="MVC", variable=btn4)

type.bind('<<ComboboxSelected>>', modifaffichage)


label0.pack()
entree0.pack()

label1.pack()
entree1.pack()

label2.pack()
type.pack()

label3.pack()


#

bouton = Button(fenetre, text="Valider",background="light green",command=lambda: (fichierindex()))
bouton.pack(side=BOTTOM)

fenetre.mainloop()
