boletim = []
while True:
    nome = str(input('Digite o nome do aluno:  '))
    nota1 = float(input('Digite a primeira nota:  '))
    nota2 = float(input('Digite a segunda nota:  '))
    media = (nota1+nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    perg = str(input('Quer continuar? [S/N]  '))
    if perg in 'Nn':
        break
print(boletim)
print('=-'*30)
for pos, c in enumerate(boletim):
    print(f'{"Aluno número":<4} {pos:^30}')
    print(f'Nome do aluno : {c[0]}    Média : {c[2]}')
    print('=-'*30)

while True:
    print()
    perg2 = int(input('Quer visualizar as notas de qual aluno?  [999 interrompe]  '))
    if perg2 == 999:
        print('FINALIZANDO... ')
        break
    if perg2 <= len(boletim)-1:
        print(f'As notas do aluno {boletim[perg2][0]} foram {boletim[perg2][1]}')
