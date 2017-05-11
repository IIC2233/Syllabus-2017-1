__author__ = "joaquin"

from threading import Thread, Lock
import random
import time


def spawn_alumnos(lista_alumnos, espera, ayudantes):
    while True:
        time.sleep(random.expovariate(espera))
        alumno = Alumno(ayudantes)
        lista_alumnos.append(alumno)
        alumno.start()


class Lloraton(Thread):

    def __init__(self, ayudantes, tasa_llegada, time, alumnos):
        super().__init__()
        self.alumnos = alumnos
        self.ayudantes = ayudantes
        self.tasa_llegada = tasa_llegada
        self.time = 0
        self.max_time = time
        self.atendidos = 0

    def run(self):
        self.time = time.time()
        spawner = Thread(target=spawn_alumnos, args=(self.alumnos, 0.5, self.ayudantes), daemon=True)
        spawner.start()
        while time.time() - self.time < self.max_time:
            # Eventualmente, podriamos querer que la lloraton tambien desencadene eventos.
            # Podria haber un terremoto, y la lloraton se acaba porque se cae la sala :(.
            # Eso, podria ir dentro de este while
            pass

class Ayudante:

    def __init__(self, nombre, piedad):
        self.piedad = piedad
        self.nombre = nombre
        self.disponibilidad = Lock()
        self.alumnos_reprobados = 0

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def dar_puntaje(self, alumno):
        if self.piedad > 0:
            give = random.randint(0, self.piedad)
        else:
            give = random.randint(self.piedad, 0)
        if give < 0:
            print("{}: {}, te voy a descontar {} por gil".format(self, alumno, -give))
        elif give > 0:
            print("{}: {}, solo porque me siento generoso te doy {}"
                  " decimas".format(self, alumno, give))
        else:
            print("{}: {}, no te voy a dar ni media decima jajaja >:D".format(self, alumno))
        alumno.nota_final += give/10
        return random.randint(2,5)


class Alumno(Thread):
    ID = 0

    def __init__(self, ayudantes):
        super().__init__()
        self._nota_examen = round(random.uniform(1,7), 2)
        self._nota_final = self._nota_examen
        self.rogado_a = list()
        self.n_alumno = Alumno.ID
        self.ayudantes = ayudantes
        self.visited = list()
        Alumno.ID += 1

    def run(self):
        print("{} llego a la lloraton".format(self))
        if self.nota_final < 3.95:
            print("{}: Vamos que se puede!! un {} se da vuelta"
                  "".format(self, self.nota_final))
        while self.nota_final < 3.95 and len(self.visited) != len(self.ayudantes):
            ayudante = random.choice(self.ayudantes)
            while ayudante.nombre in self.visited:
                ayudante = random.choice(self.ayudantes)
            self.visited.append(ayudante.nombre)
            self.beg_to(ayudante)

    def beg_to(self, ayudante):
        with ayudante.disponibilidad:
            print("{}: Por favor {} dame unas pocas decimas :(".format(self, ayudante))
            waiting = ayudante.dar_puntaje(self)
            time.sleep(waiting)

    def __repr__(self):
        return "Alumno {}".format(self.n_alumno)

    def __str__(self):
        return "Alumno {}".format(self.n_alumno)

    @property
    def nota_final(self):
        return self._nota_final

    @nota_final.setter
    def nota_final(self, value):
        if value < self.nota_final:
            print("{}: Por que me bajan >:(".format(self))
            self._nota_final = value
        elif value == self.nota_final:
            print("{}: No les costaba nada subirme un que sea una decima  :(".format(self))
        else:
            print("{}: Gracias!! todo sirve".format(self))
            self._nota_final = value
        if self.nota_final >= 3.95:
            print("{}: PASEEE CON {}!!!! LO DI VUELTA!!!! NADA ES IMPOSIBLE ... NI UNA"
                  " ...".format(self, self.nota_final))


if __name__ == "__main__":
    print("*************BIENVENIDOS A LA LLORATON!******************")
    ayudantes = [Ayudante("Andrew", 3), Ayudante("Doctor Mavrakis", -2),
                 Ayudante("Juaquin", 2), Ayudante("Floohry", 10), Ayudante("Jhon", 2)]
    alumnos = list()
    lloraton = Lloraton(ayudantes, 1, 60, alumnos)
    lloraton.start()
    lloraton.join()
    print("Termino la lloraton, gracias por participar :)")
    print("*****ESTADISTICAS******")
    print("Reprobados durante la lloraton: {}".format(len(list(
                                filter(lambda a: a.nota_final >= 3.95, alumnos)))))
    print("Aprobados durante la lloraton: {}".format(len(list(
        filter(lambda a: a.nota_final < 3.95, alumnos)))))
