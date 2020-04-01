expr = str(input('Digite uma expressão algébrica:  '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            #e se eu nao por o BREAK? testar

if len(lista)==0:
    print('Expressão válida')
else:
    print('Expressão INVÁLIDA')
