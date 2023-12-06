"""
Faça uma lista de compras
o usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista
"""

lista = []

while True:
    input_usuario = input(
        'Selecione uma opção \n[i]nserir [a]pagar [l]listar: ')

    opcoes_validas = "ial"

    if input_usuario not in opcoes_validas:
        print("Digite uma opção valida")
        

    if input_usuario == 'i':
        item_digitado = input('Informe o que deseja ser adicionado: ')
        lista.append(item_digitado)

    elif input_usuario == 'a':

        if len(lista) == 0:
            print('Não há nada listado')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
            item_apagar = int(input
                              ('Informe o que deseja ser apagado: '))

            if item_apagar not in lista:
                print('O item não está na lista')
            else:
                lista.pop(item_apagar)
                print(lista)
    elif input_usuario == 'l':
        if len(lista) == 0:
            print('Não há nada listado')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
