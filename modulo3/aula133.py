# Relações entre classes: associação, agregaçaão e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geramente é uma relação de um para muitos, onde um 
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relção onde um objeto precisa de 
# outro para determinada tarefa.
# (exitem contevérias sobre as definições de agregação)

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self,*produtos):
            self._produtos.extend(produtos)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camisa', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())