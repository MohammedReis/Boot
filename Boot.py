from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from time import localtime
import time
import sys
from colorama import init, Fore, Back

init(autoreset=True)
API = IQ_Option('mohammedfrenzy2015@gmail.com', 'Mohammedd2@')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL

if API.check_connect():
	print(' Conectado com sucesso!')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()

def Martingale(valor, payout):
	lucro_esperado = valor * payout
	perca = float(valor)	
		
	while True:
		if valor * payout > abs(perca) + lucro_esperado:
			return valor
			break
		valor += 0.01



def Payout(par, tipo, timeframe = 1):
		if tipo == 'turbo':
			a = API.get_all_profit()
			return int(100 * a)
		elif tipo == 'digital':
			API.subscribe_strike_list(par, timeframe)
		while True:
			d = API.get_digital_current_profit(par, timeframe)
			if d != False:
				d = int(d)
				break
			time.sleep(1)
		API.unsubscribe_strike_list(par, timeframe)
		return d

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





timeframe = int(input("Qual o tempo da vela: "))
money = float(input("Qual o valor da entrada: "))
payout = int(input(' Valor do payout: '))
martingale = int(input(' Indique a quantia de martingales: '))
martingale += 1
lucro = 0
hora_moeda = arquivo()
print(hora_moeda)
for x in hora_moeda:
	print("teste")
	split = x.split(',')
	hora = split[0]
	moeda = split[1]
	par = str(split[2])
	lcltime = datetime.now().strftime('%H:%M')
	print(lcltime)
	print(hora)
	print(payout)
	while(hora != lcltime):
		lcltime = datetime.now().strftime('%H:%M')
	else:
		print("Ok")	
		Money=money
		ACTIVES=moeda
		ACTION=par
		expirations_mode=timeframe
		valor = 0.0
		for i in range(martingale):
			status,id=API.buy(Money,ACTIVES,ACTION,expirations_mode)
			print("operação realizada, Boa Sorte: ")
			print(status)
			if status:
				while True:
					
					status,valor = API.check_win_v4(id)
					if status:
						valor = valor if valor > 0 else float('-' + str(abs(money)))
						lucro += round(valor, 2)
						print('Resultado operação: ', end='')
						print('WIN /' if valor > 0 else 'LOSS /' , round(valor, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' GALE' if i > 0 else '' ))
											
						money = Martingale(money,payout)
						break
				if valor > 0 : break
			else:
				print('\nERRO AO REALIZAR OPERAÇÃO\n\n')

	time.sleep(0.5)