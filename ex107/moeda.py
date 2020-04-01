def aumentar(valor=0, taxa=1):
    r =  valor + (valor * (taxa/100))
    return r

def reduzir(valor=0, taxa=1):
    r = valor - (valor * (taxa/100))
    return r

def dobro(valor=0):
    r = valor * 2
    return r

def metade(valor=0):
    r = valor/2
    return r