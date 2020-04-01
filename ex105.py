def notas(*n, sit=False):
    '''
    --->Função analisa notas de alunos
    :param n: qualquer numero de notas
    :param sit: opcional, mostra a situação
    :return: r
    '''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit == True:
        if r['média'] >= 7:
            r['sit'] = 'BOA'
        elif r['média'] >= 5:
            r['sit'] = 'RAZOAVEL'
        else:
            r['sit'] = 'RUIM'
    return r


resp = notas(9,6.9,6.5, sit=True)
print(resp)

help(notas)