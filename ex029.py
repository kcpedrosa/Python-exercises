velocidade = float(input('Qual a velocidade do carro? Digite aqui: '))
if velocidade > 80:
    print('Atenção! Você foi multado')
    print('Sua multa foi de R$ {}'.format((velocidade - 80) * 7))
else:
    print('Parabéns, você está dirigindo dentro dos limites da lei.')