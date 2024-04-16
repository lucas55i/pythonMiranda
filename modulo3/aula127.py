# Métodos de classe
# São métodos onde "self" será "cls", ou sejá,
# ao invés de receber a instacia no primeiro 
# parametro, recebemos a próripa classe

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    

ts = Pessoa.criar_com_50_anos('Lucas')
print(ts.nome)