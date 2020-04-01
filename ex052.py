#vai dizer se o numero e primo
num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m')
        total = total + 1
    else:
        print('\033[31m')
    print( '{} '.format(c), end=' ')
print('\no numero {} foi divisivel {} vez[es]'.format(num, total))
if total == 2:
    print('Esse número é primo')
elif total != 2:
    print('Esse numero NAO e primo')
#verifique pasta python para codigo sem cores

