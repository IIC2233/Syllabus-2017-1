class Nodo:

    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor

class Lista:

    def __init__(self, *args):
        self.cola = None
        self.cabeza = None
        for arg in args:
            self.append(arg)

    def __repr__(self):
        nodo = self.cabeza
        s = "["
        if nodo:
            s += str(nodo.valor) + ", "
        else:
            return "[]"
        while nodo.siguiente:
            nodo = nodo.siguiente
            s += str(nodo.valor) + ", "
        return s.strip(", ") + "]"
        
    def __getitem__(self, index):
        nodo = self.cabeza
        for i in range(index):
            if nodo:
                nodo = nodo.siguiente
            else:
                raise IndexError
        if not nodo:
            raise IndexError
        else:
            return nodo.valor

    def __in__(self, valor):
        for elemento in self:
            if elemento == valor:
                return True
        return False

    def append(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente

    # Ademas podemos anadir otros metodos como count, clear, etc. siempre
    # recordando que debemos implementarlos teniendo en cuenta los otros
    # metodos que definimos para nuestra clase ListaLigada

    def clear(self):
        self = Lista()

    def count(self, valor):
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1
        return contador
    
