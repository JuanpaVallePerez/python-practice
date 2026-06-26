print("Calculadora de IMC")
print("Calculadora del Índice de Masa Corporal basado en las guías de la OMS.")
nombre = input("¿Cuál es el nombre del paciente?: ")
edad = int(input("¿Cuál es la edad en años del paciente?: "))
profesion = input("¿Cuál es la profesión del paciente?: ")
peso = float(input("¿Cuál es el peso en kilogramos del paciente?: "))
estatura = float(input("¿Cuál es la estatura en metros del paciente?: "))
IMC = peso / estatura**2
print(f"El IMC es de {IMC: .2f}")
if IMC < 18.5:
    clasificacion =  "BAJO PESO."
elif IMC >= 18.5 and IMC <= 24.9:
    clasificacion = "PESO NORMAL."
elif IMC >= 25.0 and IMC <= 29.9:
    clasificacion = "SOBREPESO."
elif IMC >= 30.0 and IMC <= 34.9:
    clasificacion = "OBESIDAD GRADO I."
elif IMC >= 35.0 and IMC <= 39.9:
    clasificacion = "OBESIDAD GRADO II."
elif IMC >= 40.0:
    clasificacion = "OBESIDAD GRADO III."
print("FICHA DEL PACIENTE")
print(f"Nombre: {nombre}")
print(f"Profesion: {profesion}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {IMC: .2f}")
print(f"Clasificación: {clasificacion}")
respuesta = input("¿Desea calcular otro IMC? (s/n): ")
while respuesta == "s":
    nombre = input("¿Cuál es el nombre del paciente?: ")
    edad = int(input("¿Cuál es la edad en años del paciente?: "))
    profesion = input("¿Cuál es la profesión del paciente?: ")
    peso = float(input("¿Cuál es el peso en kilogramos del paciente?: "))
    estatura = float(input("¿Cuál es la estatura en metros del paciente?: "))
    IMC = peso / estatura ** 2
    print(f"El IMC es de {IMC: .2f}")
    if IMC < 18.5:
        clasificacion = "BAJO PESO."
    elif IMC >= 18.5 and IMC <= 24.9:
        clasificacion = "PESO NORMAL."
    elif IMC >= 25.0 and IMC <= 29.9:
        clasificacion = "SOBREPESO."
    elif IMC >= 30.0 and IMC <= 34.9:
        clasificacion = "OBESIDAD GRADO I."
    elif IMC >= 35.0 and IMC <= 39.9:
        clasificacion = "OBESIDAD GRADO II."
    elif IMC >= 40.0:
        clasificacion = "OBESIDAD GRADO III."
    print("FICHA DEL PACIENTE")
    print(f"Nombre: {nombre}")
    print(f"Profesion: {profesion}")
    print(f"Edad: {edad}")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"IMC: {IMC: .2f}")
    print(f"Clasificación: {clasificacion}")
    respuesta = input("¿Desea calcular otro IMC? (s/n): ")
if respuesta == "n":
    print("Muchas gracias por utilizar el programa.")










