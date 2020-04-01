#vai testar a importação de um pacote fora do ex111
#atentar para o fato de que o teste está no ex111
from UtilidadesCeV import moeda

preço = float(input('Digite o preço do produto: '))
taxa1 = int(input('Digite uma taxa de AUMENTO: '))
taxa2 = int(input('Digite uma taxa de DIMINUIÇÃO: '))

moeda.resumo(preço, taxa1, taxa2)
