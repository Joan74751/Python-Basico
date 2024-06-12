class Gato():
    def sonido(self):
        print("MIAU")

class Perro():
    def sonido(self):
        print("GUAU")

class Cerdo():
    def sonido(self):
        print("OING OING")

def escuchar(animal):
    animal.sonido()

gato1 = Gato()
perro1 = Perro()
Cerdo1 = Cerdo()

escuchar(Cerdo1)