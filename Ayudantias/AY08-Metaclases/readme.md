# Pregunta 2 - I1 2015-2
Para esta pregunta usted debe implementar una metaclase que haga que una clase sea abstracta, es decir, que no pueda ser instanciada directamente, además, cada vez que el programador agregue a un método una clase abstracta el decorador "abstracta" (`@abstract`), la metaclase debe asegurarse de que la subclase tenga implementado ese método (asumiremos que aunque contenga pass se considera como implementado).

Tips:

* Si usted solo interrumpe la llamada a la creación de la instancia además de no poder instanciar la clase no se va a poder tampoco instanciar a ninguna de sus subclases.
* Cuando usted decora una función, el atributo `__name__` de la función decorada pasa a llamarse como se llama el decorador, aquí va un ejemplo:

```python
class Ejemplo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def deco(f):
        # hacer algo
        def _f(*args):
            return f(*args)
        return _f
    
    @deco
    def fun1(self):
        pass

print(Ejemplo.__dict__)
print(Ejemplo.__dict__["deco"].__name__)
print(Ejemplo.__dict__["fun1"].__name__)
```
Output:

```
{'__init__': <function Ejemplo.__init__ at 0x1087dda60>, '__dict__': <attribute '__dict__' of 'Ejemplo' objects>, 'deco': <function Ejemplo.deco at 0x1087dd9d8>, 'fun1': <function Ejemplo.deco.<locals>._f at 0x1087dd950>, '__weakref__': <attribute '__weakref__' of 'Ejemplo' objects>, '__doc__': None, '__module__': '__main__'}
deco
_f
```