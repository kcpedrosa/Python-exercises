print('Gerador de PA')
print('=-' * 15)
primeiro = float(input('Digite o valor do primeiro termo: '))
razao = float(input('Digite o valor da razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print( '{:.2f} ->'.format(primeiro), end=' ')
        primeiro = primeiro + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer? '))
print('FIM')
print('Sua PA tem {} termo[s]'.format(total))