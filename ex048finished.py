soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        print(numero, end=' ')
        soma = soma + numero
        cont = cont + 1
        #voce pode escrever soma += numero e cont += 1 [soma ele mesmo + alguma coisa]

print('\nA soma é {}'.format(soma))
print('Foram somados {} valores'.format(cont))