
def suma(*args):
    s = 0

    for f in args:
        s += f
    return s
resultado = suma(4, 23, 4, 14, 12)

print(resultado)

def lenguaje (nombre, *lenguajes):
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {lenguajes}')

lenguaje("Joan", "PHP, Python, Java, C#")


def lenguaje0(nombre, **lenguajes):
    print(f'Hola {nombre}')
    print("Buscando Información acerca de tus lenguajes favoritos...")
    print("Cargando información... \n")

    print("Informacion: ")
    contador = 0
    for f in lenguajes:
        contador += 1
        print(f'Tu {contador} lenguaje favorito es: {lenguajes[f]}')
    
lenguaje0("Joan", lenguaje1 = "Python", lenguaje2 = "PHP", lenguaje3 = "Java\n")
