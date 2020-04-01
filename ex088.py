#sortear 6 numeros da megasena X vezes
from random import randint
lista = []
jogos = []
print('=-'*20)
print('    MEGA SENA    ')
perg = int(input('Quantos jogos você quer que sejam gerados: '))
tot = 1
while tot <= perg:
    cont=0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
            #atenção a identação, lista.sorte estava bem abaixo desse IF
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'Os numeros foram: ')
for pos, c in enumerate(jogos):
    print(f'{c}')
print('BOA SORTE!!!')