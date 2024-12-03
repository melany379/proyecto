#Calcula_Distancia
import math
x1 = float(input(" Ingresa la coordenada correspondiente a x1: "))
x2 = float(input(" Ingresa la coordenada correspondiente a x2: "))
y1 = float(input(" Ingresa la coordenada correspondiente a y1: "))
y2 = float(input(" Ingresa la coordenada correspondiente a y2: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"Los puntos acordados son ({x1},{x2}) y ({y1},{y2})") 

print(f"La distancia entre este par de puntos es: {distancia}") 