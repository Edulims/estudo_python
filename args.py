"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis



def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(1, 2, 3))

# print(soma_todos_numeros(1, 2, )) # TypeError
# print(soma_todos_numeros(1, 2, 3, 4)) # TypeError

# Exemplos

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros("Edu", "edu@teste"))
print(soma_todos_numeros("Edu", "edu@teste", 1, 2, 3))
print(soma_todos_numeros('edu', 'edu@teste', 1, 2, 3, 4))
print(soma_todos_numeros('edu', 'edu@teste', 4, 5, 6, 7, 8, 9, 10))



# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Não tenho certeza quem você é ...'

print(verifica_info('Geek', 'University'))
print(verifica_info())
print(verifica_info('Eu', True, 22, 3.145, 'Geek'))
print(verifica_info('Eu', True, 'University', 22, 3.145, 'Geek'))


"""

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5]
# print(soma_todos_numeros(numeros)) # ERRADO
print(soma_todos_numeros(*numeros)) # CERTO, faz o Desempacotamento

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.








