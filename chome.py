﻿#imports
import cmd
from gettext import find
from tkinter import ON, ttk
import webbrowser 
import platform
import socket
import multiprocessing as mp
import os

#host ip
get_ip = lambda : socket.gethostbyname(socket.gethostname())

git = "https://github.com/flipper1/flipper-auto-"
urlsextap = "https://www.pornhub.com/view_video.php?viewkey=2006034279#1"
oakferd = "https://www.google.com/maps/place/11+Oakfern+Crescent,+Stittsville,+ON+K2S+1E5/@45.2617061,-75.9167991,3a,79.4y,324.32h,84.41t/data=!3m6!1e1!3m4!1sQms25DhHVi3aldbfIqYymQ!2e0!7i16384!8i8192!4m5!3m4!1s0x4ccdff4d902e1c7b:0xf4f14b456052e0f7!8m2!3d45.2618533!4d-75.9170219"
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))

#start menu
#flipper text
print ('')
print ('                               ███████╗██╗░░░░░██╗██████╗░██████╗░███████╗██████╗░   ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░')
print ('                               ██╔════╝██║░░░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗   ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░')
print ('                               █████╗░░██║░░░░░██║██████╔╝██████╔╝█████╗░░██████╔╝   ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌')
print ('                               ██╔══╝░░██║░░░░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗   ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░')
print ('                               ██║░░░░░███████╗██║██║░░░░░██║░░░░░███████╗██║░░██║   ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░')
print ('                               ╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝   ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░')
#spaces 
print ('                                                                                     ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░')
#auto text
print ('                                       ░█████╗░██╗░░░██╗████████╗░█████╗░            ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄')
print ('                                       ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗            ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒')
print ('                                       ███████║██║░░░██║░░░██║░░░██║░░██║            ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒')
print ('                                       ██╔══██║██║░░░██║░░░██║░░░██║░░██║')
print ('                                       ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝')
print ('                                       ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░')
print ('')
print ('')
print ('')
print ('           █░█░█ █░█ ▄▀█ ▀█▀   █░█░█ █▀█ █░█ █░░ █▀▄   █▄█ █▀█ █░█   █░░ █ █▄▀ █▀▀   ▀█▀ █▀█   █▀▄ █▀█')
print ('           ▀▄▀▄▀ █▀█ █▀█ ░█░   ▀▄▀▄▀ █▄█ █▄█ █▄▄ █▄▀   ░█░ █▄█ █▄█   █▄▄ █ █░█ ██▄   ░█░ █▄█   █▄▀ █▄█')
print ('')
print ('                                                              ┏┓')
print ('                                                              ┃┃')
print ('                                          ┏━━┳━━┳┓┏┳┓┏┳━━┳━┓┏━┛┣━━┓')
print ('                                          ┃┏━┫┏┓┃┗┛┃┗┛┃┏┓┃┏┓┫┏┓┃━━┫')
print ('                                          ┃┗━┫┗┛┃┃┃┃┃┃┃┏┓┃┃┃┃┗┛┣━━┃')
print ('                                          ┗━━┻━━┻┻┻┻┻┻┻┛┗┻┛┗┻━━┻━━┛')
print ('')
print ('                                 "spammer" , "money" , "hacking" , "other" ')
print ('')

whepion = input("                                              what is it today?")
if  whepion == "spammer":
    spam = True
    while spam == True:
        print("11oakferd")
        webbrowser.get('chrome').open_new_tab(oakferd)
if whepion == "other":
    print ('           █░█░█ █░█ ▄▀█ ▀█▀   █░█░█ █▀█ █░█ █░░ █▀▄   █▄█ █▀█ █░█   █░░ █ █▄▀ █▀▀   ▀█▀ █▀█   █▀▄ █▀█')
    print ('           ▀▄▀▄▀ █▀█ █▀█ ░█░   ▀▄▀▄▀ █▄█ █▄█ █▄▄ █▄▀   ░█░ █▄█ █▄█   █▄▄ █ █░█ ██▄   ░█░ █▄█   █▄▀ █▄█')
    print ('')
    othyr = input('                                 "info" , "account" , "history" , "github" ')
    if othyr == "info":
        print ("11 oakferd cres")
        print ("Processor:", )
        print ("gpu:")
        print ("ram:")
        print ("name")
        print ("operating system:", platform.system(), platform.version(), platform.node())
        print ("your ip:", get_ip())
    if othyr == "history":
        os.system('cmd /k "ipconfig /displaydns"')
    if othyr == "github":
        webbrowser.get('chrome').open_new_tab(git)
#spam
































































































































#beppe
if whepion == "beppe":
    print ("░▄█████░█████▌░█░▀██████▌█▄▄▀▄")
    print ("░▌███▌█░▐███▌▌░░▄▄░▌█▌███▐███░▀")
    print ("▐░▐██░░▄▄▐▀█░░░▐▄█▀▌█▐███▐█")
    print ("░░███░▌▄█▌░░▀░░▀██░░▀██████▌")
    print ("░░░▀█▌▀██▀░▄░░░░░░░░░███▐███")
    print ("░░░░██▌░░░░░░░░░░░░░▐███████▌")
    print ("░░░░███░░░░░▀█▀░░░░░▐██▐███▀▌")
    print ("░░░░▌█▌█▄░░░░░░░░░▄▄████▀░▀")
    print ("░░░░░░█▀██▄▄▄░▄▄▀▀▒█▀█░")
    print ("╠─────────────────────────────────────────────────────────────────────────────────────╣")
    print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%&%%%%%%%&%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%%%%%%%%%%%%%&&&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@@@@&&%%%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@&&%#####(######%%%&&&@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%&@@@@@@&&&#%(((((((((((((####%%%%&&&@@@&&@@@@@@@@%%%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%&&@@@@@@#%#((////////////(((((####%%%&&&@@@@%%%&@@@@@@%%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%&@@@@@@@#(///////////////////(((((###%&&&@@@@@%%&%%@@@@@%%%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&%%%%%%%%%%%%%%%#@@%%%&%#((/#%%&&&&&#(///////(%%&@&&%####%&@@@@@%%&%%%%%@@&%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&%%%%%%%%%%%%%%#@@%%%%@#((%#//**///((//////(#%&%######%%%%%&@@@@@@&&%%%@@@@%%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&%%%%%%%%%%%%%%#@&%%%%&%((////(#&@@&%(/////(#&@@@@#&#@@&&&@@@@@@@@@@@@@@@@@@%%%%%%%%%%%")
    print ("&&&&&&&&&&&&&&%%%%%%%%%%%%%@@@@&@&&&%///(%&&%%%%##(/////(#&&@@@&%((((##%&&&@@@@@@@@@@@@@@%%%%%%%%%%%")
    print          ("&&&&&&&&&&&&&&%%%%%%%%%%%%%@@@@@@@@@(//////****/////*////#%&&@@&&%#######%&&@@@@@@@@@@@@@@%%%%%%%%%%")
    print          ("&&&&&&&&&&&&&&%%%%%%%%%%%%&@@@@@@@@@(//****///***********/#&&&@&&%//(((##%&&@@@@@@@@@@@@@@%%%%%%%%%%")
    print          ("&&&&&&&&&%%&&&%%%%%%%%%%%%@@@@@@@@@@//**************/%/*(#%&#(&&#****//((#%&&@@@@@@@@@@@@@%%%%%%%%%%")
    print          ("&&&&&&&&&&&&&&%%%%%%%%%%%%@@@@@@@@@@//****,,,,**/*******///(#%&%#(/***//(#%&&@@@@@@@@@@@@@%%%%%%%%%%")
    print          ("&&&&&&&&&%&&&&%%%%%%%%%%%%&&&%#&@&@@#/***,,,,**/***/****//((((#%&&%//////(%&&@@@@@@@@@@@@@@@@@%%%%%%")
    print          ("&&&&&&&&&&%&&&%%%%%%%%%%%%%@(**%&@&@@/**,,,,,*****/(#(/**/(/##%##%%((///((#&@@@@@@@@@@@@@@@@@&%%%%%%")
    print          ("&&&&&&&&&&%&&%%%%%%%%%%%%%%@@@@@@@@@@#/**,,,,**/(((((#########%&&&%(////##%&@@@@@@@@@@@@@@@%%%%%%%%%")
    print         ("&&&&&&&&&&%&&%%%%%%%%%%%%%%%@@@@@@@@@@(***,,,,******//////(((#%%&#(((//(#%&@@@&@@@@@@@@@%%%#%%%%%%%%")
    print         ("&&&&&&&&&%%&%%%%%%%%%%%%%%%%%&@@@@@@@@@(**,,,,,,,*******///////((((((((#%&@@@&%%#%%%%%%&%##%%%%%#%%%")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/**,,,,,,********////(((####%%&&@@@%%%%%%%%%%%&%##%%%%%%%%%")
    print         ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%///******,,,,,******//(#%%&&@@@@@@@%%####%%%%%#%########%%#")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#**//******,**,****/(##%%&@@@@@@@@@%%#####%%%%###########%%")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*****//*////////((##%%&@@@@@@@@@@@%#######%%##############")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%**,,,***//////((((##%&&&&&@@@@@@@@&#%%%%%%%%#%%%%%%%######")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%**,,,***//////((((##%&&&&&@@@@@@@@&#%%%%%%%%#%%%%%%%######")
    print          ("&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%**,,,,,,,,***//((###%%##((///((#&@@@@%#%&%%%##%###%%%#####")
    print          ("&&&&&&&&%%%%%%%%%%%%#%%%%#%#%#%%%%%%%%%%%/**,,,,,,,,,,***************///(#%%&@@&%@@@@@&#%%%%%%%#####")
    print          ("&&&&&&&&%%%%%%%%%@@@@@@@@@@@@@@@&&%%%%(/****,,,,,,,,,,,,,,,,,********/(%&@@@@@&&@@&@@@@@@@@@@@@&&&&&")
    print          ("&&&&&&&%%%%%%%&@@@@@@@@@@@@@@@@&&&&&%%%/****,,,,,,,,***/((#%&&@&&&&&&&&&&&@@&%@&&&@@@@@@@@@@&&@@@&&&")
    print          ("&&&&&&&%%%%%%@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&@@%&&&&&@@@@@&&&&&&&&&&&&&&")
    print          ("&&&&&&&%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&@@&&&&&&&&&&&&&&&&&&&&")
    print         ("&&&&&&%%&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#&&@@&&&&&&&&&&&&&&&&&&&&&&&")


    print ("╠────────────────────────────────────────────────────────────────────────────────────────────────────────╣")


print ("░▄█████░█████▌░█░▀██████▌█▄▄▀▄")
print ("░▌███▌█░▐███▌▌░░▄▄░▌█▌███▐███░▀")
print ("▐░▐██░░▄▄▐▀█░░░▐▄█▀▌█▐███▐█")
print ("░░███░▌▄█▌░░▀░░▀██░░▀██████▌")
print ("░░░▀█▌▀██▀░▄░░░░░░░░░███▐███")
print ("░░░░██▌░░░░░░░░░░░░░▐███████▌")
print ("░░░░███░░░░░▀█▀░░░░░▐██▐███▀▌")
print ("░░░░▌█▌█▄░░░░░░░░░▄▄████▀░▀")
print ("░░░░░░█▀██▄▄▄░▄▄▀▀▒█▀█░")


