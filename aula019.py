pessoa = {'nome':'Ishsan', 'idade':'600', 'sexo':'M'}
print(pessoa)
print(pessoa['idade'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
#del pessoa['sexo']
#pessoa['nome']='Sengir'
#vai mudar o nome de Ishsan para Sengir
pessoa['peso']=200
for k, v in pessoa.items():
    print(f'{k} = {v}')