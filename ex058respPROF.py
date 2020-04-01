#jogo de advinhação
from random import randint
numero = randint(0,5)
print('Sou seu PC e pensei num numero de 0 a 5. Tente advinhar qual!')
tentativa = int(input('Digite um numero: '))
acertou = False
numtentat = 0
while not acertou:
    tentativa = int(input('Digite um numero: '))
    numtentat = numtentat + 1
    if tentativa == numero:
        acertou = True
    else:
        if tentativa < numero:
            print('Errou! Tente um numero MAIOR')
        elif tentativa > numero:
            print('Errou! Tente um numero MENOR')
#else:
print('Acertou miseravi, com {} tentativas'.format(numtentat+1))
