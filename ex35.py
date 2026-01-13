r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
cores = {'sem formato' : '\033[30m' ,'verde':'\033[32m', 'vermelho' :'\033[35m'}

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Os segmentos {cores['verde']}PODEM\033[m formar um triangulo!')
else:
    print(f'Os segmentos {cores ['vermelho']}NÃO PODEM\033[m formar um triangulo!')
    