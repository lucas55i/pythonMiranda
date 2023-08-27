"""
Reptições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
Operadores de atribuição.
= += -= *= /= //= **= %=
"""
contador = 0
while contador <= 100:
    contador += 1

    if contador == 6:
        # print("NÃO VOU MOSTRAR O 6")
        continue

    if contador >= 10 and contador <= 27:
        # print("NÃO VOU MOSTRAR do 10 ao 27")
        continue


    print(contador)

    if contador == 40: 
        break

