# Exercícios com funções

"""
Crie um funçãp que mutiplica todos os argumntos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variavel.
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)



"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par opu ímpar
"""
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f"{numero} é par"
    return f"{numero} é impar"


print(par_impar(1))
print(par_impar(88))
print(par_impar(1902))
print(par_impar(8765))
print(par_impar(112353))