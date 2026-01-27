while True:

    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))

    print('\n----- Qual operação deseja realizar? -----')
    o = int(input('\n[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos Números \n[ 5 ] Sair do Programa\n '))
    if o == 1:
        print(f'O soma de {n1} e {n2} é: {n1+n2}.')        
    elif o == 2:
        print(f'A multiplicação de {n1} e {n2} é: {n1*n2}.')    
    elif o == 3:
        print(f'O maior entre {n1} e {n2} é: {max(n1,n2)}') 
    elif o == 4:
        o == True
    elif o == 5:
        print('O programa terminou.')
        break
    else:
        print('Operação invalida')
        o == True