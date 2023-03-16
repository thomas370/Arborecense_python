import os
import time
import tkinter as tk
import tkinter.ttk as ttk
import keyboard
import subprocess

def install_options_sass():
    os.chdir("src")
    os.mkdir("assets")
    os.chdir("assets")
    os.mkdir("scss")
    os.chdir("scss")
    main = open("main.scss", "w+")  # créer le fichier main.scss
    main.close()
    variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
    variables.close()
    responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
    responsive.close()
    os.system("yarn add sass")
    os.chdir("../../../")
    return

def testInstallNode():
    try:
        node_version = subprocess.check_output(['node', '-v'])
        print(
            f"Node est installé (version {node_version.decode().splitlines()[0]})")
    except OSError:
        print("Node n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system(
                "powershell.exe -Command \"Invoke-WebRequest -Uri https://get.scoop.sh -UseBasicParsing | Invoke-Expression\"")
            os.system("scoop install nodejs nvm")
            print("Node est installé")
        else:
            print("Installation annulée")
            return


def testInstallPHP():
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


def testInstallComposer():
    testInstallPHP()
    try:
        composer_version = subprocess.check_output(['composer --version'])
        print(
            f"Composer est installé (version {composer_version.decode().splitlines()[0]})")
    except OSError:
        print("Composer n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("php -r \"copy('https://getcomposer.org/installer', 'composer-setup.php');\"") #erreur php access denied (pas de solution erreur sur pc du taf ) 
            os.system("php composer-setup.php")
            os.system("php -r \"unlink('composer-setup.php');\"")
            print("Composer est installé")
        else:
            print("Installation annulée")
            return


def testInstallsymfony():
    testInstallComposer()
    try:
        symfony_version = subprocess.check_output(['symfony'])
        print(
            f"Symfony est installé (version {symfony_version.decode().splitlines()[0]})")
    except OSError:
        print("Symfony n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("scoop install symfony-cli")
            print("Symfony est installé")
        else:
            print("Installation annulée")
            return


def testInstallLaravel():
    testInstallComposer()
    try:
        laravel_version = subprocess.check_output(['laravel'])
        print(
            f"Laravel est installé (version {laravel_version.decode().splitlines()[0]})")
    except OSError:
        print("Laravel n'est pas installé, voulez-vous l'installer ?")
        answer = input("Entrez 'oui' ou 'non' : ")
        if answer.lower() in {'oui', 'o', 'yes', 'y'}:
            os.system("composer global require laravel/installer")
            print("Laravel est installé")
        else:
            print("Installation annulée")
            return

# Verifications technologies

# Symfony ok
def create_symfony_project(project_name):
    testInstallsymfony()
    print("Tout est installé")
    os.system("composer create-project symfony/website-skeleton" + " " + project_name)#executable a verifier 
    os.chdir(project_name)
    os.system("composer install")
    os.system("composer require symfony/webpack-encore-bundle")
    os.system("yarn install")

# vuejs pas ok

def create_vue_project(project_name, install_sass=0, routage=0):
    testInstallNode()
    os.system("npm install -g @vue/cli")
    os.system("vue create " + project_name)
    time.sleep(10)
    keyboard.press_and_release("enter")
    os.chdir(project_name)
    os.system("yarn install")
    if install_sass == 1:
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()

# React ok
def create_react_project(project_name, install_sass=0, routage=0, composants_menu=0):
    testInstallNode()
    os.system("npx create-react-app " + project_name)
    os.chdir(project_name)
    os.system("yarn install")
    os.chdir("src")
    os.mkdir("components")
    os.chdir("..")
    if install_sass == 1:
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()
    elif composants_menu == 1:
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("styles")
        os.chdir("styles")
        menustyles = open("Menu.css", "w+")
        menustyles.close()
    elif (composants_menu == 1) and (install_sass == 1):
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("scss")
        os.chdir("scss")
        main = open("main.scss", "w+")  # créer le fichier main.scss
        main.close()
        variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
        variables.close()
        responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
        responsive.close()
        menustyles = open("Menu.scss", "w+")
        menustyles.close()
        os.system("yarn add sass")

# Bot Discord ok
def create_bot_discord():
    testInstallNode()
    os.system("git clone https://github.com/DamienFoulon/obot.git")
    os.chdir("obot")
    os.system("npm install")

# MERN ok
def create_mern_stack(project_name, install_sass=0, routage=0, composants_menu=0):
    testInstallNode()
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
    os.mkdir("utils")
    os.chdir("utils")
    connexion = open("connexion.js", "w+")  # créer le fichier connexion.js
    connexion.close()
    os.mkdir("components")
    os.mkdir("pages")
    os.mkdir("styles")
    os.chdir("..")
    if install_sass == 1:
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()
    elif composants_menu == 1:
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("styles")
        os.chdir("styles")
        menustyles = open("Menu.css", "w+")
        menustyles.close()
    elif (composants_menu == 1) and (install_sass == 1):
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("scss")
        os.chdir("scss")
        main = open("main.scss", "w+")  # créer le fichier main.scss
        main.close()
        variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
        variables.close()
        responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
        responsive.close()
        menustyles = open("Menu.scss", "w+")
        menustyles.close()
        os.system("yarn add sass")


# React Symfony ok
def create_react_symfony_project(project_name, install_sass=0, routage=0, composants_menu=0):
    testInstallsymfony()
    os.system("composer create-project symfony/website-skeleton" + " " + project_name)#executable a verifier
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
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()
    elif composants_menu == 1:
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("styles")
        os.chdir("styles")
        menustyles = open("Menu.css", "w+")
        menustyles.close()
    elif (composants_menu == 1) and (install_sass == 1):
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("scss")
        os.chdir("scss")
        main = open("main.scss", "w+")  # créer le fichier main.scss
        main.close()
        variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
        variables.close()
        responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
        responsive.close()
        menustyles = open("Menu.scss", "w+")
        menustyles.close()
        os.system("yarn add sass")



# NextJS ok
# Intervention user pour la création du projet nextjs
def create_nextjs_project(project_name, install_sass=0, routage=0, composants_menu=0):
    testInstallNode()
    os.system("npx create-next-app " + project_name)
    os.chdir(project_name)
    os.system("yarn install")
    if install_sass == 1:
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()
    elif composants_menu == 1:
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("styles")
        os.chdir("styles")
        menustyles = open("Menu.css", "w+")
        menustyles.close()
    elif (composants_menu == 1) and (install_sass == 1):
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("scss")
        os.chdir("scss")
        main = open("main.scss", "w+")  # créer le fichier main.scss
        main.close()
        variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
        variables.close()
        responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
        responsive.close()
        menustyles = open("Menu.scss", "w+")
        menustyles.close()
        os.system("yarn add sass")



# NextJS Symfony ok
# Intervention user pour la création du projet nextjs
def create_next_symfony_project(project_name, install_sass=0, routage=0, composants_menu=0):
    testInstallsymfony()
    os.system("composer create-project symfony/skeleton:\"6.2.*\"" + project_name)
    os.chdir(project_name)
    os.system("composer require symfony/webpack-encore-bundle")
    os.system("yarn add @symfony/webpack-encore --dev")
    os.system("npx create-next-app")
    os.system("yarn install")
    os.chdir("assets")
    os.mkdir("js")
    os.chdir("js")
    os.mkdir("components")
    os.chdir("..")
    os.chdir("..")
    if install_sass == 1:
        install_options_sass()
    elif routage == 1:
        os.chdir("src")
        os.mkdir("routage")
        os.chdir("routage")
        os.system("yarn add react-router-dom")
        routeur = open("routeur.js", "w+")  # créer le fichier routeur.js
        routeur.close()
    elif composants_menu == 1:
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("styles")
        os.chdir("styles")
        menustyles = open("Menu.css", "w+")
        menustyles.close()
    elif (composants_menu == 1) and (install_sass == 1):
        os.chdir("assets")
        os.chdir("js")
        os.chdir("components")
        menu = open("Menu.js", "w+")
        menu.close()
        os.mkdir("scss")
        os.chdir("scss")
        main = open("main.scss", "w+")  # créer le fichier main.scss
        main.close()
        variables = open("_variables.scss", "w+")  # créer le fichier _variables.scss
        variables.close()
        responsive = open("_responsive.scss", "w+")  # créer le fichier _responsive.scss
        responsive.close()
        menustyles = open("Menu.scss", "w+")
        menustyles.close()
        os.system("yarn add sass")

# Laravel ok
def create_laravel_project(project_name):
    testInstallLaravel()
    os.system("laravel new " + project_name)
    os.chdir(project_name)

#Angular ok
def create_agular_projet(project_name):
    testInstallNode()
    os.system("npm install -g @angular/cli")
    os.system("ng new " + project_name)
    os.chdir(project_name)



# Create project
def create_project():
    project_name = entree0.get().strip()
    project_type = type.get().strip()
    install_sass = btn1.get()
    composants_menu = btn3.get()
    routage = btn2.get()
    if not project_name:
        # Si le nom du projet n'est pas saisi, affiché une erreur
        error_label.config(text="Veuillez saisir un nom de projet.")
        return

    if project_type == "Symfony-Project":
        create_symfony_project(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()
        cbtn3.grid_forget()

    elif project_type == "Vue-Project":
        create_vue_project(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.pack_forget()
        #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.pack_forget()
        #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()
        
        

    elif project_type == "React-Project":
        create_react_project(project_name, install_sass, routage, composants_menu)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()
        #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()

    elif project_type == "Bot-Discord":
        create_bot_discord()
        cbtn1.grid_forget()
        cbtn2.grid_forget()

    elif project_type == "MERN":
        create_mern_stack(project_name, install_sass, routage, composants_menu)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()
        #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()

    elif project_type == "React-Symfony":
        create_react_symfony_project(project_name, install_sass, routage, composants_menu)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()
        #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()

    elif project_type == "NextJS":
        create_nextjs_project(project_name, install_sass, routage, composants_menu)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()
        #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()

    elif project_type == "Next-Symfony":
        create_next_symfony_project(project_name, install_sass, routage, composants_menu)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
            #################################
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()
            #################################
        if btn3.get() == 1:
            cbtn3.grid(row=10, column=0)
        else:
            cbtn3.grid_forget()

    elif project_type == "Laravel-Project":
        create_laravel_project(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()
        cbtn3.grid_forget()

    elif project_type == "Angular-Project":
        create_agular_projet(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()
        cbtn3.grid_forget()

        success_label.config(
            text="Le projet {} a été créé avec succès!".format(project_name))


def update_tool_options(event):
    project_type = type.get().strip()

    if project_type in ("Symfony-Project", "bot-discord", "Laravel-Project", "Angular-Project"):
        cbtn1.grid_forget()
        cbtn2.grid_forget()
        cbtn3.grid_forget()
    elif project_type in ("React-Symfony", "Vue-Project", "React-Project", "MERN", "NextJS", "Next-Symfony"):
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
        cbtn3.grid(row=9, column=7, sticky="w", padx=10, pady=5)
    else:
        cbtn1.grid_forget()
        cbtn2.grid_forget()
        cbtn3.grid_forget()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Création de projet")
fenetre.configure(background="#03224c")
fenetre.geometry("500x500")

# Création d'un label pour le nom du projet
label0 = tk.Label(fenetre, background="#03224c",
                  foreground="White", text="Entrez le nom du projet: ")
label0.grid(row=0, column=0)

# Création d'une zone de saisie pour le nom du projet
entree0 = tk.Entry(fenetre, width=30)
entree0.grid(row=0, column=1)

# Création d'un label pour le type de projet
label1 = tk.Label(fenetre, background="#03224c",
                  foreground="White", text="Choisissez le type de projet: ")
label1.grid(row=3, column=0)

# Création d'une liste déroulante pour le type de projet
type = ttk.Combobox(fenetre, values=["Symfony-Project", "Vue-Project", "React-Project", "bot-discord", "MERN", "React-Symfony", "NextJS", "Next-Symfony", "Laravel-Project", "Angular-Project"])
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

# Création d'un bouton pour installer un routage basique
btn2 = tk.IntVar()
cbtn2 = tk.Checkbutton(fenetre, text="Routage", variable=btn2)

# Création d'un bouton pour installer un composant
btn3 = tk.IntVar()
cbtn3 = tk.Checkbutton(fenetre, text="component-Menu", variable=btn3)

# Création d'un bouton pour créer le projet
bouton = tk.Button(fenetre, text="Créer le projet", command=create_project)
bouton.grid(row=11, column=1)

# Lancement de la boucle principale
fenetre.mainloop()