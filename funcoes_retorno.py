"""
Funções com retorno


OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno da função.
Podemos passar a execução da função para outras funções.


# Exemplo função

def quadrado_7():
    print(7 * 7)

quadrado_7()

ret = quadrado_7()

print(ret)

# Vamos refatorar esta função para que ela de retorno o valor

def quadrado_7():
    return 7 * 7
# Criamos uma variável para receber o retorno da função. Não é obrigatório
ret = quadrado_7()
print(f'Retorno {ret}')
# ou pode ser assim
print(f'Retorno {quadrado_7() + 1}')


# Refatorando a primeira função

def diz_oi():
    return 'Oi'

alguem = 'Pedro!'

print(diz_oi(), alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 1

def diz_oi():
    return 'Oi'
    print('execução pos retorno') # linha pós return não é executada

print(diz_oi())



# Exemplo 2

def nova_funcao():
    variavel = False # True, None - Em uma função diferentes returns com condicionais
    if variavel:
        return variavel
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(type(outra_funcao()))


# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização de retorno em uma função, codificação desnecessária.

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True # não precisa de else, pq nesse caso só tem 2 possibilidade, evitar else sem necessidade
    return False

print(eh_impar())

"""















