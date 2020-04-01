#esse programa simula pagamentos em uma loja
print('{} {} {}'.format('=' *10,'LOJAS IZZET GUILD','='*10 ))
compras = float(input('Digite o valor das compras: R$ '))
print('O valor das compras foi de {}'.format(compras))
print('Digite o a forma de pagamento conforme a numeração seguinte: '
      '\n (1) À vista em espécie ou cheque '
      '\n (2) À vista no cartão'
      '\n (3) 2x no cartão'
      '\n (4) 3x ou mais no cartão')
forpag = int(input('Digite a forma de pagamento conforme numeração: '))
if forpag == 1:
    valorapagar = compras * 0.9
    print('O valor a pagar será de R$ {} com desconto de 10%'.format(valorapagar))
elif forpag == 2:
    valorapagar = compras * 0.95
    print('O valor a pagar será de R$ {} com desconto de 5%'.format(valorapagar))
elif forpag == 3:
    valorapagar = compras
    parcela = valorapagar / 2
    print('O valor a pagar será de R$ {} '.format(valorapagar))
    print('A parcela de pagamento será de {} SEM JUROS'.format(parcela))
elif forpag == 4:
    numeroparcelas = int(input('Digite o numero de parcelas: '))
    if numeroparcelas > 10:
        print('O numero maximo de parcelas é 10')
    if numeroparcelas<=10 and numeroparcelas>2:
        valorapagar = compras * 1.2
        parcela = valorapagar / numeroparcelas
        print('O valor a pagar será de R$ {} com juros de 20%'.format(valorapagar))
        print('A parcela de pagamento será de {}'.format(parcela))
    if numeroparcelas<=2:
        print('Digite 2 como opção para a forma de pagamento.')
elif forpag != 1 or 2 or 3 or 4 :
    print('Você digitou uma opção inválida para a forma de pagamento. Digite uma opção válida')

