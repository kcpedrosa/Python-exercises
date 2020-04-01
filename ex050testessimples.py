for c in range(0,6):
    print('hello')
print('fim')
print(' ')
for c in range(6,0, -1):
    print(c)
print('fim')
print(' ')
for c in range(0,8, 2):
    print(c)
print('fim')
print(' ')
#atenção ao proximo codigo
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')
#anda, para e pula
i = int(input('Inicio:'))
f= int(input('Fim:'))
p = int(input('pulando de quanto em quanto:'))
for c in range(i,f+1, p):
    print(c)
print('FIM DO TESTE')