import os
import time
import keyboard
from Arborecense_python.test import *


#la ou ce trouve toutes les fonctions de création de projet et d'installation des outils nécessaires 

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

# Symfony ok
def create_symfony_project(project_name):
    testInstallsymfony()
    print("Tout est installé")
    os.system("composer create-project symfony/skeleton:"+"6.2.*"+" "+ project_name)
    os.chdir(project_name)
    os.system("composer require webapp")
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
def create_react_project(project_name, install_sass=0, routage=0):
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

# Bot Discord ok
def create_bot_discord():
    testInstallNode()
    os.system("git clone https://github.com/DamienFoulon/obot.git")
    os.chdir("obot")
    os.system("npm install")

# MERN ok
def create_mern_stack(project_name, install_sass=0, routage=0):
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

# React Symfony ok
def create_react_symfony_project(project_name, install_sass=0, routage=0):
    testInstallsymfony()
    os.system("composer create-project symfony/skeleton:"+"6.2.*"+" "+ project_name)
    os.chdir(project_name)
    os.system("composer require webapp")
    os.system("composer require symfony/webpack-encore-bundle")
    os.system("yarn add @symfony/webpack-encore --dev")
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

# NextJS ok
# Intervention user pour la création du projet nextjs
def create_nextjs_project(project_name, install_sass=0, routage=0):
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

# NextJS Symfony ok
# Intervention user pour la création du projet nextjs
def create_next_symfony_project(project_name, install_sass=0, routage=0):
    testInstallsymfony()
    os.system("composer create-project symfony/skeleton:\"6.2.*\"" + project_name)
    os.chdir(project_name)
    os.system("composer require symfony/webpack-encore-bundle")
    os.system("yarn install")
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

# Laravel ok
def create_laravel_project(project_name):
    testInstallLaravel()
    os.system("laravel new " + project_name)
    os.chdir(project_name)

#Angular ok
def create_angular_projet(project_name):
    testInstallNode()
    os.system("npm install -g @angular/cli")
    os.system("ng new " + project_name)
    os.chdir(project_name)

