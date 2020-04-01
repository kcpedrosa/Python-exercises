dados = [['Ishsan', 600], ['Tsabo', 200],['Slobad', 50]]
print(dados[0])
print(dados[0][1])
print('=-'*20)
for pos, c in enumerate(dados):
    print(f'{c[0]} que está na posição {pos}')
print()
for c in dados:
    print(f'{c[0]} que tem {c[1]} anos')