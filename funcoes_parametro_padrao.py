"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seha opcional;

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2))   # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva á potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parametro numero, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potencia,
#Então será calculada esta potência

"""

"""
# OBS: Em funções Pyton, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

Exemplo:
Errado
def teste(num=2, potencia):
    return num ** potencia

Certo
def teste(potencia, num=2):
    return num ** potencia


    
# Outros exemplos

def mostra_informacao(nome= 'Geek', instrutor=False):
    if nome == 'Geek' and instrutor: # True
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Paulo'))


# Por que utilizar parâmetro com valor default?

- Nos permite ser mais flexiveis na funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;
    

# Quais tipos de dados podemos utilizar como valores default para parâmetro?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;


# Exemplos

def soma(numero1, numero2):
    return numero1 + numero2

def mat(numero1, numero2, fun=soma):
    return fun(numero1 , numero2)

def sub(numero1, numero2):
    return numero1 - numero2

print(mat(2, 3))
print(mat(2, 3, sub))


# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # variável global

def diz_oi():
    instrutor = 'python' # variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com mesmo nome de uma globa, a variável local vai ter preferencia 
# OBS: A variável local só é reconhecida dentro do seu bloco

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa()


total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())




















