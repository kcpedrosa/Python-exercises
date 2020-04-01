#trabalhando com listas [que sao mutaveis]
num = [1,3,9,7]
num.pop(0)
#pop tira o ultimo se nao houver parametro, se houver, tira o num na posic indicada
num.append(2)
#o append coloca o 2 no fim da lista
num.insert(1,2)
#na posição 1 insere o valor 2, se colocar uma pos que NAO existe nao vai inserir
num.remove(2)
#remove o primeiro 2, mas dá pra remover todos os 2 com LAÇOS
#SE mandar remover valor que N consta da lista,dá erro. pode-se resolver assim:
if 4 in num:
    num.remove(4)
else:
    print('Não achei o valor 4')
print(num)
