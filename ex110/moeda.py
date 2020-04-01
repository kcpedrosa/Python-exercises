def aumentar(valor=0, taxa=1, formato=False):
    r = valor + (valor * (taxa/100))
    return r if formato is False else moeda(r)


def reduzir(valor=0, taxa=1, formato=False):
    r = valor - (valor * (taxa/100))
    return r if formato is False else moeda(r)


def dobro(valor=0, formato=False):
    r = valor * 2
    return r if not formato else moeda(r)


def metade(valor=0, formato=False):
    r = valor/2
    return r if not formato else moeda(r)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')

def resumo(amount=1, taxa1=1, taxa2=1):
    texto = '              RESUMO DO VALOR              '
    print('='*len(texto))
    print(texto)
    print('='*len(texto))
    print(f'Preço do produto analisado: \tR$ {amount:.2f}'.replace('.',','))
    d = amount * 2
    print(f'Dobro do preço: \t\t\t\tR$ {d:.2f}'.replace('.',','))
    m = amount / 2
    print(f'Metade do preço: \t\t\t\tR$ {m:.2f}'.replace('.',','))
    aum = amount + (amount*(taxa1/100))
    print(f'Com {taxa1}% de aumento: \t\t\tR$ {aum:.2f}'.replace('.',','))
    dim = amount - (amount*(taxa2/100))
    print(f'Com {taxa2}% de diminuição: \t\t\tR$ {dim:.2f}'.replace('.',','))
    print('='*len(texto))
#OBS abaixo vai a função RESUMO2, quase igual a do prof

def resumo2(preço, taxa1, taxa2):
    print('='*40)
    print('RESUMO DO VALOR'.center(40))
    print('='*40)
    print(f'Valor do produto: \t\t{moeda(preço)}')
    print(f'Dobro do valor: \t\t{dobro(preço, True)}')
    print(f'Metade do valor: \t\t{metade(preço, True)}')
    print(f'Com {taxa1}% de aumento: \t{aumentar(preço,taxa1,True)}')
    print(f'Com {taxa2}% de redução: \t{reduzir(preço, taxa2, True)}')
    print('='*40)
