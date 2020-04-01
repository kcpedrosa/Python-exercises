#Estatísticas em produtos
total = 0
mais1000 = 0
my_list=[]
my_list2=[]
cheaper=''
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto em R$: '))
    total += valor
    my_list += [valor]
    if valor == min(my_list):
        my_list2.append(produto)
    if valor > 1000:
        mais1000 += 1
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'NS':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print('=-'*20)
print('O valor total dos produtos foi R$ {}'.format(total))
print(f'Temos {mais1000} produto[s] que custam mais de R$ 1000')
#so falta o nome do produto MAIS BARATO
print(f'O mais barato foi {my_list2}')