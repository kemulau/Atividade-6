from Animal import Animal  

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def mostrar(self):
        return f"Gato: {self.getNome()}, Idade: {self.getIdade()}, Raça: {self.__raca}"
