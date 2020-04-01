#jogo de par ou impar
from random import randint
jogador=0
computador=0
vitoria=0
while True:
    tipo = str(input('Digite PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    while tipo not in 'PI':
        tipo = str(input('Digite PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    jogador = int(input('Digite um valor[numero de 0 a 10]: '))
    computador = randint(0, 10)
    total = jogador + computador
    print('Você jogou {} e o computador jogou {}, o total foi de {}'.format(jogador, computador, total))
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2==0:
            print('VOCE VENCEU')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCE VENCEU')
            vitoria +=1
        else:
            print('Você perdeu')
            break
    print('Let´s play again...')
#inicialmente coloquei o BREAK na vitoria e o prof pos na derrota, se por na vitoria o contador
#sempre vai dar UMA vitoria
print(f'Você ganhou {vitoria} vez[es]')