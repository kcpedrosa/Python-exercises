dias = int(input('Digite o número de dias alugados: '))
km = float(input('Digite o número de kilômetros rodados: '))
preçodia = dias * 60
preçokm = km * 0.15
print ('O total a pagar é R$ {:.2f}'.format(preçodia + preçokm))