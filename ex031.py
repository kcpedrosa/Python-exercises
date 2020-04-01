dist = float(input('Qual a distancia da sua viagem?: '))
print('Você está prestes a iniciar uma viagem de {} kilometros'.format(dist))
if dist <= 200:
    v1 = dist * 0.5
    print('O preço da passagem será R$ {}'.format(v1))
else:
    v2 = dist * 0.45
    print('O preço da passagem[viagens longas] será R$ {}'.format(v2))
#obs colocando a variavel como preço poderiamos escrever
#preço = distancia * 0.5 if distancia <=200 else distancia * 0.45 [operador ternario]