import os
import subprocess


# Verifications technologies installées

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