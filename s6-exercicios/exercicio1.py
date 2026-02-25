"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.

"""

"""
valores = list(range(6))
print(valores)

for valor in valores:
    print(valor)
"""

lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f"Digite um valor {len(lista) + 1}/6: "))
    lista.append(valor)

for valor in lista:
    print(valor)