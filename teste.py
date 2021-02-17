from iqoptionapi.stable_api import IQ_Option
from time import localtime
from datetime import datetime
import time


def carregar_sinais():
    arquivo = open('sinais.txt', encoding='UTF-8')
    lista = arquivo.read()
    arquivo.close

    lista = lista.split('\n')

    for index, a in enumerate(lista):
        if a == '':
            del lista[index]

    return lista



def arquivo():
    
    lista = carregar_sinais()

    hora_moeda = []
    for sinal in lista:
        dados = sinal.split(',')

        hora_moeda.append(dados[0]+","+dados[1]+","+dados[2])
        
    
    return hora_moeda 




print("login...")
API=IQ_Option("mohammedfrenzy2015@gmail.com","Mohammedd2@")
API.connect()#connect to iqoption


hora_moeda = arquivo()
for x in hora_moeda:
    split = x.split(',')
    hora = split[0]
    moeda = split[1]
    par = split[2]
    
    lcltime = datetime.now().strftime('%H:%M')
    while(hora != lcltime):
        lcltime = datetime.now().strftime('%H:%M')
    else:
        
        Money=10
        ACTIVES=moeda
        ACTION=par
        expirations_mode=15
        id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
        print("operação realizada, Boa Sorte: ")
        

        

