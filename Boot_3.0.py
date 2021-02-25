from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from time import localtime
import time
import sys
from colorama import init, Fore, Back
import threading

def stop(lucro, gain, loss):
	if lucro <= float('-' + str(abs(loss))):
		print('Stop Loss batido!')
		sys.exit()
		
	if lucro >= float(abs(gain)):
		print('Stop Gain Batido!')
		sys.exit()

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

def login():
	init(autoreset=True)
	API = IQ_Option('mohammedfrenzy2015@gmail.com', 'Mohammedd2@')
	API.connect()
	if API.check_connect():
		print(' Conectado com sucesso! \n')
	else:
		print(' Erro ao conectar')
		input('\n\n Aperte enter para sair')
		sys.exit()
  
	entrada(API)    

def entrada(API):
	hora_moeda = arquivo()
	for x in hora_moeda:	
		split = x.split(',')
		hora = split[0]
		moeda = split[1]
		par = str(split[2])
		velas = API.get_candles(moeda, (int(timeframe) * 60),100,  time.time())
		ultimo = round(velas[0]['close'], 4)
		primeiro = round(velas[-1]['close'], 4)
		diferenca = abs( round( ( (ultimo - primeiro) / primeiro ) * 20, 3) )
		tendencia = "CALL" if ultimo < primeiro and diferenca > 0.01 else "PUT" if ultimo > primeiro and diferenca > 0.01 else "False"
		lcltime = datetime.now().strftime('%H:%M')
	

timeframe = int(input("Qual o tempo da vela: "))
money = float(input("Qual o valor da entrada: "))
martingale = int(input('Indique a quantia de martingales: '))
stop_loss = float(input('Indique o valor de Stop Loss: '))
stop_gain = float(input('Indique o valor de Stop Gain: '))
martingale += 1
lucro = 0

login()


print("\nAguandando a Hora para fazer a entrada !!! \n")


