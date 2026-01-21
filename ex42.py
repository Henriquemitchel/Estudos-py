l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do terceiro lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f'A junção dos lados \033[0;32mPODE FORMAR\033[m um triângulo')
    if l1 == l2 == l3:
        print(f'\033[0;36mEQUILATERO!\033[m')
    elif l1 == l2 and l1 != l3:
        print(f'\033[0;35mISÓCELIS!\033[m')
    else:
        print(f'\033[0;34mESCALÉNO!\033[m')
else:
    print(f'A junção dos lados \033[0;31mNÃO PODE FORMAR\033[m um triângulo.')

# def tipo_t(l1,l2,l3):
#     if l1 == l2 == l3:
#         return(f'\033[0;36mEQUILATERO!\033[m')
#     elif l1 == l2 and l1 != l3:
#         return(f'\033[0;35mISÓCELIS!\033[m')
#     else:
#         return(f'\033[0;34mESCALÉNO!\033[m')
    
# def form_t(l1, l2, l3):
#     if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
#         return True
#     else:
#         return False

# if form_t(l1,l2,l2) == True:
#     print(f'A junção dos lados \033[0;32mPODE FORMAR\033[m um triângulo' , tipo_t(l1,l2,l3))
# else:
#     print(f'A junção dos lados \033[0;31mNÃO PODE FORMAR\033[m um triângulo.')



    
