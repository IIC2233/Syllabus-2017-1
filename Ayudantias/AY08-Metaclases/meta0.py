print("lo primero es estto")

class MiMetaClase(type):
    def __new__(meta, nombre, base_clases, dic):
        print(meta)
        print(nombre)
        dic.update({"peso": 40})
        return super().__new__(meta, nombre, base_clases, dic)

