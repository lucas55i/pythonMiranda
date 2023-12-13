"""
Valores padrão para pparametros
Ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o parametro, o valor ppadrão será usado
Refatorar: editar o seu código
"""


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(2, 2)
soma(3, 5, 0)
