print('SEQUENCIA DE FIBONACCI')
n = int(input('Quantos termos você quer mostrar?: '))
t1 = 0
t2 = 1
cont = 3
fibo=1
print('{} - > {}'.format(t1, t2), end=' ')
while cont <= n:
    t3 = t2 + t1
    print('-> {}'.format(t3), end=' ')
    cont=cont+1
    t1=t2
    t2=t3
print(' -> FIM')
#explicação
'''0       1       1
t1      t2      t3
t1=1
t2=1
logo t3=[2]
se t1=t2, t1=1
se t2=t3, t2=[2]
logo t3=3
t1=2
t2=3
logo t3=5
t1=3
t2=5
logo t3=8
t1=5
t2=8
logo t3=13'''