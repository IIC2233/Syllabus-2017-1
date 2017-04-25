class Abstract(type):
    def __new__(metacls, name, bases, clsdict):
        _abstract_methods = {k for k, v in clsdict.items() if getattr(v, '_is_abstract', False)}
        _is_abstract = True
        for base in bases:
            if type(base) == metacls:
                _is_abstract = False
        clsdict['_is_abstract'] = _is_abstract
        if _is_abstract:
            clsdict['_abstract_methods'] = _abstract_methods
        return super().__new__(metacls, name, bases, clsdict)

    def __call__(cls, *args, **kwargs):
        if cls._is_abstract:
            raise Exception("ERROR! no se puede instanciar una clase abstracta!")
        for name in cls._abstract_methods:
            method = getattr(cls, name)
            if getattr(method, '_is_abstract', False):
                raise Exception("ERROR! debe implementar el método", name)
        return super().__call__(*args, **kwargs)


def abstract(f):
    f._is_abstract = True
    return f


class Zorro(metaclass=Abstract):
    def __init__(self, color_pelaje):
        self.pelajo = color_pelaje
        print("Instancia de Zorro ya creada")

    @abstract
    def cazar(self):
        pass


class ZorroDarwin(Zorro):
    def cazar(self):
        pass


zorrito = ZorroDarwin("cafe")
