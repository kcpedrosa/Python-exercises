num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    print('{}'.format(c))
    if num % c == 0:
        total = total + 1
print('O numero {} é divisivel {} vez[es]'.format(num, total))
if total == 2:
        print('{} é um numero primo'.format(num))
else:
        print('{} NAO é um numero primo'.format(num))
