
#Primera forma de crear un diccionario
dic = {
    "Nombre": "Joan",
    "Edad": 21,
    "Documento": 499
}

print(dic)

#Segunda forma de crear un diccionario

dic2 = dict (Nombre = 'Fernanda',
             Edad = 19,
             Documento = 962)

print(dic2)

#Tercera forma de crear un diccionario

dic3 = dict([
    ('Nombre', 'Juan'),
    ('Edad', 37),
    ('Documento', 480)
])

print(dic3)

#Ejemplo 

inventario = dict(
    Manzana = 235,
    Pera = 400,
    Naranjas = 250,
    Sandias = 500)

print(inventario.keys())
print(inventario.values())
print(inventario.items())
