from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte

    def mostrar(self):
        return f"Cachorro: {self.getNome()}, Idade: {self.getIdade()}, Porte: {self.__porte}"
