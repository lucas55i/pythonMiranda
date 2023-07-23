'''
Faça um programa que pergunte a horas ao usuário e, 
baseando-se no horário descrito, exiba a saudação apropriada

Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''

hora_atual = int(input('Digite a hora atual(Número Inteiro): '))

try:
    numero_int = int(hora_atual)
    if numero_int >= 0 and numero_int <= 11:
        print('Bom Dia!')
    elif numero_int >= 12 and numero_int <= 17:
        print('Boa Tarde!')
    elif numero_int >= 18 and numero_int <= 23:
        print('Boa Noite!')
    else:
        print(f'A {numero_int} não é uma hora valida')
except:
    print('Não é um número inteiro')
