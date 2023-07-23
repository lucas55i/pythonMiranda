'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digitar um número inteiro,
informe que não é um número inteiro.
'''

numero = input('Digite um número inteiro: ')


try:
    numero_int = int(numero)
    resto = numero_int % 2
    if resto == 0:
        print('Número é par')
    else:
        print('Número é impar')
except:
    print('Isso não é um número inteiro')
