from collections import deque


def sonda():
    with open('data/sonda.txt', 'r') as f:
        minerales = dict()
        for line in f:
            line = line.strip()
            separados = line.split(',') #["3", "4", "oro"]
            mineral = separados.pop()
            coordenadas = ','.join(separados)
            minerales[coordenadas] = mineral

        num_consultas = int(input('Ingrese numero de consultas'))
        for i in range(num_consultas):
            n_coordenadas = input('Ingrese coordenadas: ')
            if n_coordenadas in minerales:
                print(minerales[n_coordenadas])
            else:
                print('No hay nada!! :c xdxdxd')


def traidores():
    bufalo = set()
    rivales = set()
    with open('data/bufalos.txt', 'r') as f:
        for line in f:
            line = line.strip()
            bufalo.add(line)

    with open('data/rivales.txt', 'r') as f:
        for line in f:
            line = line.strip()
            rivales.add(line)

    print(rivales.intersection(bufalo))


class Pizza:
    n_pizzas = 0
    def __init__(self):
        Pizza.n_pizzas += 1
        self.id = Pizza.n_pizzas


def pizzas():
    with open('data/pizzas.txt', 'r') as f:
        pila = []
        cola = deque()
        for line in f.read().splitlines():
            line = line.strip()
            if line == 'APILAR':
                n_pizza = Pizza()
                pila.append(n_pizza)
                print('Pizza {0} apilada. {1} Pizzas apiladas - {2} Pizzas en cola'.format(n_pizza.id, len(pila),
                                                                                           len(cola)))
            elif line == 'ENCOLAR':
                pizza_encola = pila.pop()
                cola.append(pizza_encola)
                print('Pizza {0} encolada. {1} Pizzas apiladas - {2} Pizzas en cola'.format(pizza_encola.id, len(pila),
                                                                                           len(cola)))

            elif line == 'SACAR':
                pizza_sacada = cola.popleft()
                print('Pizza {0} sacada. {1} Pizzas apiladas - {2} Pizzas en cola'.format(pizza_sacada.id, len(pila),
                                                                                           len(cola)))



if __name__ == '__main__':
    exit_loop = False

    functions = {"1": sonda, "2": traidores, "3": pizzas}

    while not exit_loop:
        print(""" Elegir problema:
            1. Sonda
            2. Traidores
            3. Pizzas
            Cualquier otra cosa para salir
            Respuesta: """)

        user_entry = input()

        if user_entry in functions:
            functions[user_entry]()
        else:
            exit_loop = True
