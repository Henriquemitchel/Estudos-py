num = int(input('Que numero deseja descobrir o fatorial? '))

fato = 1
cont = num

while cont > 1:
    fato = fato * cont
    cont = cont - 1
  
print(fato)