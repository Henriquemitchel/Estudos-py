p = str(input('Digite uma frase: ')).strip().replace(' ', '').lower()

if p == p[::-1]:
    print('\nÉ palindromo')
else:
    print('\nNão é palindromo')