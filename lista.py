'''
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
'''

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U']
lista3 = []
lista4 = list(range(11))
lista5 = (list('Geek University'))




'''

# Revisão de slicing

#lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de listas com parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando do índice 1 e pegando os elementos restantes

print(lista[::]) # todos os elementos

print(lista[:2]) # Começa em 0, pega até o índice 2

print(lista[:4]) # Começa em 0, pega até o índice 4

print(lista[1::2]) # Começa em 1, vai até o final, 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, 2 em 2


# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista, será apresentado erro


# Podemos facilmente checar se determinado valor está contido na lista
num = 17
if num in lista4:
    print(f'Numero encontrado: {num}')
else:
    print(f'Numero {num} não encontrado\n')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrência em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Para adicionar elementos em listas, utilizamos a função append
print(lista1)
lista1.append(42) # Coloca elementos unicos
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista.append(12, 34, 56) # ERRO

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print(f'Encontrei a lista: {[8, 3, 1]}')
else:
    print('Não encontrado')

lista1.extend([123, 44, 67]) # coloca cada elemento da lista como valor adicional
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice

lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

lista1 = lista1 + lista2
print(lista1)

# Reverter lsita de numeros
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

print(lista1[::-1])
print(lista2[::-1])

# Copiar lista
lista6 = lista2.copy()
print(lista6)

# Contar tamanho da lista, quanto elementos na lista
print(len(lista1))
print(len(lista2))

# Podemos remover pelo índice
# obs: se não houver elemento no índice informado, teremos erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover o ultimo elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover todos os elementos, zerar a lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para lista
# Exemplo 1
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso2 = 'Programação,em,python:,Essencial'
print(curso2)
curso2 = curso2.split(',')
print(curso2)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

curso = ' '.join(lista6) # Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
print(curso)

curso = '$'.join(lista6)
print(curso)

# Iterando sobre listas
# Exemplo 1

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
     print('Adicione um produto na lista ou digite "sair" para sair')
     produto = input()
     if produto != 'sair':
         carrinho.append(produto)
for produto in carrinho:
    print(produto)


# Podemos utilizar variáveis em listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4

numeros = [num1, num2, num3, num4]
print(numeros)



# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul']

print(cores[0])
print(cores[1])
print(cores[2])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerar indice em um for

cores = ['verde', 'amarelo', 'azul']

for indice, cor in enumerate(cores):
    print(indice, cor)


# Lista aceita valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(23)
lista.append(11)

print(lista)

'''
