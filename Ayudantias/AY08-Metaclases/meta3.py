class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, dic):
        print(meta)
        print(nombre)
        dic.update({"peso": 40})
        return super().__new__(meta, nombre, base_clases, dic)

    def __init__(cls, name, bases, dic):
        print("este es el init en la metaclase")
        super().__init__(name, bases, dic)


print("ahora pasamos a la def de clase menor")


class MiClase(metaclass=MiMetaClase):
    def func(self, params):
        pass

    mi_param = 4


print("\nahora recién voy a crear una instancia")

instancia = MiClase()
