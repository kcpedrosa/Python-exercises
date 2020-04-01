#a aula é sobre tuplas
lanches = ('Hamburguer','Suco','Empada', 'Kibe' )
sushi = ('Tekka', 'Kappa')
juntos = sushi + lanches
#como coloquei sushi primeiro, o prg vai printar tekka e kappa antes
print(lanches[:2])
#o python sempre exclui o ultimo termo, entao vai do 0 ao 1
print(lanches[-2])
#o kibe é  -1, a empada é -2 etc
print(lanches[:-2])
#foi do 0 ate o 1 e excluiu o -2 [ou o 2] que é a empada
#atenção abaixo
#lanches[1] = 'Cana'
#vai dar erro, tuplas sao IMUTAVEIS : TypeError: 'tuple' object does not support item assignment
for comida in lanches:
    print(f'Eu vou comer {comida}')

print(len(lanches))
#vai dizer que tem 4 comidas
for c in range(0, len(lanches)):
    print(c, end=' ' )

print('\nAtenção:')

for c in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[c]}')
print('\n')

#enumerate e range dão a POSIÇÃO do elemento
print('USO DO ENUMERATE')
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')
print('\n')
for c in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[c]} na posição {c}')

print('\n')
#sorted coloca em ordem ALFABETICA
print(sorted(lanches))
print(juntos)