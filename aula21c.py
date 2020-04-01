cores = {'fverde':'\033[42m',
         'fciano':'\033[46m',
         'limpa':'\033[m'}

def fatorial(n=1):
    f = 1
    for c in range(n, 0 ,-1):
        f = f * c
    return f

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


n = int(input('Digite um valor para n: '))
print(f'O fatorial de {n} é {fatorial(n)}')
f1 = fatorial(4)
f2 = fatorial(5)
print(f'{cores["fciano"]}Os valores dos fatoriais requisitados são {f1} e {f2} {cores["limpa"]}')

num = int(input('Digite um número pra saber se é par: '))
if par(num) == True:
    #se eu digitar if par(num): tb func, assim o prof fez
    print('É par')
else:
    print('É impar')