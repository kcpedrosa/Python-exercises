#Maior e menor da sequência
maior=0
menor=0
for pessoa in range(1,4):
    peso = float(input('Digite o peso da {}ª pessoa em kgs: '.format(pessoa)))
    print('O valor do peso da {}ª pessoa é {} kgs'.format(pessoa, peso))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} kgs e o menor {} kgs'.format(maior, menor))


