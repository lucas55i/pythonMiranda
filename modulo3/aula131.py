# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = public 
#         pode ser usado em qualuer lugar
# _   (um underline) = protected
#         não DEVE ser usado fora da classe.
#         ou suas subclasses.
# __ (dois underlines) = private
#     "name mangling" (desfiguração de nomes) em Python
#     só DEVE ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.public =  'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo =  'isso é privado'

    def metodo_publico(self):
        return "metodo_publico"
    
    def _metodo_protected(self): 
        return '_metodo_protected'

    def __metodo_private(self):
        return '__metodo_private'

f = Foo()
# print(f.metodo_publico())
print(f._metodo_protected())
print(f.__exemplo)