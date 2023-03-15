import tkinter as tk
from tkinter import ttk
from Arborecense_python.arbo import *


# Création de la fenêtre principale (main window)

def create_project():
    project_name = entree0.get().strip()
    project_type = type.get().strip()
    install_sass = btn1.get()
    routage = btn2.get()
    if not project_name:
        # Si le nom du projet n'est pas saisi, affiché une erreur
        error_label.config(text="Veuillez saisir un nom de projet.")
        return

    if project_type == "Symfony-Project":
        create_symfony_project(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()

    elif project_type == "Vue-Project":
        create_vue_project(project_name)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.pack_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.pack_forget()

    elif project_type == "React-Project":
        create_react_project(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.pack_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.pack_forget()

    elif project_type == "Bot-Discord":
        create_bot_discord()
        cbtn1.grid_forget()
        cbtn2.grid_forget()

    elif project_type == "MERN":
        create_mern_stack(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()

    elif project_type == "React-Symfony":
        create_react_symfony_project(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()

    elif project_type == "NextJS":
        create_nextjs_project(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()

    elif project_type == "Next-Symfony":
        create_next_symfony_project(project_name, install_sass, routage)
        if btn1.get() == 1:
            cbtn1.grid(row=9, column=0)
        else:
            cbtn1.grid_forget()
        if btn2.get() == 1:
            cbtn2.grid(row=10, column=0)
        else:
            cbtn2.grid_forget()

    elif project_type == "Laravel-Project":
        create_laravel_project(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()

    elif project_type == "Angular-Project":
        create_angular_projet(project_name)
        cbtn1.grid_forget()
        cbtn2.grid_forget()

        success_label.config(
            text="Le projet {} a été créé avec succès!".format(project_name))


def update_tool_options(event):
    project_type = type.get().strip()
    if project_type == "symfony-project":
        cbtn1.grid_forget()
        cbtn2.grid_forget()
    elif project_type == "bot-discord":
        cbtn1.grid_forget()
        cbtn2.grid_forget()
    elif project_type == "react-symfony":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "vue-project":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "react-project":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "MERN":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "NextJS":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "next-symfony":
        cbtn1.grid(row=9, column=0, sticky="w", padx=10, pady=5)
        cbtn2.grid(row=10, column=0, sticky="w", padx=10, pady=5)
    elif project_type == "laravel-project":
        cbtn1.grid_forget()
        cbtn2.grid_forget()
    elif project_type == "Angular-Project":
        cbtn1.grid_forget()
        cbtn2.grid_forget()
    else:
        cbtn1.grid_forget()


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
type = ttk.Combobox(fenetre, values=["Symfony-Project", "Vue-Project",
                    "React-Project", "bot-discord", "MERN", "React-Symfony", "NextJS", "Next-Symfony", "Laravel-Project", "Angular-Project"])
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


# Création d'un bouton pour créer le projet
bouton = tk.Button(fenetre, text="Créer le projet", command=create_project)
bouton.grid(row=11, column=1)

# Lancement de la boucle principale
fenetre.mainloop()
