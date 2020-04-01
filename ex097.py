#esse programa ira fazer um print especial
def escreva(msg):
    tam = len(msg)+5
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


#abaixo segue o PROGRAMA PRINCIPAL
escreva('Vampires everywhere')