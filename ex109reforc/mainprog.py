from ex109reforc import moeda
#exerc refeito pra reforçar
preço = float(input('Digite o preço do produto: '))
taxa1 = int(input('Digite uma taxa de AUMENTO: '))
taxa2 = int(input('Digite uma taxa de DIMINUIÇÃO: '))
#o primeiro moeda é o nome do módulo e o segundo é o da função[abaixo]
#o preço abx está em dolar apenas pra testar o 2nd parâmetro
print(f'O valor do produto é    {moeda.moeda(preço,"U$")}')
print(f'O valor do produto com taxa de aumento é  {moeda.aumentar(preço,taxa1, True)}')
print(f'O valor do produto coom taxa de diminuição é  {moeda.reduzir(preço,taxa2, False)}')
print(f'A metade do valor do produto é  {moeda.metade(preço,)}')
print(f'O dobro do valor do produto é  {moeda.dobro(preço, True)}')

#o prof usou taxas fixas, nao colocou input pra taxa ("aumentando em 10%...")
#colocou direto moeda.aumentar(preço,10) p ex