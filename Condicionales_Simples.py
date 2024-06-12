'''
Primer Ejemplo:

Crear un programa que reciba el numero de años que tiene nuestra computadora imprimir en consola si es nuevo o es viejo.

Condiciones: Si es menor o igual a 2 años, entonces es nuevo.
Pero, si es mayor a 2 años, entonces es viejo.

'''


year = int(input("¿Cuántos años tiene tu computador? "))

if year >= 0 and year <= 2:
    print("Tu computador es nuevo")
else:
    print("Tu computador es viejo")


edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Es usted mayor de edad")
else:
    print("Es usted menos de edad")

print("¡Hasta la próxima!")