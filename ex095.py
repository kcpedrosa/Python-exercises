#refazer o ex093 do zero e continuar com o que foi pedido
time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome']= str(input('Digite o NOME do jogador:  '))
    partidas = int(input(f'Quantas  partidas o {jogador["Nome"]} jogou?:  '))
    for pos in range(0,partidas):
        gols.append(int(input(f'Quantos gols na {pos+1}ª partida? ')))
        jogador['Gols'] = gols[:]
    jogador['Total de gols'] = sum(gols)
    time.append(jogador.copy())
    #essa linha 13 salva no TIME[] enquanto a 6 apaga o JOG{}
    while True:
        perg = str(input('Quer continuar? [S/N]  '))
        if perg in 'SsNn':
            break
        else:
            print('ERRO! Responda apenas S ou N ')
    if perg in 'Nn':
        break
print('=-'*40)
print('cod', end=' ')
for k, v in jogador.items():
    print(f'{k:<15}', end=' ')
print()
print('--'*40)
for pos, c in enumerate(time):
    print(f'{pos:>3} ' ,end=' ')
    for d in c.values():
        #só printa os valores, ou seja, ex KAKA, e não 'Nome'
        print(f'{str(d):<15}', end=' ')
    print()
print('--'*40)
while True:
    perg = int(input('Quer saber os dados de qual jogador? [Digite o código, digite 999 para parar:  '))
    if perg == 999:
        break
    elif perg > len(time):
        print('ERRO! Não existe um jogador com o código digitado. COD. INVAL.')
    else:
        print(f'---Analisando os dados do jogador {time[perg]["Nome"]}')
        for pos, c in enumerate(time[perg]['Gols']):
            print(f'Na {pos+1} ª partida, {time[perg]["Nome"]} fez {c} gols')
print('=-'*30)
print('FIM DO PROGRAMA...')
print(time)









#print(jogador)
#print(gols)
#print(sum(gols))