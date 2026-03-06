"""
Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor

"""
def maior(inteiros: list) -> int:
    return max(inteiros)

if __name__ == '__main__':
    lista: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'O maior valor da lista {lista} é {maior(lista)}')