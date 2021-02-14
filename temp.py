def carregar_sinais():
    arquivo = open('sinais.txt', encoding='UTF-8')
    lista = arquivo.read()
    arquivo.close

    lista = lista.split('\n')

    for index, a in enumerate(lista):
        if a == '':
            del lista[index]

    return lista




    
lista = carregar_sinais()

hora_moeda = []
for sinal in lista:
    dados = sinal.split('-')

    hora_moeda.append(dados[0]+"-"+dados[1]) 
    
     
    
print(hora_moeda)     
 
	
 
 
