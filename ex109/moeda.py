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
