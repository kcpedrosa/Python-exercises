#o programa é uma calculadora de emprestimo imob. e diz se este foi aprovado
vc = float(input('Qual o valor da casa?: '))
salario = float(input('Digite aqui seu salario: '))
tempo = int(input('Digite em quantos anos ira pagar o débito: '))
prestação = vc / (tempo * 12)
print('Para pagar uma casa de R$ {:.2f} em {} ano(s) a prestação será de R$ {:.2f}'.format(vc, tempo, prestação))
if prestação > (salario * 0.3):
    print('O financiamento FOI NEGADO')
else:
    print('O financiamento FOI APROVADO')
