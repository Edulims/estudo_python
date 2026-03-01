"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados detro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Possuem entrada e saída;

"""
from traceback import print_tb

"""
# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2  # elevado ao quadrado

print(quadrado(2))
print(quadrado(3))
print(quadrado(7))
print(quadrado(4))
print(quadrado(6))
"""

"""
# Refatorando uma função

def cantar_parabens(aniversariante):
    print('Parabens para você!')
    print('Nesta data querida')
    print(f'Muitas felicidades {aniversariante}')
    print('Muitos anos de vida.')

cantar_parabens('Edu')
"""

"""
# Funções pode ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return(num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError
"""

"""
# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} e {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))


# A diferença entre parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função:
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa!
"""

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        #return total - local errado do return
    return total # bloco do for finaliza e depois executa o return, return finaliza a função

lista = [1, 2, 3, 4, 5]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5)
print(soma_impares(tupla))



