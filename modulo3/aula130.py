# @property + @setter - getter e setter no modo pythonico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um 
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        # print("PROPERTY")
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        # if valor == 'Rosa':
        #     raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

    
def mostrar(caneta):
    return caneta.cor

   
    
caneta = Caneta('Azul')
caneta.cor = 'Rosa-'
caneta._cor_tampa = 'Vermelho'
print(caneta.cor_tampa)
