__author__ = 'Benjamín'

import random
from collections import deque


class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.habilidad = random.uniform(1, 10)
        self.jugados = 0


    @property
    def retirarse(self):
        if self.jugados > random.uniform(1, 10):
            return True
        return False

    def ganarle(self, oponente):
        if self.habilidad >= random.uniform(1, self.habilidad + oponente.habilidad):
            return True
        return False

    def __repr__(self):
        return self.nombre



class Simulacion:

    def __init__(self, numero_inicial, tiempo = 70):
        self.cola = deque()
        i = 0
        for i in range(numero_inicial):
            self.cola.append(Jugador('Jugador {}'.format(i)))
        self.id = i + 1
        self.lista_eventos = list()

        self.jugando = deque()
        self.proxima_llegada = None

        self.tiempo_maximo = tiempo

    @property
    def partido_valido(self):
        if len(self.jugando) == 2:
            return True
        return False

    def run(self):

        tiempo = 0
        self.tiempo_llegada(tiempo)

        while tiempo <= self.tiempo_maximo:
            #tiempo, evento = self.lista_eventos.popleft()


            self.llenar_mesa(tiempo)

            if tiempo == self.proxima_llegada:
                self.llegada_personas(tiempo)

            if tiempo == self.proximo_termino:
                self.fin_partido(tiempo)

            tiempo += 1
        print('[{}] Terminó la simulación'.format(self.tiempo_maximo))
        self.generar_estadisticas()

    def llenar_mesa(self, tiempo):
        if len(self.jugando) < 2:
            if len(self.jugando) < 1:
                if len(self.cola) >= 1:
                    self.jugando.append(self.cola.popleft())
            if len(self.jugando) < 2:
                if len(self.cola) >= 1:
                    self.jugando.append(self.cola.popleft())
            if len(self.jugando) == 2:
                self.tiempo_partido(tiempo)


    def llegada_personas(self, tiempo):
        self.tiempo_llegada(tiempo)
        persona = Jugador('Jugador {}'.format(self.id))
        self.cola.append(persona)
        print('[{}] LLegó la persona {}'.format(tiempo, persona))
        self.id += 1

    def fin_partido(self, tiempo):
        jugador1 = self.jugando.popleft()
        jugador2 = self.jugando.popleft()
        if jugador1.ganarle(jugador2):
            if not jugador2.retirarse:
                self.cola.append(jugador2)
            self.jugando.append(jugador1)
            ganador = jugador1
        else:
            if not jugador1.retirarse:
                self.cola.append(jugador1)
            self.jugando.append(jugador2)
            ganador = jugador2
        print('[{}] Termino el partido entre {} y {}. Ganó {}'.format(tiempo, jugador1, jugador2, ganador))
        self.llenar_mesa(tiempo)

    def tiempo_partido(self, tiempo):
        self.proximo_termino = tiempo + round(random.uniform(4, 6))

    def tiempo_llegada(self, tiempo):
        self.proxima_llegada = tiempo + round(random.expovariate(1 / 15) + 1)
        # Le sumo 1 porque podría ser 0 y nunca ejecutarse el evento.

    def generar_estadisticas(self):
        print('\nEstadísticas:')
        print('algo')


sim = Simulacion(3)
sim.run()