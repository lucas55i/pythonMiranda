"""
 Operadores lógicos
 and (e) or (or) not (não)
 and - Todas as condições precisam ser verdadeiras.
 se qualquer valor for considerado falso, a expressão inteira  será avaliada naquele valor.
 São consideradoes falsy (que vc já viu)
 0 0.0 '' false
 Também existe o tipo None que é usado para representar um não valor.
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitada = '12345'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitada:
    print('Entrar')
else:
    print('Sair')

# print(True and False and True)
