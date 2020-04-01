from random import randint
from time import sleep
computador = randint(0,2)
print('=-=' * 20)
print('Vou pensar em um numero de 0 a 2, tente advinhar')
print('-=-'*20)
jogador = int(input('Em que numero pensei? Digite um numero: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, vc ganhou')
else:
    print('Perdeu otário, pensei em {}, não em {}'.format(computador, jogador))
