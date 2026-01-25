ida = 0 
tot = 0
velho = 0
velho_nome = ''

for c in range(1,5):
    print(f'\n----- {c}º Pessoa -----')
    idade = int(input(f'\nIdade: '))
    ida = idade + ida
    
    sexo = str(input(f'Sexo [M/F]: ')).strip().lower()
    if sexo == 'f' and idade < 20:
        tot = tot + 1
        
    nome = str(input(f'Nome: ')).strip().capitalize()
    if sexo == 'm' and idade > velho:
        velho = idade
        velho_nome = nome
    
if velho == 0 and velho_nome == '':
    print('\nNão ha homens no grupo.')
else:
    print(f'\nO homem mais velho tem {velho} anos e seu nome é {velho_nome}.')
print(f'A média de idade do grupo foi: {ida//c} anos.')
print(f'O total de mulheres com menos de 20 anos foi: {tot}.')
