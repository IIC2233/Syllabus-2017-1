__author__ = 'ibutelmann', 'mabucchi'


def comparar_por(atributo):
    """
    Este es un generador de decoradores de clases que toma como argumento
    el atributo por el cual se desea implementar la comparación de la clase.
    """

    def decorador(clase):
        def menor(a, b):
            return getattr(a, atributo) < getattr(b, atributo)

        def menor_igual(a, b):
            return getattr(a, atributo) <= getattr(b, atributo)

        def igual(a, b):
            return getattr(a, atributo) == getattr(b, atributo)

        def mayor_igual(a, b):
            return getattr(a, atributo) >= getattr(b, atributo)

        def mayor(a, b):
            return getattr(a, atributo) > getattr(b, atributo)

        # ahora le agregamos los nuevos métodos a la clase
        setattr(clase, '__lt__', menor)
        setattr(clase, '__le__', menor_igual)
        setattr(clase, '__eq__', igual)
        setattr(clase, '__ge__', mayor_igual)
        setattr(clase, '__gt__', mayor)

        # retornamos la clase modificada
        return clase

    return decorador


def guardar_instancias(clase):
    """Esta función modifica el comportamiento de una clase de tal forma
    que esta guarde en una lista estática todas las instancias creadas.
    Esta lista se puede acceder mediante 'Clase.instancias'.
    """

    # se guarda el __init__ original antes de ser modificado.
    prev_init = getattr(clase, '__init__')

    def new_init(self, *args, **kwargs):
        # El nuevo __init__ llama al previo, pero además agrega el objeto
        # creado a la lista de instancias de la clase
        prev_init(self, *args, **kwargs)
        clase.instancias.append(self)

    # Se agregan y modifican los atributos de la clase
    setattr(clase, 'instancias', list())
    setattr(clase, '__init__', new_init)

    # Se retorna la clase original tras sus modificaciones
    return clase


def cambiar_precio(func):
    """Este es un generador de decorador de funciones para calcular
    el precio correctamente (suponiendo que el IVA cambio)."""

    def _funcion(num):
        # Le restamos los 100 sumados por transporte y luego multiplicamos por 1.23/1.19
        # para obtener el precio con el nuevo IVA, despues sumamos los 100 nuevamente
        return (func(num) - 100) * 1.23 / 1.19 + 100

    return _funcion