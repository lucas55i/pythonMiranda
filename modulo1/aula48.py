"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# print('Valor' if True else 'Outro valor')

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

# digito = 9 # > 9 = 0
# digito igual a digito, caso for menor que 9, se não será 0
# novo_digito = digito if digito <= 9 else 0

# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)


nome = 'Lucas'
poder = True
up = poder if nome == "Lucas" else 'Não recebe poder' 
print(up)