#jogo de advinhação
from random import randint
numero = randint(0,5)
print('Sou seu PC e pensei num numero de 0 a 5. Tente advinhar qual!')
tentativa = int(input('Digite um numero: '))
numtentat = 0
while tentativa != numero:
    numtentat = numtentat +1
    if tentativa < numero:
        print('Errou! Tente um numero MAIOR')
    elif tentativa > numero:
        print('Errou! Tente um numero MENOR')
    tentativa = int(input('Digite um numero: '))

else:
    print('Acertou miseravi, foram {} tentativas'.format(numtentat+1))