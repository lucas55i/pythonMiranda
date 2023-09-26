# Operadores in e not in 
# Strings são iteráveis
# 0 1 2 3 4 5
# L u c a s
# -6-5-4-3-2-1

# nome = "Lucas vai a casa da mãe dele, onde ele não gosta de ficar muito tempo, pois sente energia estranhas."
# print(nome[2])
# print('u' in nome)
# print(10* '-')
# print('s vai' not in nome)
# print('e ele' in nome)

nome = input('Digite seu nome: ')
encontrar = input('O que vc quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'"{encontrar}" não está em {nome}')