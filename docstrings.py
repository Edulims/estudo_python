"""
Documentação funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help()
"""

# Exemplo

def diz_oi():
    """Uma função simples que retorna a string 'Oi!' """
    return 'Oi!'

# print(diz_oi.__doc__) # Acesso a documentação de uma função



def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

# print(exponencial.__doc__)
help(exponencial)