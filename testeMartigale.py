from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz

API = IQ_Option('mohammedfrenzy2015@gmail.com', 'Mohammedd2@')
API.connect()
API.change_balance('PRACTICE') # PRACTICE / REAL

while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		API.connect()
	else:
		print('Conectado com sucesso')
		break
	
	time.sleep(1)

def timestamp_converter(x):
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

 
par = 'EURUSD-OTC'
status,id=API.buy_digital_spot(par,5,'CALL',1)
vela = API.get_candles(par,60,1,time.time())
valorAtual = str(vela[0]['close'])
x = float(int(vela[0]['to']))
x = x-1
x = timestamp_converter(x)

lcltime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


while(x != lcltime):
    lcltime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
else:
    vela = API.get_candles(par,60,1,time.time())
    valorDeFechamento = str(vela[0]['close']) 
    if  valorDeFechamento < valorAtual:
        status,id=API.buy_digital_spot(par,5,'CALL',1)
        print(status)
