'''
add // Añade un elmento al final del conjunto
clear // Elimina toda la informacion del conjunto
pop // Devuelve y elimina un elemento arbitrario o devuelve un error si está vacio
remove // Intenta eliminar un elemento del cojunto, si no existe eleva un error
union // Devuelve un conjunto con todos los elemenros de ambos conjuntos
'''

#Primera forma de crear conjuntos
alumnos = {"Andrea", "Ruby", "Marcos", "Marlon", "Jose"}

print(type(alumnos))
print(alumnos)

#Segunda forma de crear conjuntos
lenguajes = set (["PHP", "Java", "C", "Python"])
print(lenguajes)

#lenguajes.add("C#")
#lenguajes.clear()
#lenguajes.pop()
#lenguajes.remove("PHP")

todos = alumnos.union(lenguajes)

print(todos)