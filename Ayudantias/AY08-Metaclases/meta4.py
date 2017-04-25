class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, dic):
        print(meta)
        print(nombre)
        dic.update({"peso": 40})
        return super().__new__(meta, nombre, base_clases, dic)

    def __call__(clase, *args, **kwargs):
        print("\n se llamó a la creación de una nueva instancia de la clase menor")
        print("call de ", str(clase))
        print("call con args: ", str(args))
        return super().__call__(*args, **kwargs)


class Zorro(metaclass=MiMetaClase):
    def __init__(self, color_pelaje):
        print("\nestamos en el init de la clase menor")
        self.pelaje = color_pelaje

    def func(self, params):
        pass

    def __call__(self, texto):
        print("el zorro dice: ", texto)

    mi_param = 4


print("\nahora recién voy a crear una instancia")

instancia = Zorro("rojo")
instancia("waw")