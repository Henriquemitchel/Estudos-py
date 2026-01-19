l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do terceiro lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))

def form_t(l1, l2, l3):
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        return('Pode formar triangulo')
    else:
        return('Não forma triangulo')

def tipo_t(l1,l2,l3):
    if l1 == l2 == l3:
        return('Trianuglo equilatero')
    elif l1 == l2 and l1 != l3:
        return('Triangulo isocelis')
    else:
        return('Triangulo escaleno')
    
print(form_t(l1,l2,l3))
print(tipo_t(l1,l2,l3))


    
