# @property - um getter no modo Pythonico
# getter - um método para obter um AttributeError
# cor -> get_cor()
# modo Pythonico - modo de Python de fazer as coisas
# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situa"oes:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

   
    
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)



# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta
    
# caneta = Caneta('Azul')
# print(caneta.get_cor())