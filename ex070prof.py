#Estatísticas em produtos
total = 0
mais1000 = 0
cont=0
menorpreço = 0
cheaper=''
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto em R$: '))
    total += valor
    cont += 1
    if cont == 1:
        menorpreço = valor
        cheaper = produto
    else:
    #o else pode ser subst por um OR no IF acima 'if cont == 1 OR valor < menorpreço
    #pois os comandos subsequentes sao iguais (OR=lembre de logica formal)
        if valor < menorpreço:
            menorpreço = valor
            cheaper = produto
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
print(f'O mais barato custa {menorpreço} e foi o {cheaper}')