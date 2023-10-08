"""
Faça um jogo para o usuário adivinhar qual é a palavra secreta.

- Voce vai propor uma palara secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, voce vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta/ exiba a letra
    - Se a letra digitada não estiver na palavra secreta exxiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = 'lucas'
letras_acertadas = ''
tentativas = 0

while True:
    letra_tentativa = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_tentativa) > 1:
        print("Digite apenas uma letra")
        continue

    if (letra_tentativa in palavra_secreta):
        letras_acertadas += letra_tentativa

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Ganhou')
        print('A palavra era ', palavra_formada)
        print('Tentativas: ', tentativas)
        break
