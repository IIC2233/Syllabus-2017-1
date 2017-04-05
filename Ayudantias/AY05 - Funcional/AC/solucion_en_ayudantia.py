from datetime import date
from functools import reduce

def leer_archivo(path):
    with open(path) as archivo:
        splitted = list(map(lambda l: tuple(l.split(";")),
                            archivo))
        tuplas = map(lambda t: t[0:5] + tuple(map(int, t[5:11])),
                     splitted)
        return list(tuplas)


def se_llama_como(tuplas, nombre):
    return list(filter(lambda t: any(map(lambda x, y: x.lower() == y.lower(), t, nombre)),
                       tuplas))

def chilenos_zurdos(tuplas):
    return list(filter(lambda t: t[3:5] == ("Chile", "izquierdo"),
                       tuplas))


def edades(tuplas):
    anho = date.today().year # 2017
    return list(map(lambda t: t[0:2] + (anho - t[7],),
                    tuplas))


def sub_17(tuplas):
    return list(filter(lambda t: t[2] <= 17,
                       edades(tuplas)))


def goleador(tuplas):
    return reduce(lambda x, y: x if x[8] > y[8] else y,
                  tuplas)
    #return reduce(lambda x, y: max(x, y, key=lambda t: t[8]), tuplas)

def mayor_riesgo_obesidad(tuplas):
    imc = lambda t: ((t[3] / (t[2]/100)**2),)
    chilenos = filter(lambda t: t[3] == "Chile", tuplas)
    aux = map(lambda t: t[0:2] + t[9:11], chilenos)
    tuplas_con_imc = map(lambda t: t + imc(t), aux)
    return reduce(lambda x, y: x if x[4] > y[4] else y,
                  tuplas_con_imc)


if __name__ == "__main__":
    arch = leer_archivo("jugadores_sin_tildes.txt")
    #print(mayor_riesgo_obesidad(leer_archivo("jugadores_sin_tildes.txt")))
    print(se_llama_como(arch, ("Luis Felipe", "Suazo", "Perez")))
