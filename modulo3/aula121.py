# Métodos em instancias de classes Python
# Hard coded - É algo que foi diretamente escrito no código.
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()