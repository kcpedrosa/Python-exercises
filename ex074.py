#Maior e menor valores em Tupla COM NUMEROS SORTEADOS
from random import randint
print('O programa vai sortear 5 valores')
numeros = (randint(1,10), randint(1,10),
           randint(1,10), randint(1,10), randint(1,10))
print(f'Os numeros sorteados foram {numeros}')
#o professor fez
#print('Os valores sorteados foram: ', end='')
#for n in range numeros
#   print(f'{n}',end='')
print(f'O maior numero dentre os digitados foi {max(numeros)}')
print(f'O menor numero dentre os digitados foi {min(numeros)}')