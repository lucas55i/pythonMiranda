"""
Calculadora com while
"""
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    numero_validos = None  # flag
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Digite um operador valido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador valido")
        continue

    print("Realizando sua conta.")
    if operador == "+":
        soma = num_1_float + num_2_float
        print(f"A soma entre {num_1_float} e {num_2_float} é {soma}")
    elif operador == "-":
        subtracao = num_1_float - num_2_float
        print(f"A subtração entre {num_1_float} e {num_2_float} é {subtracao}")
    elif operador == "*":
        multiplicacao = num_1_float * num_2_float
        print(
            f"A multiplicação entre {num_1_float} e {num_2_float} é {multiplicacao}")
    elif operador == "/":
        divicao = num_1_float / num_2_float
        print(f"A divisão entre {num_1_float} e {num_2_float} é {divicao}")
    else:
        print("Nunca deveria chegar aqui")
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
