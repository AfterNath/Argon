
import os 
from time import *
from time import sleep
from os import *
from pyfade import *
from pyfade import Colors
from pyfade import Fade
from colorama import *
from pycenter import *
from os import system

system("title Argon")
system("mode 160, 40")

cls = os.system("cls")

# Title

splash = """                                                                                                                                                                                     

##        #######     ###    ########  #### ##    ##  ######               
##       ##     ##   ## ##   ##     ##  ##  ###   ## ##    ##              
##       ##     ##  ##   ##  ##     ##  ##  ####  ## ##                    
##       ##     ## ##     ## ##     ##  ##  ## ## ## ##   ####             
##       ##     ## ######### ##     ##  ##  ##  #### ##    ##              
##       ##     ## ##     ## ##     ##  ##  ##   ### ##    ##  ###      ###     ### 
########  #######  ##     ## ########  #### ##    ##  ######   ###      ###     ###                                                 
"""

sep = """
---------------------------------------------------\n
"""


# /Title




def push():
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    print(center(Fore.GREEN + "Votre lien devrait ressembler a ca :" + Fore.BLUE + " https://github.com/[USER]]/[REPO].git"))
    gitlink = input("Entrez votre lien > ")
    sleep(1)
    os.system("git remote add origin " + gitlink)
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    print(Fore.MAGENTA + "Publication en cours...")
    sleep(1)
    print(Fore.RESET)
    os.system("git add .")
    os.system("git commit -m New Commit")
    os.system("git push origin main")
    sleep(1)
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    print(Fore.GREEN + "Tache effectuée avec succes !")
    sleep(3)
    os.system("cls")
    main()


def init():
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m FirstCommit")
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    print(Fore.GREEN + "Tache effectuée avec succes !")
    sleep(3)
    os.system("cls")
    main()

def commit():
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    commessage = input(Fore.LIGHTGREEN_EX + "Message d'information > ")
    os.system("git add .")
    os.system("git commit -m " + commessage)
    os.system("cls")
    print(Fore.GREEN + "Tache effectuée avec succes !")
    sleep(3)
    os.system("cls")
    main()

#SelMenu
def main():
    os.system("cls")
    print(center(Fore.CYAN + "ARGON V0.1 // By AfterNath"))
    print(center(Fade.Vertical(Colors.purple_to_blue,"""
                                =======================================
                                |                                     |
                                |       1. Initialiser le REPO        |
                                |       2. Commit                     |
                                |       3. Envoyer sur GitHub         |
                                |       4. Credits                    |
                                |                                     |
                                =======================================
    """)))
    

    selection = input(Fore.LIGHTGREEN_EX + "Choisissez une option > " + Fore.RESET)

    if selection == "1":
        os.system("cls")
        init()
    
    if selection == "2":
        os.system("cls")
        commit()

    if selection == "3":
        os.system("cls")
        push()




print(Anime.anime(splash, Colors.purple_to_red, Fade.Vertical, time=4))
os.system("cls")
main()