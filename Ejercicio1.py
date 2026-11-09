import random
import math

def calcular_resultado(a, b, c, d, cantidad_puntos):
    puntos_elipse = 0
    puntos_interseccion = 0
    for _ in range(cantidad_puntos):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        condicion_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
        if condicion_elipse:
            puntos_elipse += 1
            condicion_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1
            if condicion_hiperbola:
                puntos_interseccion += 1  
    area_elipse_teorica = math.pi * a * b
 
    if puntos_elipse > 0:
        area_interseccion = area_elipse_teorica * (puntos_interseccion / puntos_elipse)
    else:
        area_interseccion = 0.0
    return puntos_elipse, puntos_interseccion, area_elipse_teorica, area_interseccion
if __name__ == "__main__":
    print("Ingrese los datos")
    
    a = float(input("ingrese el valor de a: "))
    b = float(input("ingrese el valor de b: "))
    c = float(input("ingrese el valor de c: "))
    d = float(input("ingrese el valor de d: "))
    cantidad = int(input("ingrese la cantidad de puntos aleatorios: "))
    
    p_elipse, p_inter, area_teorica, area_inter = calcular_resultado(a, b, c, d, cantidad)
    
    print("\nResultados:")
    print(f"area teorica de la elipse: {area_teorica}")
    print(f"puntos aleatorios que cayeron dentro la elipse: {p_elipse}")
    print(f"puntos aleatorios que cayeron en la intersección: {p_inter}")
    print(f"area aproximada de la intersección: {area_inter}")
    print("______________")