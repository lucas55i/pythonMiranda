"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversuib flags - !r !s !a
"""

variavel = 'Start'
print(f'{variavel: >10}')
print(f'{variavel:=^20}') 
print(50* '-')
print(f'{10000.12314124234:.2f}')