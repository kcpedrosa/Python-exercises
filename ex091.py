from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)
         }
ranking = []
print('  JOGO DE DADO  ')
print(jogos)

for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
#se colocar o itemg no 0 vai aparecer jogador4 primeiro
print(ranking)
print('=-'*30)
for pos, c in enumerate(ranking):
    print(f'{pos+1}º lugar : {c[0]} com {c[1]} pontos no dado')
    sleep(1)
print('   FIM   ')


#COMO FAZER ESSE PROGRAMA IDENTIF OS EMPATES?
#jogo=0
#for c in range(0,4):
    #jogo = randint(1,6)
    #jogos['Numero']=jogo

#print(jogos)