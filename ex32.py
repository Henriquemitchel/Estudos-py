from datetime import datetime

cores = {'vermelho' : '\033[31m', 'verde':'\033[32m'}
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.now().year
    
if ano %4 == 0 and ano %100 !=0 or ano %400 == 0:
    print(f'{ano} {cores ['verde']}É\033[m bissexto')
else:
    print(f'{ano} {cores ["vermelho"]}NÃO É\033[m bissexto')

