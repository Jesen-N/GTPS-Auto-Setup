#Made By Jesen N
#Inspired By Kesv

import os
from time import sleep

def main():
    print("Done setup all!")
    input("press enter to exit...")

def php():
    global ip, port
    print("setup server_data.php..")
    os.system("cd C:/xampp/htdocs")
    os.system("mkdir growtopia")

    with open('server_data.php', 'w') as f:
        f.write("server|{IP}\nport|{port}\ntype|1\n#maint|Protected By NodeJS-GTPS\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
        print("done setup server_data.php")
        main()

def sama():
    print("Setup Xampp")
    yu = input("install xampp? (y/n): ")
    if yu == "y":
        print("installing xampp..")
        os.system("""%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "Invoke-WebRequest https://downloadsapachefriends.global.ssl.fastly.net/7.4.11/xampp-windows-x64-7.4.11-0-VC15-installer.exe?from_af=true -OutFile xampp.exe""")
        os.system("start xampp.exe")
        lol = input("want download server_data.php? (y/n)")
        if lol == "y":
            php()
        elif lol == "n":
            main()
    elif yu == "n":
        print("ok")
        main()

def suka():
    global ip, port
    print("Setup Port")
    ya = input("Press Enter To Continue: ")
    if ya == "":
        os.system('cls')
        os.system("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""")
        os.system("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""")
        os.system(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
        os.system(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
        os.system("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
        os.system("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
        os.system(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")
        os.system(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")

        os.system('cls')
        print("Done Setup Port!")
        sama()

def aku():
    os.system('cls')
    print("Setup Windows Firewall")
    ye = input("Press Enter To Continue: ")
    if ye == "":
        os.system('cls')
        os.system("""netsh advfirewall set privateprofile state off""")
        os.system("""netsh advfirewall set publicprofile state off""")

        os.system('cls')
        print("Done Setup Windows Firewall")
        suka()

print("""

░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░

[>] Made By Jesen N
[>] Github: http://github.com/Jesen-N
""")
ip = input("Put Your IP: ")
port = input("Port: ")
aku()
