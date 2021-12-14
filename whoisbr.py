
# Simples Script para pegar informaçoes de um site ou ip.
# acho que nem vou soltar kkkkkk
# criador: https://github.com/bruntyt



import whois
import os
import time

nome = input("Qual é o seu nome? ")
print(nome, ", seja bem vindo!!")

os.system('clear')
os.system('figlet Whois?')

comando = input('Site ou IP >>> ')
os.system('echo ')
print(''aguarde..."
time.sleep(1)
os.system('echo ')
print('ᴅɴs ᴇ sᴜʙᴅᴏᴍɪɴɪᴏs')
print('-------------------')
os.system(f'host {comando}')
print('-------------------')
os.system('echo ')
print('ɪɴғᴏʀᴍᴀÇᴏᴇs! ')
os.system('echo ')
os.system(f'whois {comando} | grep "domínio:" ')
os.system(f'whois {comando} | grep "Proprietário:" ')
os.system(f'whois {comando} | grep "país:" ')
os.system(f'whois {comando} | grep "ownerid:" ')
os.system(f'whois {comando} | grep "person:" ')
os.system(f'whois {comando} | grep "e-mail:" ')
os.system(f'whois {comando} | grep "responsável:" ')
os.system('echo ')

