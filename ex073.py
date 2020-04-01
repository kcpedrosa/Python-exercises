#Tuplas com Times de Futebol
tipos = ('Izzet','Golg','Azor','Boros','Zombie','Angel','Goblin','Troll',
         'Wizard','Rats')
print(tipos)
print('=-'*20)
print(f'Em ordem alfabética: {sorted(tipos)}')
print('=-'*20)
print(f'Os quatro primeiros são {tipos[0:4]}')
print(f'Os quatro últimos são {tipos[-4:]}')
#obs um em baixo do outro
for t in tipos:
    print(t)
print(f'O Zombie está na {tipos.index("Zombie")+1}ª posição')