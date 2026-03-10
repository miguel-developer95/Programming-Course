import matplotlib.pyplot as plt
import numpy as np

def calcular_propiedades(fig, *args):
    """Devuelve una tupla con (área, perímetro)"""
    if fig == "triangulo":
        ancho, alto = args[0], args[1]
        area = ancho * alto
        perimetro = 2* (ancho + alto )
        return area, perimetro
        
    elif fig == "cuadrado":
        ancho, alto = args[0], args[1]
        area = ancho * alto
        perimetro = 2 * (ancho + alto)
        return area, perimetro
    
    if fig == "circulo":
        radio = args[0]
        area = np.pi * (radio ** 2)
        perimetro = 2 * np.pi * radio
        return area, perimetro

    return 0, 0

def maximo(mensaje, minimo = 0, maximo = 10):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < minimo or numero > maximo:
                print(f"\n\n\n---Error. Ingrese un numero entre {minimo} y {maximo}---")
            else:
                return numero
        except ValueError:
            print("\n\n\n---Error. Ingrese solo numeros---")
def solo_numeros(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("\n\n\n---Error. Ingrese solo numeros---")
def triangulo(ax, punto1, punto2, punto3):
    area, peri= calcular_propiedades("triangulo", punto1, punto2)
    ax.add_patch(plt.Polygon([[punto1,punto2], [punto2,punto3], [punto3,punto1]], color="green", fill=False, label=f"Area:{area:.1f}\nPerimetro:{peri:.1f}"))
    ax.legend(loc="center")
    print("Haciendo un triangulo")
def cuadrado(ax, ubicacionx, ubicaciony, ancho, alto):
    area, peri = calcular_propiedades("cuadrado", ancho, alto)
    ax.add_patch(plt.Rectangle((ubicacionx, ubicaciony), ancho, alto, color="red", fill=False, label=f"Area:{area:.1f}\nPerimetro:{peri:.1f}"))
    ax.legend(loc="center")
    print("Haciendo un cuadrado")
def circulo(ax, ubicacionx, ubicaciony, ancho):
    area, peri = calcular_propiedades("circulo", ancho, ubicaciony )
    ax.add_patch(plt.Circle((ubicacionx, ubicaciony), ancho, color="blue", fill=False, label=f"Area:{area:.1f}\nPerimetro:{peri:.1f}"))
    ax.legend(loc="center")    
    print("Haciendo un circulo")

def menu():
        Operacion= solo_numeros("Que figura desea hacer? \n1 triangulo \n2 cuadrado \n3 circulo \n4 salir\n")
        fig, ax = plt.subplots(figsize=(5,3), layout = "constrained")
        match Operacion:
            case 1:
                punto1 = maximo("Ingrese el punto 1 del triangulo (1-10): ", 1, 10)
                punto2 = maximo("Ingrese el punto 2 del triangulo (1-10): ", 1, 10)
                punto3 = maximo("Ingrese el punto 3 del triangulo (1-10): ", 1, 10)
                if punto1 + punto2 + punto3 > 30:
                    print("\n\n\n---Error. La suma de los puntos del triangulo no puede ser mayor a 30---")
                    return
                triangulo(ax, punto1, punto2, punto3)
            case 2:
                ubicacionx = maximo("Ingrese la ubicacion x del cuadrado (1-10): ", 1, 10)
                ubicaciony = maximo("Ingrese la ubicacion y del cuadrado (1-10): ", 1, 10)
                ancho = maximo("Ingrese el ancho del cuadrado (1-10): ", 1, 10)
                alto = maximo("Ingrese el alto del cuadrado (1-10): ", 1, 10)
                if ubicacionx + ancho > 10 or ubicaciony + alto > 10:
                    print("\n\n\n---Error. El cuadrado se sale de los limites de la grafica---")
                    return
                cuadrado(ax, ubicacionx, ubicaciony, ancho, alto)
            case 3:
                ubicacionx = maximo("Ingrese la ubicacion x del circulo (1-10): ")
                ubicaciony = maximo("Ingrese la ubicacion y del circulo (1-10): ")
                ancho = maximo("Ingrese el ancho del circulo (1-10): ")
                if ubicacionx - ancho < 0 or ubicacionx + ancho > 10:
                    print("\n\n\n---Error. El ancho del circulo es demasiado grande para la ubicacion x---")
                    return
                if ubicaciony - ancho < 0 or ubicaciony + ancho > 10:
                    print("\n\n\n---Error. El ancho del circulo es demasiado grande para la ubicacion y---")
                    return
                circulo(ax, ubicacionx,ubicaciony , ancho)
            case 4:
                exit()
                print("---Saliendo Del Programa---")
            case _:
                print("\n\n\n---Error. Ingrese una opcion valida---")

while True:
    
    menu()
    plt.ylim(0, 10)
    plt.xlim(0, 10)
    plt.show()



      