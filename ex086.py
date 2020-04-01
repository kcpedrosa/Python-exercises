#O programa vai salvar valores e mostrar em formato de matriz 3X3
#ver aula 17 c
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz [l] [c] = int(input(f'Digite um valor para {l}, {c} :'))
print(matriz)
#print(matriz[0])
#print(matriz[1])
#print(matriz[2])
#assim fica sem estrutura (=feio)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
