while True:
    try:
        n = input("Ingrese un entero: ")
        n = int(n)
        break

    except Exception:
        print("Algo malo ocurrio...")

    except ValueError:
        print("Entero no valido, intente nuevamente...")

    finally:
        print("Saliendo del programa")

print("Proceso terminado con exito")
