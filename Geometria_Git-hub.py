while True:
  try:
    print("select a figure")
    print("1. cuadrado")
    print("2. triángulo")
    print("3. rectángulo")
    print("4. círculo")
    opcion =int(input("ingrese el numero de la figura "))
  except ValueError:
    print("Error. Ingrese números enteros")
    continue # Si la entrada no es un entero, imprime el error y reinicia el ciclo
  else:
    # Si la entrada es un número entero válido, continua con match
    match opcion:
      case 1:
        print("has seleccionado 1.")
      case 2:
        print("has seleccionado 2.")
      case 3:
        print("has seleccionado 3.")
      case 4:
        print("has seleccionado 4.")
      case _:
        print("error: Opción no válida. Por favor, seleccione un número entre 1 y 4.")
        continue # Solicitar información nuevamente
      



      