import random
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
lista = [a, b, c]

print('A ordem de apresentação será {}'.format(random.shuffle(lista)))

