teste = []
teste.append('Ishsan')
teste.append(600)
galera = []
galera.append(teste[:])
teste[0] = 'Tsabo'
teste[1] = 200
galera.append(teste[:])
print(galera)
#tem que fazer uma copia pra criar duas listas=use [:]
#se nao colocar [:] vai criar DUAS listas 'Tsabo , 200' dentro da lista maior