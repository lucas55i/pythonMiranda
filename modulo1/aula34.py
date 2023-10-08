"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez 
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# numeros = range(0, 100, 8)
# for numero in numeros:
#     print(numero)


# for letra in txt
txt = 'lucas'  # iterável
iterador = iter(txt)  # iterator

while True:
    try:
        letra = next(iterador) # proximo valor da iteração.
        print(letra)
    except StopIteration:
        break

# ===============================
# Resumindo.
# for letra in txt:
#     print(letra)