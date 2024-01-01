"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcaçavel
O escopo local é o escopo onde apenas nome do mesmo local 
podem ser alcançados

Não temos acesso a nomes de escopos internos nos espocos externos.
A palavra global faz uma variável do escopo externo ser a mesma no interno.
"""

x = 1


def escopo():
    x = 10

    def outra_fun():
        x = 12
        y = 2
        print(x + y)
    print(x)
    outra_fun()


escopo()
