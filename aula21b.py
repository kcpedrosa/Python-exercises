cores = {'vermelhofbranco': '\033[31:40m',
        'azulmarifcinza': '\033[1:34:47m',
        'froxo': '\033[30:41m',
        'fciano': '\033[30:46m',
        'fverde': '\033[1:30:42m',
        'finv': '\033[7:30m',
        'famarelo':'\033[43m',
        'limpa':'\033[m'}

def soma(a=0,b=0,c=0):
    soma = a + b + c
    print(f'A soma vale {soma}')


def soma2(a=0,b=0,c=0):
    soma2 = a + b + c
    return soma2


#programa principal
print(cores["fverde"])
soma(1,2,3)
soma(8,5)
soma(9)
print(cores["limpa"])
#como tirar essa barra verde longa?
#os resultados são padronizados, compare com abaixo

r1 = soma2(1,4,5)
r2 = soma2(7,7,7)
print(f'{cores["fciano"]}O resultado das minhas somas foram {r1} e {r2} {cores["limpa"]}')
#perceba que aqui há mais possibilidades de customizc de como mostr o resultado