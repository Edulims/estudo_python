"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui

"""

"""
listaB = [x * 2 for x in range(10)]
print(len(listaB))

for valor in listaB:
    if valor % 2 == 0:
        print(valor)
"""

lista: list[int] = []
contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f"Digite um valor {len(lista) + 1}/10: "))
    lista.append(valor)

for valor in lista:
    if valor % 2 == 0:
        contador_pares += 1

if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} números pares')
else:
    print(f'A lista {lista} não possui valor par')

