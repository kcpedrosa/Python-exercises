#situação de notas de alunos usando DICIONARIOS
aluno = {}
aluno['Nome'] = str(input('Nome:  '))
aluno['Media'] = float(input(f'Média do(a) {aluno["Nome"]}: '))
#tb funciona assim: aluno['media'] = float(input('Media do aluno: '))  [sem f string]
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Em Recuperação'
elif aluno['Media'] < 5:
    aluno['Situação'] = 'REPROVADO'

print('=-'*30)
print(aluno['Situação'])
for k, v in aluno.items():
    print(f'=== {k} é igual a {v}')