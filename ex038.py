#esse é um programa para comparar numeros
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um segundo numero: '))
if n1 > n2:
    print('O numero {:.2f} [que é o primeiro] é maior que {:.2f}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} [que é o segundo] é maior que {}'.format(n2, n1))
else:
    print('Os dois valores são iguais')


