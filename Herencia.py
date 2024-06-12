class Vehículo():
    def __init__(self, matricula, modelo, marca, color):
        #ATTRIBUTES
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False
    #METHODS
    def avanzar(self):
        self.avanza = True
    def frenar(self):
        self.frena = True
    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f'Matricula: {self.matricula}\nModelo: {self.modelo}\nMarca: {self.marca}\nColor: {self.color}\nAvanzar: {self.avanza}\nFrenar: {self.frena}'
              f'\nGirar: {self.gira}')
class Moto(Vehículo):
    def __init__(self, matricula, modelo, marca, color, cilindraje):
        super().__init__(matricula, modelo, marca, color)
        self.cilindraje = cilindraje

moto1 = Moto('ABC12345', 2018, "BMW", "Azul", 150)
print(f'Cilindraje: {moto1.cilindraje}')
moto1.avanzar()
moto1.girar()
moto1.frenar()
moto1.imprimir()