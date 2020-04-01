#calcular passagens, se até 200km custa x0.5, além custa x0.45
dist = float(input('Qual a distancia da sua viagem? Digite: '))
print('Voce esta prestes a iniciar uma viagem de {} kilometros'.format(dist))
valor = dist * 0.5 if distancia <= 200 else valor = dist * 0.45
print('O preço que voce tera de pagar é R$ {}'.format(valor))
