n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1>n2 and n1>n3:
    print('{} é maior'.format(n1))
elif n2>n1 and n2>n3:
    print(' {} é maior'.format(n2))
else:
    print('{} é maior'.format(n3))
#agora para o menor
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1<n2 and n1<n3:
    print('{} é menor'.format(n1))
elif n2<n1 and n2<n3:
    print(' {} é menor'.format(n2))
else:
    print('{} é menor'.format(n3))
