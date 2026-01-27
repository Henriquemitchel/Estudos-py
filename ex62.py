
pt = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
l = 10

while True:
    
    print('Os 10 primeiros termos da PA são:')
    while l > 1:
        pt = pt + ra
        l = l - 1
        print( pt , end= ' ')
    
    mt = int(input('\nQuer mostrar mais quantos termos?\nSe quer encerrar digite [ 0 ] '))
    l = mt + 1
    if mt == 0:
        print('Programa terminou')
        break