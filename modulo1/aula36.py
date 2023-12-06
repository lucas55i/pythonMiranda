"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, inser, pop, del, clear, extend, +
"""
# ......01234
# .......54321

# string = 'ABCDE'  # 5 caracteres
# lista = [123, True, 'Lucas', 1.2, [1,2,3]]
# print(lista)

lista_a = [10, 20, 30, 40]
lista_b = [50, 60, 70, 80]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)


# ---
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# ------
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista)
# -----

# lista.insert(0, 5)
# print(lista)
