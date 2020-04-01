#definir uma função para calcular área
def area(larg, comp):
    a = larg * comp
    print(f'A ÁREA de um terreno de {larg} X {comp} equivale a {a} m²')



#Programa principal
print('Controle de terrenos - Cálculo da área')
print('=-'*30)
l = float(input('Digite a LARGURA em METROS:  '))
c = float(input(('Digite o COMPRIMENTO em METROS:  ')))
area(l,c)
