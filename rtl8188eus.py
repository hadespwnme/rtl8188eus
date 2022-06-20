import os
import platform

#warna
RED = "\x1B[31m"
BRED = "\x1B[41m"
GREEN = "\x1B[32m"
BGREEN = "\x1B[42m"
DEFAULT = "\x1B[0m"
nc="\033[1;37m"
yellow="\033[1;33m"


def install_kali():
    print(f"{nc}[{RED}+{nc}]{yellow}Update & Upgrading system!!!{nc}[{RED}+{nc}]")
    os.system("sudo apt update -y && apt upgrade -y && apt dist-upgrade")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing linux headers{nc}[{RED}+{nc}]")
    os.system("sudo apt-get install linux-headers-$(uname -r) -y")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing bc{nc}[{RED}+{nc}]")
    os.system("sudo apt install bc -y")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Deleting old driver{nc}[{RED}+{nc}]")
    os.system("sudo rmmod r8188eu.ko")
    print()
    os.system("clear")
    prinr(f"{nc}[{RED}+{nc}]{yellow}Installing module pyperclip{nc}[{RED}+{nc}]")
    os.system("sudo pip3 install pyperclip")
    print()
    os.system("clear")
    prinr(f"{nc}[{RED}+{nc}]{yellow}Installing module pyautogui{nc}[{RED}+{nc}]")
    os.system("sudo pip3 install pyautogui")
    os.system("cd rtl8188eusFIX && sudo python3 command-for-kalilinux.py")
    print()
    os.system("clear")
    prinr(f"{nc}[{RED}+{nc}]{yellow}Installing Driver{nc}[{RED}+{nc}]")
    os.system("sudo make && sudo make install && sudo modprobe 8188eu")

def install_parrot():
    print(f"{nc}[{RED}+{nc}]{yellow}Update & Upgrading system!!!{nc}[{RED}+{nc}]")
    os.system("sudo apt update && sudo apt -y upgrade")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing Build Essential{nc}[{RED}+{nc}]")
    os.system("sudo apt-get install build-essential")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing bc linux header{nc}[{RED}+{nc}]")
    os.system("sudo apt-get install -y bc linux-headers-$(uname -r)")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing linux header{nc}[{RED}+{nc}]")
    os.system("sudo apt install linux-headers-$(uname -r)")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing linux header amd64{nc}[{RED}+{nc}]")
    os.system("sudo apt-get install linux-headers-amd64")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing bc{nc}[{RED}+{nc}]")
    os.system("sudo apt install bc")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing module pyautogui{nc}[{RED}+{nc}]")
    os.system("sudo pip3 install pyautogui")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing module pyperclip{nc}[{RED}+{nc}]")
    os.system("sudo pip3 install pyperclip")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Deleting old driver{nc}[{RED}+{nc}]")
    os.system("sudo rmmod r8188eu.ko")
    print()
    os.system("clear")
    print(f"{nc}[{RED}+{nc}]{yellow}Installing driver{nc}[{RED}+{nc}]")
    os.system("cd rtl8188eusFIX && sudo python3 command-for-parrotos.py")
    os.system("sudo make && sudo make install && sudo modprobe 8188eu")


def menu():
    sistem = platform.uname()
    LOGO = f"""
	                {RED}.YYY555PPPPGGGG?
	                .BBB####&&&&&@@?
	                .GBBB:.....P&&@?
	         .~     .GBBG      5@&@?
	        ^BJ     .GBBG      5@&@?
	       ?B#J     .GBBG      5@&@?   {yellow}| {nc}System    : {GREEN}{sistem.system}{RED}
	      !BBBJ     .PGGG      5@&@?   {yellow}| {nc}Node Name : {GREEN}{sistem.node}{RED}
	      !BB#J                5@&@?   {yellow}| {nc}Machine   : {GREEN}{sistem.machine}{RED}
	      !BB#J     {GREEN}HADES{RED}      5@&@?   {yellow}| {nc}Release   : {GREEN}{sistem.release}
	     {nc} !BB#J        ..      5@&@?
	      !BB#J      #&&&.     5@&@?
	      !BB#J      &&@@.     5@@5
	      !BB#J      &&@&.     P&~
	      !BB#J      &&@&.     !.
	      !BBBY.....:&&@&.
	      !BBB###&&&&&@@@.
	      !YYYY555PPPGGGG.{nc}

	           [{RED}+{nc}]{GREEN}Installing DRIVER {yellow}RTL8188EUS{nc}[{RED}+{nc}]
	"""
    print(LOGO)
    print(f'''
                        {nc}------------------------
                              {RED}MENU INSTALL
                        {nc}------------------------

                           {yellow}1) Install on kali linux
                           {yellow}2) Install on Parrot Os
    ''')
    menu = input(f"{GREEN}hades> ")
    if menu == "1":
        install_kali()
    elif menu == "2":
        install_parrot()
    else:
        menu()

menu()
    