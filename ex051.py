#fazer uma PA
p = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da nossa PA: '))
extensao = int(input('Digite ate onde vai nossa PA: '))
enesimo = p + (extensao - 1) * razao
for c in range(p,enesimo+1,razao):
    print( ' {} '.format(c))
print('FIM')