"""
Módulo Collections - Counter (Contador)

Collections -> High-peformancve Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor
quantidade de ocorrências desse elemento


# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 42, 34, 49]

res = Counter(lista)

print(res) # Counter({1: 5, 2: 4, 4: 4, 3: 3, 5: 3, 45: 2, 66: 1, 42: 1, 34: 1, 49: 1})
print(type(res))

# Par cada elemento da lista criou uma chave, e colocou como valor a quantidade de ocorrência

print(Counter('Geek University'))

"""

from collections import Counter

texto = """ "Blank Space" é uma canção da artista musical estadunidense Taylor Swift para o seu quinto álbum de estúdio,
1989. Composta pela artista com os colaboradores Max Martin e Shellback, tendo sido também produzida pelos dois últimos. 
Foi lançada oficialmente como o segundo single do disco em 10 de novembro de 2014 pela Big Machine Records, e promovida pela Republic Records.
A sua gravação ocorreu em 2014 nos MXM Studios em Estocolmo, Suécia, e nos Conway Recording Studios, em Los Angeles, Estados Unidos.
No mesmo dia seu lançamento, foi enviada para várias estações de rádio estadunidenses.
Foi posteriormente comercializada em formato físico e digital.
Em 2023, após uma disputa acerca da posse de seus masters, foi lançada uma regravação de "Blank Space",
com o subtítulo "Taylor's Version", e incluída como parte do álbum de regravação de 1989."""

palavras = texto.split() # Transforma o texto em lista
print(type(palavras))

res = Counter(palavras)
print(res)

print(res.most_common(5)) # Encontrando as 5 palavras com mais ocorrência no texto







