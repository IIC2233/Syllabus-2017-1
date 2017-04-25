print("lo primero es estto")

class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, dic):
        print(meta)
        print(nombre)
        dic.update({"peso": 40})
        return super().__new__(meta, nombre, base_clases, dic)


class MiClase(metaclass=MiMetaClase):
    def func(self, params):
        pass

    mi_param = 4


