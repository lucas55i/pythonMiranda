# Exercício
# Peça ao usuário para digitar seu nome.
# Peça ao usuário para digitar sua idade.
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é
#         Seu nome invertido é
#         Se nome contem (ou não) espaços
#         Seu nome tem n letras.
#         A primeira letra do seu nome é
#         A última letra do seu nome é
# Se nada for digitado em nome ou idade:
#     exiba ¨Descukpe, voce deixou camposn vazios.¨

nome = input('Digite Seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Se nome contem espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: ¨{nome[0]}¨')
    print(f'A Útima letra do seu nome é: ¨{nome[-1]}¨')
else:
    print('Desculpe, voce deixou campos vazios')
