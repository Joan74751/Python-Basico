#Calculadora de IMC

contador = 0

print("CALCULADAORA DE INDICE DE MASA CORPORAL (IMC) \n")

while contador != 2:
    contador = int(input("¿Quieres serguir calculado el IMC? \n1.Si y 2.No\n"))

    if contador == 1:
        estatura = float(input("Ingrese su estatuta en metro: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        resultado = round(peso/(estatura * estatura), 2)

        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO')
        elif 18.5 < resultado < 24.9:
            print(f'IMC {resultado} = PESO NORMAL')
        elif 25 < resultado < 29.9:
            print(f'IMC {resultado} = SOBREPESO')
        elif resultado > 30:
            print(f'IMC {resultado} = OBESIDAD')
    elif contador == 2:
        print("Hasta pronto \n")
print("Gracias por usar la calculadora de IMC \n")