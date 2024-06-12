
edad = int(input("¿Cuántos años tienes? "))
graduacion = input("¿Ya te has graduado? (Si) o (No) ")

if edad > 18:
    print("Felicidades! ya tiene la mayoria de edad ")
    if graduacion == 'Si':
        print("Felicidades por tu graduacion! ")


password = input("Ingresa la Contraseña: ")

if (len(password)>= 8):
    print("Muy bien, contraseña suficientemente larga")

    if(password == 'Prueba12345'):
        print("Además, es la contraseña correcta")
    else:
        print("Pero es incorrecta")
else:
    print("Tu contraseña es incorrecta e insegura")
    print("Además, es incorrecta")

