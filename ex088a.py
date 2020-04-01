from random import randint
from time import sleep
lista = []
jogos = []
print('=-'*30)
print('   JOGOS DA MEGA SENA   ')
perg = int(input('Digite quantos jogos você quer visualizar: '))
tot = 1
while tot <= perg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {perg} jogos...')
sleep(2)
print('Os jogos sorteados foram: ')
for pos, c in enumerate(jogos):
    sleep(1)
    print(f'Jogo {pos+1} : {c}')
print('<<<<BOA SORTE>>>>')

