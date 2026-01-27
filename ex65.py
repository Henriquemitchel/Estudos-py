med = 0
con = 0
mai = 0
men = 0  

while True:
    
    num = int(input('Digite um numero: '))
    con = con + 1
    med = med + num
    
    if con == 1:
        mai = num
        men = num
    else:
        if num > mai:
            mai = num
        if num < men:
            men = num
           
    res = str(input('Quer continuar? [S/N] ')).strip().lower()
    if res != 's':
        print(f'Voce digitou {con} numeros, a media foi {med//con}.\nO maior foi {mai} e o menor foi {men}.')
        break
    