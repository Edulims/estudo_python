"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retorna uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já realizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- sum()
- count()
- e muito mais

# Exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python'
print(curso)

cores.append('roxo')
print(cores)

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Como definir função

"""


"""
Em Python, a forma geral de definir função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (snake case);
parametros_de_entrada -> Opcional, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais ou não;
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo yma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado
em python para definir blocos.

"""


# Definindo a primeira função
# Definição
def diz_oi():
    print('Oi!')

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;

"""

# Utilizando funções
# Chamada de execução, OBS: Nunca esqueça o () ao executar uma função.
diz_oi()

# Exemplo 2

def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()














