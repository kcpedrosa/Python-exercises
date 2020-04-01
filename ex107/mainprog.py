from ex107 import moeda
#a chamada do prof foi from moeda import aumentar etc etc
#mas ele tb usou a cham acima no fim do video
#opção; colocar import ex107.moeda
preço = float(input('Digite o preço do produto: '))
taxa1 = int(input('Digite uma taxa de AUMENTO: '))
taxa2 = int(input('Digite uma taxa de DIMINUIÇÃO: '))
print(f'O valor do produto é  R$  {preço}')
print(f'O valor do produto com taxa de aumento é R$ {moeda.aumentar(preço,taxa1)}')
print(f'O valor do produto coom taxa de diminuição é R$ {moeda.reduzir(preço,taxa2)}')
print(f'A metade do valor do produto é R$ {moeda.metade(preço)}')
print(f'O dobro do valor do produto é R$ {moeda.dobro(preço)}')

#o prof usou taxas fixas, nao colocou input pra taxa ("aumentando em 10%...")
#colocou direto moeda.aumentar(preço,10) p ex