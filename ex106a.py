#essa é  uma versão simplificada do 106, apenas pra evidenciar a lógica
def ajuda(com):
    help(com)


#programa principal
comando = ''
while True:
    comando = str(input('Biblioteca ou Função >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

