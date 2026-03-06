"""
 Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.
"""

def data_por_extenso(data: str) -> None:
    d = data.split('/')

    dia = d[0]
    mes = d[1]
    ano = d[2]

    if mes == '01':
        mes_str = 'Janeiro'
    elif mes == '02':
        mes_str = 'Fevereiro'
    elif mes == '03':
        mes_str = 'Março'
    elif mes == '04':
        mes_str = 'Abril'
    elif mes == '05':
        mes_str = 'Maio'
    elif mes == '06':
        mes_str = 'Junho'
    elif mes == '07':
        mes_str = 'Julho'
    elif mes == '08':
        mes_str = 'Agosto'
    elif mes == '09':
        mes_str = 'Setembro'
    elif mes == '10':
        mes_str = 'Outubro'
    elif mes == '11':
        mes_str = 'Novembro'
    elif mes == '12':
        mes_str = 'Dezembro'

    print(f'Data: {dia} de {mes_str} de {ano}')


if __name__ == '__main__':
    data_por_extenso('01/01/2024')
