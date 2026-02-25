"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

    # Forma 1
paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
print(paises, '\n')

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))



paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
# Acessando elementos

# Forma 1
print(paises['br'])
print(paises['eua'])

# Forma 2 - Acessando via get (recomendado)
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('py'))
print(paises.get('ru')) # None, não existe na coleção

paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
print(paises.get('br'))
print(paises.get('eua'))
pais = paises.get('ru')

if pais:
    print(f'{pais} - Encontrado ')
else:
    print('País não encontrado')


# Podemos definir um valor padrão, para casos não encontremos objetos com a chave informada
paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}

pais = paises.get('py', 'Não existe')

print(f'{pais} - Encontrado ')


paises = {'br' : 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
# Podemos verificar se determinada chave se encontrado em um dicionário
print('br' in paises)
print('Brasil' in paises) # Isso é valor e não chave, a busca é pela chave
print('ru' in paises)



# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla e dicionários , como chaves
#de dicionários.

# Tuplas, por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas
#são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))




# Adicionar elementos em um dicionário

receita = {'jan' : 100, 'fev' : 120, 'mar' : 300}
print(receita)
print(type(receita))

# Forma 1 - mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai' : 500}
receita.update(novo_dado) # receita.update({'mai' : 500})
print(receita)


# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai' : 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos e modificar dados de um dicionário é a mesma
# CONCLUSÃO 2: Não podemos ter chaves repetidas


# Remover dados de um dicionário

receita = {'jan' : 100, 'fev' : 120, 'mar' : 300}
print(receita)

#Forma 1
ret = receita.pop('mar') # podemos usar apenas receita.pop('mar'), mas ae se perde o valor retornado associado a chave eliminada
print(ret)

print(receita)

#OBS: Precisamos informar a chave, caso não encontre = KeyError
#OBS2: Ao remover um objeto o valor desse objeto é retornado.

# Forma 2
del receita['fev']
print(receita)

# Se a chave não existir mais ao tentar remover vai dar KeyError
# OBS: Neste caso o valor removido não é retornado


"""

# Imagine um comércio eletrônico / e-commerce, onde tem carrinho de compras, add produtos
"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
    - nome;
    - quantidade;
    - preço;
    
    
    # 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome' : 'Playstation 4', 'quantidade' : 1, 'preco' : 2300.00}
produto2 = {'nome' : 'God of War 4', 'quantidade' : 1, 'preco' : 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação


# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)


# Copiando um dicionário para outro

# Forma 1 # Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)
print(d)

# Forma 2 # Shallow Copy

novo = d
print(novo)

novo['d'] = 4 # altera o dicionário original e o novo
print(novo)
print(d)

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# O método fromkeys recebe dois parãmetro: um interável e um valor.
# Ele vai gerar para cada valor iterável uma chave  irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

"""





















