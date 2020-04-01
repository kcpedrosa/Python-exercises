# Maior e menor da sequência
lst=[]
for pessoa in range(1, 4):
    peso = float(input('Digite o peso da {}ª pessoa em kgs: '.format(pessoa)))
    lst+=[peso]
    print('O valor do peso da {}ª pessoa é {} kgs'.format(pessoa, peso))
print('O maior peso foi {} kgs'.format(max(lst)))
print('O menor peso foi {} kgs'.format(min(lst)))
