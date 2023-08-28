"""
Iterando strings com while.
"""
nome = "Lucas Silva"

indice = 0
novo_nome = ""
while indice < len(nome): # iterando apartir do tamanho da string
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1
    # break
print(novo_nome)