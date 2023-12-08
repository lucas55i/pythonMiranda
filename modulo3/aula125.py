# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando...")
            return

        print(f"{self.nome} está filmando...")
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando...")
            return

        print(f"{self.nome} está parando filmando...")
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar filmando...")
            return

        print(f"{self.nome} está fotografando...")


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.fotografar()
c1.filmar()
c1.parar_filmar()
print("--------")
c2.fotografar()
c2.filmar()
c2.parar_filmar()
# c1.filmar()
