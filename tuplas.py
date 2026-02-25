"""
# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)


# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)



# iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)



# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Agosto'))


"""








