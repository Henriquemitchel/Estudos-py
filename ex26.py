frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A quantidade de letra A nessa frase é: {frase.count("a")}')
print(f'A primeira posição da letra A é: {frase.find("a")+1}')
print(f'A ultima posição da letra A é: {frase.rfind('a')+1}')