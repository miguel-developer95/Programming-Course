import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
import math

def hacer_triangulo():
    # Pedir coordenadas al usuario
    puntos = []
    for i in range(3):
      xi = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
      yi = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
      puntos.append((xi, yi))

    fig, ax = plt.subplots()
    tri = Polygon(puntos, facecolor='green', edgecolor='red', linewidth=3)
    ax.add_patch(tri)
    ax.set_aspect('equal')

    # Ajustar límites dinámicamente
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    ax.set_xlim(min(xs)-1, max(xs)+1)
    ax.set_ylim(min(ys)-1, max(ys)+1)

    plt.show()
    print("haciendo un triángulo")

    # Calcular área y perímetro
    area = 0.5 * abs(sum(xs[i]*ys[(i+1)%3] - xs[(i+1)%3]*ys[i] for i in range(3)))
    perimetro = sum(math.dist(puntos[i], puntos[(i+1)%3]) for i in range(3))

    return {"area": area, "perimetro": perimetro}


def hacer_cuadrado():
    # Pedir coordenadas de esquina inferior izquierda y lado
    x = float(input("Ingrese la coordenada x de la esquina inferior izquierda: "))
    y = float(input("Ingrese la coordenada y de la esquina inferior izquierda: "))
    lado = float(input("Ingrese la longitud del lado: "))

    if lado<=0:
        print('ERROR: El lado debe ser positivo, mayor a cero')
        return None

    fig, ax = plt.subplots(figsize=(5,3), layout='constrained')
    cuad = Rectangle((x, y), lado, lado, facecolor='green', edgecolor='black', linewidth=3)
    ax.add_patch(cuad)
    ax.set_aspect('equal')
    ax.set_xlim(x-1, x+lado+1)
    ax.set_ylim(y-1, y+lado+1)

    plt.show()
    print("haciendo un cuadrado")

    area = lado**2
    perimetro = 4*lado

    return {"area": area, "perimetro": perimetro}

def hacer_circulo():
    # Pedir centro y radio
    cx = float(input("Ingrese la coordenada x del centro: "))
    cy = float(input("Ingrese la coordenada y del centro: "))
    radio = float(input("Ingrese el radio del círculo: "))

    fig, ax = plt.subplots()
    cir = Circle((cx, cy), radio, color='blue', fill=True)
    ax.add_patch(cir)
    ax.set_aspect('equal')
    ax.set_xlim(cx-radio-1, cx+radio+1)
    ax.set_ylim(cy-radio-1, cy+radio+1)

    plt.show()
    print("haciendo un círculo")

    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio

    return {"area": area, "perimetro": perimetro}

def menu(): 
    print("\nMenú de figuras geométricas")
    print("1. triángulo")
    print("2. cuadrado")
    print("3. círculo")
    print("4. salir")

while True:
    menu()
    try:
        opcion = int(input("Ingrese el número de la figura: \n"))
    except ValueError:
        print("Error. Ingrese números enteros")
        continue

    match opcion:
        case 1:
            valores = hacer_triangulo()
            print("Valores:", valores)
        case 2:
            valores = hacer_cuadrado()
            print("Valores:", valores)
        case 3:
            valores = hacer_circulo()
            print("Valores:", valores)
        case 4:
            print("Saliendo")
            break
        case _:
            print("Error: Opción no válida. Por favor, seleccione un número entre 1 y 4.")
            continue



      