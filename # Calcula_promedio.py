# Calcula_promedio
calificaciones = []

def agregar_calificacion(materia, calificacion):
    calificaciones.append((materia, calificacion))

def calcular_promedio():
    total = sum(calificacion for materia, calificacion in calificaciones)
    promedio = total / len(calificaciones)
    return promedio

while True:
    materia = input("Introduce el nombre de la materia (o 'fin' para terminar): ")
    if materia.lower() == 'fin':
        break
    calificacion = float(input(f"Introduce la calificación para {materia}: "))
    agregar_calificacion(materia, calificacion)

promedio = calcular_promedio()
print(f"El promedio de tus materias es: {promedio:.2f}")
