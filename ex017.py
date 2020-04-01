'''import math
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
h = math.sqrt(c1 **2 + c2 ** 2)
print (' O valor da hipotenusa é: {:.3f} '.format(h))'''

c1 = float(input('Digite o valor do cateto 1: '))
c2 = float(input('Digite o valor do cateto 2: '))
h = (c1 ** 2 + c2 ** 2) **(1/2)
print('O valor da hipotenusa é: {:.3f}'.format(h))