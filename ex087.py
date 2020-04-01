#exercicio de matriz baseado no anterior
somapar = mai = somacoluna = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
#l indica as listas secundarias, enquanto c indica a posição dos numeros dentro dessas lst secundarias
        matriz[l][c] = int(input(f'Digite um valor para o {(c)}º termo do {(l)}º grupo: '))
#a lógica foi absorvida, mas não automatizada e nem é intuitiva
print(matriz)
for l in range(0,3):
    for c in range(0,3):
        print(f' [{matriz[l][c]:^5}] ', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in range(0,3):
        somacoluna += matriz[l][2]
for c in range(0,3):
        if c == 0:
            mai = matriz[1][c]
        elif matriz[1][c] > mai:
            mai = matriz[1][c]
#vai calcular o valor da 2a linha
print('=-'*20)
print(f'A soma dos numeros PARES da matriz gerada é {somapar}')
print(f'A soma dos termos da TERCEIRA coluna é {somacoluna}')
print(f'O maior valor da 2a LINHA é {mai}')