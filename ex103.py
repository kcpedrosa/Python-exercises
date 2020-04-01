def jogador(a='<desconhecido>',b=0):
    '''
    --->A função printa o nome do jogador e o numero de gols feitos.
    :param a: nome do jogador, opc=<desc>
    :param b: numero de gols, opc=0
    :return: nome e gols feitos
    '''
    print(f'O jogador {a} fez {b} gols')


#programa principal
j = str(input('Digite o nome do jogador  '))
while True:
    g = str(input('Digite o numero de gols  '))
    if g[0] not in '0123456789':
        print('Erro, digite um número')
    else:
        break
if j.strip() == '':
    jogador(b=g)
else:
    jogador(j,g)


help(jogador)
