
word = input ("Ingresa una palabra ")

for f in range(10):
    print(word)



print('Comienzo')

contador = 1

for f in [23, 4, 0]:
    print(f'Vuelta número: {contador}')
    print(f'Hola, ahora f vale {f} y su cuadrado es {f**2}')
    contador += 1

print('Final')


numero = int(input("¿De que número quieres la tabla de multiplicar? "))


print(f'Tabla de multiplicar del {numero}')

for f in range (1, 11):
    print(f'{f} * {numero} = {numero*f}')
