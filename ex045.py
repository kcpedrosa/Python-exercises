#esse é um programa para jogar pedra papel tesoura
from random import randint
import time
#deixei aqui o exemplo de como usar a importação de modulos com import ou com from
#para usar usando import é nec. colocar nomedomodulo.função
#usando from/import so precisa colocar o nome da função

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('Vamos jogar PEDRA PAPEL E TESOURA')
print('''Suas opções são:
[ZERO] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Qual é a sua jogada? Digite o numero: '))
print('=-='*20)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!!')
time.sleep(3)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=-='*20)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O jogador VENCEU')
    elif jogador == 2:
        print('O computador VENCEU')
    elif jogador >= 3:
        print('Jogada inválida')
if computador == 1:
    if jogador == 0:
        print('O computador VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O jogador VENCEU!')
    elif jogador >= 3:
        print('Jogada inválida')
if computador == 2: #pc jogou tesoura
    if jogador == 0:
        print('O jogador VENCEU!')
    elif jogador == 1:
        print('O computador VENCEU')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador >= 3:
        print('Jogada inválida')
