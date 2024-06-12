'''
Crear un tupla con varias numeros despues pedir un numero por teclado e indicar 
cuantas veces se repite
'''

numero = (5,6,7,8,5,5,6,90,12,14,22)

n = int(input("Dame un número: "))

print(f'El número se repite: {numero.count(n)} veces')

print(f'El número {n} se encuentra en el indice: {numero.index(n)}')