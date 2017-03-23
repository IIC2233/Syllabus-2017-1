# PRIMERA PARTE: Estructura basica


# SEGUNDA PARTE: Clase Isla
class Isla:
    def __init__(self):
        pass

    def __repr__(self):
        pass


# TERCERA PARTE: Clase Archipielago
class Archipielago:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def agregar_isla(self, nombre):
        pass

    def conectadas(self, nombre_origen, nombre_destino):
        pass

    def agregar_conexion(self, nombre_origen, nombre_destino):
        pass

    def construir(self, archivo):
        pass

    def propagacion(self, nombre_origen):
        pass


if __name__ == '__main__':
    # No modificar desde esta linea
    # (puedes comentar lo que no este funcionando aun)
    arch = Archipielago("mapa.txt") # Instancia y construye
    print(arch) # Imprime el Archipielago de una forma que se pueda entender
    print(arch.propagacion("Perresus"))
    print(arch.propagacion("Pasesterot"))
    print(arch.propagacion("Cartonat"))
    print(arch.propagacion("Womeston"))
