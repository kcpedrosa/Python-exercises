preço = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor percentual do desconto: '))
valorpromo = preço * (1 - (desconto/100))
print ('O produto que custava R$ {} , na promoção com desconto de {} %\n agora custa R$ {}'.format (preço, desconto, valorpromo))