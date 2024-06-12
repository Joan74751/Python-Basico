class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    def frenar(self):
        return "La bicicleta está frenando."
    
    def avanzar(self):
        return "La bicicleta está avanzando."
    
    def girar(self):
        return "La bicicleta está girando."

urbana = Bicicleta("Rojo", 8, 27.5)
hibrida = Bicicleta("Azul", 1, 29)

print(f'Urbana: {urbana.color}')
print(f'Comportamiento de la bicicleta urbana: {urbana.girar()}')
print("\n")
print(f'Híbrida: {hibrida.cambios}')
print(f'Comportamiento de la bicicleta urbana: {urbana.avanzar()}')
print("\n")
