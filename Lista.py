'''
Escribier un programa que almacene las asignaturas de un curso

asig = ["Matematicas", "Física", "Español", "Ingles"]

Print(asig[0])
print(type(asig))
'''

#Loteria
numeros = []
for f in range (6):
    numeros.append(int(input("Introduce un número: ")))    
numeros.sort()
print(f'Los números ganadores son: {numeros}')

#lista = [1, 4, 5, 6, 7, 8, 6, "Hola"]

#Formas de borrar un argumento de la lista
#lista.remove(6)
#lista.pop(6)
#del lista[1]

#Borrar todo de la lista 
#lista.clear()

#Para contar cuantas veces se repite en la lista
#lista.count(6)

#Para saber la posicion en la lista
#lista.index("Hola")

#Cambiar el orden de la lista 
#lista.reverse()

#print(lista)