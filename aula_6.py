conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca1 = conjunto.discard(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença de 1 para 2: {}'.format(conjunto_diferenca1))
print('Diferença de 2 para 1: {}'.format(conjunto_diferenca2))


"""
conjunto = {1, 2, 3, 5 , 9 }
conjunto.add(5)
conjunto.discard(2)
print(conjunto)

"""