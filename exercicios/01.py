primeiro_valor = int(input('Digite um valor: '))
segundo_valor =  int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor} é maior que {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O {segundo_valor} é maior que {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais')
else:
    print('Digite algo valido')