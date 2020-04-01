print('Gerador de PA')
print('=-' * 15)
primeiro = float(input('Digite o valor do primeiro termo: '))
razao = float(input('Digite o valor da razao: '))
limite = int(input('Digite até onde vai a PA[numero de termos]: '))
cont = 1
while cont <= limite:
    print( '{:.2f} ->'.format(primeiro), end=' ')
    primeiro = primeiro + razao
    cont = cont + 1
print('FIM')
print('Sua PA tem {} termo[s]'.format(limite))