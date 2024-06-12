class Persona:
    def __init__(self, id, nombre, edad):
        self.__id = id
        self.nombre = nombre
        self.edad = edad
    
    def saludos(self):
        return f'Hola {self.nombre}'
    
    def getId(self):
        return self.__id
    
    def setId(self, valor):
        self.__id = valor

Persona1 = Persona(45678, "Jose", 45)
print(Persona1.getId())
#print(Persona1._Persona__id)
Persona1.setId(12345)
print(Persona1.getId())
print(Persona1.nombre)
print(Persona1.edad)
