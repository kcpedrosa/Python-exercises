galera = []
dados = []
espectro = []
naoehum = hum = 0
for c in range(0,3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a IDADE: ')))
    galera.append(dados[:])
#se vc nao por [:], qnd o prog der clear em dados dará clear tb em galera pois sem o [:]
#cria-se uma ligação entre as listas
    dados.clear()
for p in galera:
    if p[1] > 100:
        print(f'{p[0]} não é humano')
        naoehum += 1
        if p[1] > 500:
            espectro.append(p[0])
            print(f'{p[0]} é um ESPECTRO')
    else:
        print(f'{p[0]} certamente é humano ou similar')
        hum += 1
print(galera)
print(f'Temos {naoehum} não humano[s] e {hum} humano ou algo similar')
print(f'O nome do[s] espectro[s] é {espectro}')
