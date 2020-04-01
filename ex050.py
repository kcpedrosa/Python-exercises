#Soma dos pares dentre tres numeros
#nao precisa usar cont
soma = 0
cont = 0
for c in range(0,3):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('A some é dos num pares é:')
print(soma)
print('Vc informou {} numero[s] par[es]'.format(cont))