from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from time import localtime
import time
import sys
from colorama import init, Fore, Back
import threading
from dateutil import tz
import json


def stop(lucro, gain, loss):
	if lucro <= float('-' + str(abs(loss))):
		print('Stop Loss batido!')
		arquivo = open('lucro.txt', 'w')
		arquivo.write('0')
		arquivo.close
		sys.exit()
		
	if lucro >= float(abs(gain)):
		print('Stop Gain Batido!')
		arquivo = open('lucro.txt', 'w')
		arquivo.write('0')
		arquivo.close
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


def timestamp_converter(x):
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]


def teste(id,lucro,Money,ACTIVES,ACTION,expirations_mode,martingale,contador,API,stop_loss,stop_gain):
	time.sleep(1)
	arquivo = open('lucro.txt', 'r')
	arquivo1 = arquivo.read()
	lucro = float(str(arquivo1))
	arquivo.close
	if contador == 0:
		condicao = True
		i = 0
		if isinstance(id, int):
			while condicao == True:
				status,valor = API.check_win_v4(id)
				if status:
					valor = valor if valor > 0 else float('-' + str(abs(Money)))
					lucro += round(valor,2)
					print('Resultado operação: ', end='')
					print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
					arquivo = open('lucro.txt', 'w+')
					arquivo.write(str(lucro))
					arquivo.close
					if valor <= 0:
						Money = money*2.1
						stop(lucro, stop_gain, stop_loss)
						#status,id=API.buy_digital_spot(ACTIVES,Money,ACTION,expirations_mode)
						status,id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
						while condicao == True:
							status,valor = API.check_win_v4(id)
							if status:
								i = 1
								valor = valor if valor > 0 else float('-' + str(abs(Money)))
								lucro += round(valor,2)
								print('Resultado operação: ', end='')
								print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
								arquivo = open('lucro.txt', 'w+')
								arquivo.write(str(lucro))
								arquivo.close
								condicao = False
								stop(lucro, stop_gain, stop_loss)
					else:
						Money = money
						stop(lucro, stop_gain, stop_loss)
						break
			sys.exit()
	if contador == 1:
  		#status,valor = API.check_win_v4(id)
		condicao = True
		i = 0
		if isinstance(id, int):
			while condicao == True:
				status,valor = API.check_win_v4(id)
				if status:
					valor = valor if valor > 0 else float('-' + str(abs(Money)))
					lucro += round(valor,2)
					print('Resultado operação: ', end='')
					print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
					arquivo = open('lucro.txt', 'w+')
					arquivo.write(str(lucro))
					arquivo.close					
					if valor <= 0:
						Money = money*2.1
						stop(lucro, stop_gain, stop_loss)
						#status,id=API.buy_digital_spot(ACTIVES,Money,ACTION,expirations_mode)
						status,id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
						while condicao == True:
							status,valor = API.check_win_v4(id)
							if status:
								i = 1
								valor = valor if valor > 0 else float('-' + str(abs(Money)))
								lucro += round(valor,2)
								print('Resultado operação: ', end='')
								print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
								arquivo = open('lucro.txt', 'w+')
								arquivo.write(str(lucro))
								arquivo.close								
								condicao = False
								stop(lucro, stop_gain, stop_loss)
					else:
						Money = money
						stop(lucro, stop_gain, stop_loss)
						break  
			sys.exit()
	if contador == 2:
  		#status,valor = API.check_win_v4(id)
		condicao = True
		i = 0
		if isinstance(id, int):
			while condicao == True:
				status,valor = API.check_win_v4(id)
				if status:
					valor = valor if valor > 0 else float('-' + str(abs(Money)))
					lucro += round(valor,2)
					print('Resultado operação: ', end='')
					print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
					arquivo = open('lucro.txt', 'w+')
					arquivo.write(str(lucro))
					arquivo.close					
					if valor <= 0:
						Money = money*2.1
						stop(lucro, stop_gain, stop_loss)
						#status,id=API.buy_digital_spot(ACTIVES,Money,ACTION,expirations_mode)
						status,id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
						while condicao == True:
							status,valor = API.check_win_v4(id)
							if status:
								i = 1
								valor = valor if valor > 0 else float('-' + str(abs(Money)))
								lucro += round(valor,2)
								print('Resultado operação: ', end='')
								print('WIN /' if valor > 0 else 'LOSS /' , round(Money, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else ''))
								arquivo = open('lucro.txt', 'w+')
								arquivo.write(str(lucro))
								arquivo.close
								stop(lucro, stop_gain, stop_loss)						
								condicao = False
					else:
						Money = money
						stop(lucro, stop_gain, stop_loss)
						break
			sys.exit()


init(autoreset=True)

API = IQ_Option('Login', 'Senha')
API.connect()
API.change_balance('PRACTICE') # PRACTICE / REAL

if API.check_connect():
	print(' Conectado com sucesso!')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()
 

arquivos = open('lucro.txt', 'w')
arquivos.write(str(0))
arquivos.close


timeframe = int(input("Qual o tempo da vela: "))
money = float(input("Qual o valor da entrada: "))
martingale = int(input('Indique a quantia de martingales: '))
stop_loss = float(input('Indique o valor de Stop Loss: '))
stop_gain = float(input('Indique o valor de Stop Gain: '))
lucro = 0
print("\nAguandando a Hora para fazer a entrada !!! ")
martingale += 1
hora_moeda = arquivo()
contador = 0
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
	print("Tendencia: ",tendencia)
	print("Entrada do Sinal: ",par)
	while(hora != lcltime):
			lcltime = datetime.now().strftime('%H:%M')
	else:
		Money=money
		ACTIVES=moeda
		ACTION=par
		expirations_mode=timeframe
		valor = 0.0
		if par == tendencia or tendencia == "False":
			#status,id=API.buy_digital_spot(ACTIVES,Money,ACTION,expirations_mode)
			status,id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
			print("\noperação realizada, Boa Sorte: ")
			
			if status:
				threading.Thread(target=teste, args=(id, lucro,Money, ACTIVES, ACTION,expirations_mode,martingale,contador,API,stop_loss,stop_gain,)).start()
				contador += 1
				if contador == 3:
					contador = 0        
			else:
				print('\nParidade fechada\n\n')
		
		else:
			print('\nOperação contra tendencia\n\n')

sys.exit()