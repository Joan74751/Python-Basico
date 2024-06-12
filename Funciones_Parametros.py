
def parf (numero):
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')
parf(2)


def saludar(nombre):
    print(f'Hola {nombre} eres el mejor programador')
saludar("Joan")



def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b
resultado = resta(5,6)
print(resultado)


def multi (numero = None):
    if numero == None:
        print("Por favor, introduce un número")
    else:
        print(f'TABLA DE MULTIPLICAR DEL {numero}')
        for f in range(1,11):
            print(f'{f} X {numero} = {f * numero}')
multi (25)