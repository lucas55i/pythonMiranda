# Qual letra mais apareceu na frase com FOR
frase = "O Python é uma linguagem de programação " \
    "multiparadigma. " \
    "Python foi criado por Guido van Rossum."
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
for letra in frase:
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == " ":
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1
print(
    f"A letra que apareceu mais foi [{letra_apareceu_mais_vezes}], {qtd_apareceu_mais_vezes}")
