print('=-'*30)
print('   BOLETIM   ')
boletim = []
while True:
    nome = str(input('Digite o NOME do aluno: '))
    nota1 = int(input('Digite a 1ª NOTA:  '))
    nota2 = int(input('Digite a 2ª NOTA:  '))
    media = (nota1+nota2)/2
    boletim.append([nome, [nota1,nota2], media])
    perg = str(input('Quer continuar: [S/N]'  ))
    if perg in 'Nn':
        break
print('=-'*30)
print(boletim)
print('=-'*30)
for pos, c in enumerate(boletim):
    print(f'Código identificador do aluno: {pos} \nO aluno {c[0].upper()} teve a média {c[2]}')
    print()
while True:
    perg = int(input('Quer visualizar as notas de qual aluno? Digite o codigo verif./ [999] interrompe:  '))
    if perg == 999:
        print('FINALIZANDO ... ')
        break
    elif perg <= (len(boletim)-1):
        print(f'As notas do aluno {boletim[perg][0].upper()} foram {boletim[perg][1]}')
    else:
        print('ERRO! Digite código identif. VÁLIDO')

print(boletim[0][1])
print(len(boletim))