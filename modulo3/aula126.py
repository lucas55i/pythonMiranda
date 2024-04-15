# __dict__ e vars para atibutos de instacias
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome =  nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade 

p1 = Pessoa('João', 32)
print(p1.__dict__)
print(vars(p1))