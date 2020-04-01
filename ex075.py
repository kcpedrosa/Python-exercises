#Análise de dados em uma Tupla
numeros = (int(input('Digite o 1º numero: ')), int(input('Digite o 2º numero: ')),
           int(input('Digite o 3º numero: ')), int(input('Digite o 4º numero: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O primeiro numero 3 está na {numeros.index(3)+1}ª posição')
else:
    print(f'O numero 3 não foi digitado')
print('Os numeros pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print([n], end=' ')
