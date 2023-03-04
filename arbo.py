import os
import time
import tkinter as tk
from tkinter import ttk
import keyboard
import subprocess


def create_symfony_project(project_name):
    try:
        php_version = subprocess.check_output(['php', '-v'])
        print(f"PHP est installé (version {php_version.decode().splitlines()[0]})")
    except OSError:
        print("PHP n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install php")
            print("PHP est installé")
        else:
            print("Installation annulée")
            return

    try:
        composer_version = subprocess.check_output(['composer'])
        print(f"Composer est installé (version {composer_version.decode().splitlines()[0]})")
    except OSError:
        print("Composer n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("php -r \"copy('https://getcomposer.org/installer', 'composer-setup.php');\"")
            os.system("php composer-setup.php")
            os.system("php -r \"unlink('composer-setup.php');\"")
            print("Composer est installé")
        else:
            print("Installation annulée")
            return

    try:
        symfony_version = subprocess.check_output(['symfony', '-V'])
        print(f"Symfony est installé (version {symfony_version.decode().splitlines()[0]})")
    except OSError:
        print("Symfony n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("scoop install symfony-cli")
            print("Symfony est installé")
    else:
        print("Tout est installé")
        os.system("symfony update")
        os.system("symfony new " + project_name)
        os.chdir(project_name)
        os.system("composer require symfony/webpack-encore-bundle")
        os.system("yarn install")
# vuejs pas ok
def create_vue_project(project_name, install_sass = 0):
    try:
        node_version = subprocess.check_output(['node', '-v'])
        print(f"Node est installé (version {node_version.decode().splitlines()[0]})")
    except OSError:
        print("Node n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install nodejs")
            print("Node est installé")
    else:
        os.system("npm install -g @vue/cli")
        os.system("vue create " + project_name)
        time.sleep(10)
        keyboard.press_and_release("enter")
        os.chdir(project_name)
        os.system("yarn install")
        if install_sass:
            os.system("yarn add sass")

#React ok
def create_react_project(project_name, install_sass = 0):
    try:
        node_version = subprocess.check_output(['node', '-v'])
        print(f"Node est installé (version {node_version.decode().splitlines()[0]})")
    except OSError:
        print("Node n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install nodejs")
            print("Node est installé")
    else:
        os.system("npx create-react-app " + project_name)
        os.chdir(project_name)
        os.system("yarn install")
        os.chdir("src")
        os.mkdir("components")
        if install_sass:
            os.system("yarn add sass")

#Bot Discord ok
def create_bot_discord():
    try:
        node_version = subprocess.check_output(['node', '-v'])
        print(f"Node est installé (version {node_version.decode().splitlines()[0]})")
    except OSError:
        print("Node n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install nodejs")
            print("Node est installé")
    else:
        os.system("git clone https://github.com/DamienFoulon/obot.git")
        os.chdir("obot")
        os.system("npm install")

#MERN ok
def create_mern_stack(project_name, install_sass = 0):
    try:
        node_version = subprocess.check_output(['node', '-v'])
        print(f"Node est installé (version {node_version.decode().splitlines()[0]})")
    except OSError:
        print("Node n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install nodejs")
            print("Node est installé")
    else:
        os.system("mkdir " + project_name)
        os.chdir(project_name)
        os.mkdir("server")
        os.chdir("server")
        os.system("npm install express cors mongoose dotenv")
        os.system("npm init -y")
        os.system("npm install -D nodemon")
        os.chdir("..")
        os.system("npx create-react-app client")
        os.chdir("client")
        os.chdir("src")
        os.mkdir("components")
        os.mkdir("pages")
        os.mkdir("styles")
        os.chdir("..")
        if install_sass == 1:
            os.chdir("client")
            os.system("yarn add sass")
            os.chdir("..")

#React Symfony ok
def create_react_symfony_project(project_name, install_sass = 0):
    try:
        php_version = subprocess.check_output(['php', '-v'])
        print(f"PHP est installé (version {php_version.decode().splitlines()[0]})")
    except OSError:
        print("PHP n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system(
                "powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install php")
            print("PHP est installé")
        else:
            print("Installation annulée")
            return

    try:
        composer_version = subprocess.check_output(['composer', '-V'])
        print(f"Composer est installé (version {composer_version.decode().splitlines()[0]})")
    except OSError:
        print("Composer n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("php -r \"copy('https://getcomposer.org/installer', 'composer-setup.php');\"")
            os.system("php composer-setup.php")
            os.system("php -r \"unlink('composer-setup.php');\"")
            print("Composer est installé")
        else:
            print("Installation annulée")
            return

    try:
        symfony_version = subprocess.check_output(['symfony', '-V'])
        print(f"Symfony est installé (version {symfony_version.decode().splitlines()[0]})")
    except OSError:
        print("Symfony n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("scoop install symfony-cli")
            print("Symfony est installé")
    else:
        os.system("symfony self-update")
        os.system("symfony new " + project_name)
        os.chdir(project_name)
        os.system("composer require symfony/webpack-encore-bundle")
        os.system("yarn install")
        os.system("yarn add @symfony/webpack-encore --dev")
        os.system("npx create-react-app")
        os.system("yarn install")
        os.chdir("assets")
        os.mkdir("js")
        os.chdir("js")
        os.mkdir("components")
        os.chdir("..")
        os.chdir("..")
        if install_sass == 1:
            os.system("yarn add sass")


def create_project():
    project_name = entree0.get().strip()
    project_type = type.get().strip()
    if not project_name:
        # Si le nom du projet n'est pas saisi, afficher une erreur
        error_label.config(text="Veuillez saisir un nom de projet.")
        return

    if project_type == "symfony-project":
        create_symfony_project(project_name)
        cbtn1.grid_forget()

    elif project_type == "vue-project":
        create_vue_project(project_name)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.pack_forget()

    elif project_type == "react-project":
        create_react_project(project_name)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.pack_forget()

    elif project_type == "bot-discord":
        create_bot_discord()
        cbtn1.grid_forget()

    elif project_type == "MERN":
        create_mern_stack(project_name)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()

    elif project_type == "react-symfony":
        create_react_symfony_project(project_name)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
    success_label.config(text="Le projet {} a été créé avec succès!".format(project_name))


def update_tool_options(event):
    project_type = type.get().strip()
    if project_type == "symfony-project":
        cbtn1.grid_forget()
    elif project_type == "react-symfony":
        cbtn1.grid(row=9, column=0)
    elif project_type == "vue-project":
        cbtn1.grid(row=9, column=0)
    elif project_type == "react-project":
        cbtn1.grid(row=9, column=0)
    elif project_type == "MERN":
        cbtn1.grid(row=9, column=0)
    elif project_type == "react-symfony":
        cbtn1.grid(row=9, column=0)
    else:
        cbtn1.grid_forget()




# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Création de projet")
fenetre.configure(background="#03224c")
fenetre.geometry("500x500")

# Création d'un label pour le nom du projet
label0 = tk.Label(fenetre, background="#03224c", foreground="White", text="Entrez le nom du projet: ")
label0.grid(row=0, column=0)

# Création d'une zone de saisie pour le nom du projet
entree0 = tk.Entry(fenetre, width=30)
entree0.grid(row=0, column=1)

# Création d'un label pour le type de projet
label1 = tk.Label(fenetre, background="#03224c", foreground="White", text="Choisissez le type de projet: ")
label1.grid(row=3, column=0)

# Création d'une liste déroulante pour le type de projet
type = ttk.Combobox(fenetre, values=["symfony-project", "vue-project", "react-project", "bot-discord", "MERN", "react-symfony"])
type.current(0)

type.bind("<<ComboboxSelected>>", update_tool_options)
type.grid(row=3, column=1)

# Création d'un label pour afficher les erreurs
error_label = tk.Label(fenetre, background="#03224c", foreground="red")
error_label.grid(row=2, column=0, columnspan=2)

# Création d'un label pour afficher les succès
success_label = tk.Label(fenetre, background="#03224c", foreground="green")
success_label.grid(row=6, column=0, columnspan=2)

# Création d'un bouton pour installer sass
btn1 = tk.IntVar()
cbtn1 = tk.Checkbutton(fenetre, text="Installer sass", variable=btn1)

# Création d'un bouton pour créer le projet
bouton = tk.Button(fenetre, text="Créer le projet", command=create_project)
bouton.grid(row=10, column=1)

# Lancement de la boucle principale
fenetre.mainloop()

