# Métodos em instancias de classes Python
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()