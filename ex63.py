l = int(input('Quantos valores das sequencia de fibonacci quer ver: '))

a = 1
b = 1

while l > 1:
    n = a + b
    a = b
    b = n
    l = l - 1
    print(n)