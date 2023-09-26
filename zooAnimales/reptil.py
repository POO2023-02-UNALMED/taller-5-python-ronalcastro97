from zooAnimales.animal import Animal

class Reptil(Animal):

    def __init__(self, nombre, edad, habitat, genero):
        super().__init__(nombre, edad, habitat, genero)