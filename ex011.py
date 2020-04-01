largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print ('Sua parede tema dimensão de {} m x {} m e sua área é igual a {:.2f} m²'.format(largura, altura, area))
print ('Para pintar essa parede, você vai precisar de {} litros de tinta'.format(tinta))