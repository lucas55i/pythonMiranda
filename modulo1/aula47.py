# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Luiz']
tupla = ('Python', 'é', 'legal')


# a, b, c = lista
# print(a, c)

print(*lista)  # FODA
for nome in lista:
    print(nome)


