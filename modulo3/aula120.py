'''
class - Classes são moldes para criar novos objetos.
As classes geram novos objetoss (instancias) que podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe odem usar sesu dados 
internos para realizar várias ações.
Por convenção, usamos PAscalCase para nome de classes.
'''


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def teste(self):
        print(2)


p1 = Pessoa('Lucas', 'Silva')
print(p1.nome)
print(p1.sobrenome)
