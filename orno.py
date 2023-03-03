from asyncio.windows_events import NULL
from fileinput import close
from importlib.metadata import files
import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from keyboard import *

def fichierindex():
    a = type.get()
    if a == "symfony-project":
        os.system("symfony new " + entree0.get())
        os.chdir(entree0.get())
        os.system("composer require symfony/webpack-encore-bundle")
        os.system("yarn install")

    elif a == "vue-project":
        os.system("vue create " + entree0.get())
        #faire une pause pour que le terminal puisse créer le projet 
        os.chdir(entree0.get())
        os.system("yarn install")
        os.system("yarn add @symfony/webpack-encore --dev")

    elif a == "react-project":
        os.system("npx create-react-app " + entree0.get())
        os.chdir(entree0.get())
        os.system("yarn install")
        os.system("yarn add @symfony/webpack-encore --dev")

    elif a == "bot-discord":
        os.system("git clone https://github.com/DamienFoulon/obot.git")
        os.chdir("obot")
        os.system("npm install")

    elif a == "MERN":
        os.mkdir("client")
        os.chdir("client")
        os.system("npx create-react-app " + entree0.get())
        os.chdir(entree0.get())
        os.system("npm init -y")
        os.chdir("..")
        os.mkdir("server")
        os.chdir("server")
        os.system("npm init -y")
        os.system("npm install express cors mongoose dotenv")
        os.system("npm install -D nodemon")
        os.chdir("..")

    elif a == "react-symfony":
        os.system("symfony new " + entree0.get())
        os.chdir(entree0.get())
        os.system("composer require symfony/webpack-encore-bundle")
        os.system("yarn install")
        os.system("yarn add @symfony/webpack-encore --dev")
        os.system("npx create-react-app assets")
        os.chdir("assets")
        os.system("yarn install")
         #si sass est coché alors on installe sass 
        if btn1.get() == 1:
            os.system("yarn add sass")
            os.chdir("..")
        return


def modifaffichage(event):
    a = type.get()
    if a == "symfony-project":
        cbtn1.pack()
        cbtn2.pack()
        cbtn3.pack()
        cbtn4.pack()
        return
    elif a == "vue-project":
        cbtn1.pack()
        cbtn2.pack()
        cbtn3.pack()
        cbtn4.pack()
        return
    elif a == "react-project":
        cbtn1.pack()
        cbtn2.pack()
        cbtn3.pack()
        cbtn4.pack()
        return
    elif a == "bot-discord":
        cbtn1.pack_forget()
        cbtn2.pack_forget()
        cbtn3.pack_forget()
        cbtn4.pack_forget()
    elif a == "MERN":
        cbtn1.pack()
        cbtn2.pack_forget()
        cbtn3.pack_forget()
        cbtn4.pack_forget()
    elif a == "react-symfony":
        cbtn1.pack()
        cbtn2.pack()
        cbtn3.pack()
        cbtn4.pack()
        return
    return


fenetre = Tk()
# Création d'un label pour le nom du projet
label0 = Label(fenetre, text="Entrez le nom du projet: ")
value = StringVar()
value.set("name_projet")
entree0 = Entry(fenetre, width=30)

# Création d'un label pour le nom du fichier
label2 = Label(fenetre, text="Entrez le type de projet: ")
selection = StringVar()
type = ttk.Combobox(fenetre, values=["symfony-project", "vue-project", "react-project", "bot-discord", "MERN", "react-symfony"], textvariable=selection)

btn1 = IntVar()
btn2 = IntVar()
btn3 = IntVar()
btn4 = IntVar()

label3 = Label(fenetre, text="Selectionner les outils: ")

cbtn1 = Checkbutton(fenetre, text="SASS", variable=btn1, )

label58 = Label(fenetre, text="quelle type de base de donnée voulez vous utiliser:")

cbtn2 = Checkbutton(fenetre, text="MYSQL", variable=btn2, )
cbtn3 = Checkbutton(fenetre, text="MONGODB", variable=btn3, )
cbtn4 = Checkbutton(fenetre, text="POSTGRESQL", variable=btn4, )

type.bind('<<ComboboxSelected>>', modifaffichage)


label0.pack()
entree0.pack()

label2.pack()
type.pack()

label3.pack()

bouton = Button(fenetre, text="Valider",background="light green",command=lambda: (fichierindex()))
bouton.pack(side=BOTTOM)

fenetre.mainloop()
