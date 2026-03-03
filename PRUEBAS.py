import turtle

# Funciones para dibujar figuras
def dibujar_cuadrado():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def dibujar_triangulo():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def dibujar_rectangulo():
    for _ in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)

def dibujar_circulo():
    turtle.circle(100)

# Menú con match-case
while True:
    try:
        print("Seleccione una figura")
        print("1. Cuadrado")
        print("2. Triángulo")
        print("3. Rectángulo")
        print("4. Círculo")
        
        opcion = int(input("Ingrese el número de la figura: "))
    except ValueError:
        print("Error. Ingrese números enteros")
        continue
    else:
        turtle.reset()  # limpia la pantalla antes de dibujar
        
        match opcion:
            case 1:
                print("Has seleccionado 1. Cuadrado")
                dibujar_cuadrado()
            case 2:
                print("Has seleccionado 2. Triángulo")
                dibujar_triangulo()
            case 3:
                print("Has seleccionado 3. Rectángulo")
                dibujar_rectangulo()
            case 4:
                print("Has seleccionado 4. Círculo")
                dibujar_circulo()
            case _:
                print("Error: Opción no válida. Por favor, seleccione un número entre 1 y 4.")
                continue

turtle.done()  # mantiene abierta la ventana gráfica