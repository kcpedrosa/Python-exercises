from time import sleep
cores = {'vermelhofbranco': '\033[31:40m',
        'azulmarifcinza': '\033[1:34:47m',
        'froxo': '\033[30:41m',
        'fciano': '\033[30:46m',
        'fverde': '\033[1:30:42m',
        'finv': '\033[7:30m',
        'famarelo': '\033[43m',
        'limpa': '\033[m'}


def ajuda(com):
    '''
    Retorna o HELP de alguma função ou biblioteca
    :param com: digite função ou biblioteca
    :return: no return
    '''
    titulo(f'Acessando o comando \'{com}\'...', "fciano")
    sleep(2)
    help(com)

def titulo(msg, cor="limpa"):
    tam = len(msg)+4
    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(cores["limpa"], end='')
    sleep(1)


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', "fverde")
    comando = str(input(f'{cores["vermelhofbranco"]} Digite uma FUNÇÃO ou BIBLIOTECA:  {cores["limpa"]}'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', "famarelo")