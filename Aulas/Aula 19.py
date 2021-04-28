#Dicionários: 
#São semelhantes as tuplas e as listas, porém não usa somente indices númericos, e sem literais
#Para declarar um dicionário se usa {} ou dados = dict()
#Para calocar os dados dentro do dicionário e indentificalos se faz:
#dados = {'nome':'Pedro','idade':25}
#Para dar print é print(dados['nome'])
#Para adicionar um elemento faz:
#dados['sexo'] = 'M' 
#Para remover elementos:
#deldados['idade']
#Valores,chaves e itens: (usa nos laços)
#dados.values() (Valores são os elementos dentro do dicionário )
#dados.keys() (Chaves são os 'indices' do dicionário)
#dados.items() (Acessa tantos os valores quanto as chaves)
dados = {'nome':'Ana','idade':20,'sexo':'Feminino'} #declarando dicionários
print(dados)
print('-=-'*20)
print(f'A {dados["nome"]} tem {dados["idade"]} anos') #mostrando elementos 
print('-=-'*20)
print(dados.keys()) #acessando as keys
print('-=-'*20)
print(dados.values()) #acessando os valores
print('-=-'*20)
print(dados.items()) #acessando os itens do dicionário
print('-=-'*20)
for k , v in dados.items(): #acessando os itens por laços
    print(f'{k} = {v}')
print('-=-'*20)
Brasil = [] #lista
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'} #dicionário 1
estado2 = {'uf':'São Paulo','sigla':'SP'} #dicionário 2
Brasil.append(estado1) #adicionando dicionário 1 a lista
Brasil.append(estado2) #adicionando dicionário 2 a lista
print(Brasil[1]['sigla']) #acessando itens dentro do dicionário através da lista
print('-=-'*20)
estado = dict()
br = list()
for c in range(0,3):
    estado['ufd'] = str(input('Unidade federativa: ')) #Lendo do usuário e add no dicionário
    estado['sigla'] = str(input('Sigla do estado: ')) #Lendo do usuário e add no dicionário
    br.append(estado.copy()) #dacionando uma cópia do dicionário a lista
print(br)
for e in br:
    for k,v in e.items():
        print(f'O estado {estado["ufd"]} tem valor {estado["sigla"]}.') #dúvida
