#OBS fiz do zero esse ex no ex095, que precisava da base deste aqui
dados = {}
partidas = []
dados['Nome'] = str(input('Digite o NOME do jogador:  '))
num = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for pos in range(0, num):
    partidas.append(int(input(f'    Quantos gols {dados["Nome"]} fez na {pos+1}ª partida? ')))
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)

print(dados)
print(partidas)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v} ')
print('=-'*30)
print(f'O jogador {dados["Nome"]} fez {len(dados["Gols"])} partidas')
for pos, c in enumerate(partidas):
    print(f'  => Na partida {pos+1} o jogador fez {c} gols')
print(f'O total de gols foi {dados["Total"]}')