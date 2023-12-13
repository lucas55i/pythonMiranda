"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
por padrão, funções Python retornam None (nada).
"""

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)