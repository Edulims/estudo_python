"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

from collections import deque

deq = deque('geek')
print(deq)

# Adicionado elementos no deque
deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('k') # Adiciona no começo da lista
print(deq)

# Remover elementos
print(deq.pop()) # remove e retorna o ultimo
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)


