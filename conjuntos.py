"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não
nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos e Mapas (Dicion´rios) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

    # Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que tem repetições
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum
z = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(z)
print(type(z))

# Podemos verificar se determinado elemento esta no conjunto
if 3 in z:
    print('Tem o 3')
else:
    print('Não tem.')



# Importante lembrar que, além de não termos valores duplicados, não temos ordem

dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

lista = list(dados) # lista aceita valores duplicados
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = tuple(dados) # tuplas aceita valores duplicados
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys(dados, 'dict') # dicionario não repete chave
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto = set(dados) # conjunto não repete valores
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)


# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas que temos.
# Podemos utilizar o set para isso:

cidades_unicas = set(cidades)
print(cidades_unicas)
print(len(cidades_unicas))
# ou
print(len(set(cidades)))


# Adicionando elementos em um conjunto
s= {1,2,3}

s.add(4)
s.add(4) # Duplicidade não gera erro
print(s)


# Remover elementos em um conjunto
s = {1, 2, 3}

# Forma 1
s.remove(3) # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2
s.discard(22) # Caso valor não encontrado nenhum erro é gerado.
print(s)

# Copiando um conjunto para outro...
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)


# Copiando um conjunto para outro...
s = {1, 2, 3}
print(s)

# Forma 2 - Shallow Copy
novo = s

novo.add(4)
print(novo)
print(s)


s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Pyton também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - utilizando union
#unicos1 = estudantes_python.union(estudantes_java)
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# *Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""





















