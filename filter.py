"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))
print(media)


# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável

res = filter(lambda x: x > media, dados)
print(type(res)) #filter object - objeto proprio nome filter
print(list(res))

#OBS: Assim como na função map(), após ser utilizados os dados de filter() eles são excluidos da memória.


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, paises)

print(list(res))



paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

#res = filter(lambda pais: len(pais) > 0, paises)
#res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))


-----------------------

# A diferença entre map e filter

# map() -> Recebe dois paâmetro, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrado apenas os elementos de acordo com a função

------------------------

# Exemplo mais complexo
usuarios = [
    {'usename': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'usename': 'carla', 'tweets': ['Eu amo meu gato']},
    {'usename': 'jeff', 'tweets': []},
    {'usename': 'bob123', 'tweets': []},
    {'usename': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'usename': 'gal', 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter
#print(usuarios)

# Forma 1
#inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
#ativos = list(filter(lambda usuario: len(usuario['tweets']) > 0, usuarios))
#print(inativos)
#print(ativos)


# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

------------------------------------

"""


# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)



