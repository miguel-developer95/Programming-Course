import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# --- Función genérica para cálculos ---
def calcular_propiedades(fig, *args):
    """Devuelve (volumen, área superficial)"""
    if fig == "cubo":
        lado = args[0]
        volumen = lado**3
        area = 6 * (lado**2)
        return volumen, area
    
    elif fig == "esfera":
        radio = args[0]
        volumen = (4/3) * np.pi * (radio**3)
        area = 4 * np.pi * (radio**2)
        return volumen, area
    
    elif fig == "prisma_rectangular":
        ancho, alto, largo = args[0], args[1], args[2]
        volumen = ancho * alto * largo
        area = 2*(ancho*alto + ancho*largo + alto*largo)
        return volumen, area
    
    return 0, 0

# --- Funciones de dibujo ---
def cubo(ax, lado):
    # vértices de un cubo en (0,0,0)
    r = [0, lado]
    vertices = np.array([[x,y,z] for x in r for y in r for z in r])
    # caras
    caras = [
        [vertices[0],vertices[1],vertices[3],vertices[2]],
        [vertices[4],vertices[5],vertices[7],vertices[6]],
        [vertices[0],vertices[1],vertices[5],vertices[4]],
        [vertices[2],vertices[3],vertices[7],vertices[6]],
        [vertices[1],vertices[3],vertices[7],vertices[5]],
        [vertices[0],vertices[2],vertices[6],vertices[4]]
    ]
    ax.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    vol, area = calcular_propiedades("cubo", lado)
    ax.text(lado/2, lado/2, lado/2, f"Volumen:{vol:.1f}\nÁrea:{area:.1f}", color="black")

def esfera(ax, radio):
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:20j]
    x = radio*np.cos(u)*np.sin(v)
    y = radio*np.sin(u)*np.sin(v)
    z = radio*np.cos(v)
    ax.plot_surface(x, y, z, color="blue", alpha=0.3)
    vol, area = calcular_propiedades("esfera", radio)
    ax.text(0,0,0, f"Volumen:{vol:.1f}\nÁrea:{area:.1f}", color="black")

def prisma_rectangular(ax, ancho, alto, largo):
    # vértices
    vertices = np.array([[0,0,0],[ancho,0,0],[ancho,largo,0],[0,largo,0],
                         [0,0,alto],[ancho,0,alto],[ancho,largo,alto],[0,largo,alto]])
    caras = [
        [vertices[0],vertices[1],vertices[2],vertices[3]],
        [vertices[4],vertices[5],vertices[6],vertices[7]],
        [vertices[0],vertices[1],vertices[5],vertices[4]],
        [vertices[2],vertices[3],vertices[7],vertices[6]],
        [vertices[1],vertices[2],vertices[6],vertices[5]],
        [vertices[0],vertices[3],vertices[7],vertices[4]]
    ]
    ax.add_collection3d(Poly3DCollection(caras, facecolors='green', linewidths=1, edgecolors='k', alpha=.25))
    vol, area = calcular_propiedades("prisma_rectangular", ancho, alto, largo)
    ax.text(ancho/2, largo/2, alto/2, f"Volumen:{vol:.1f}\nÁrea:{area:.1f}", color="black")

# --- Menú principal ---
def menu():
    print("\nMenú de figuras 3D")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Prisma rectangular")
    print("4. Salir")
    op = int(input("Ingrese opción: "))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if op == 1:
        lado = float(input("Ingrese el lado del cubo: "))
        cubo(ax, lado)
    elif op == 2:
        radio = float(input("Ingrese el radio de la esfera: "))
        esfera(ax, radio)
    elif op == 3:
        ancho = float(input("Ingrese el ancho: "))
        alto = float(input("Ingrese el alto: "))
        largo = float(input("Ingrese el largo: "))
        prisma_rectangular(ax, ancho, alto, largo)
    elif op == 4:
        exit()
    else:
        print("Opción inválida")
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_zlim(0,10)
    plt.show()

while True:
    menu()