from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz
from colorama import init, Fore, Back

init(autoreset=True)
API = IQ_Option('mohammedfrenzy2015@gmail.com', 'Mohammedd2@')
API.connect()
def payout(par, tipo, timeframe = 1):
	if tipo == 'turbo':
		a = API.get_all_profit()
		print(100 * a[par]['turbo'])
		return int(100 * a[par]['turbo'])
		
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

par = API.get_all_open_time()

for paridade in par['turbo']:
	if par['turbo'][paridade]['open'] == True:
		print('[ TURBO ]: '+paridade+' | Payout: '+str(payout(paridade, 'turbo')))
		
print('\n')

for paridade in par['digital']:
	if par['digital'][paridade]['open'] == True:
		print('[ DIGITAL ]: '+paridade+' | Payout: '+str( payout(paridade, 'digital') ))