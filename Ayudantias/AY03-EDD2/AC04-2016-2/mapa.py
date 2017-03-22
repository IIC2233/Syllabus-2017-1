from listaligada import Lista

class MapaGenetico:

    def __init__(self):
        self.especies = Lista()

    def __repr__(self):
        s = ""
        for especie in self.especies:
            s += str(especie) + "\n"
            for pariente, gen in especie.parientes:
                s += "    {} - Gen compartido: {}\n".format(
                    pariente, gen)
        return s.strip()

    def agregar_nodo(self, id_nodo, genes):
        especie = Especie(id_nodo, genes)
        for e in self.especies:
            for gen in especie.genes:
                if gen in e.genes:
                    e.parientes.append(Lista(especie, gen))
                    especie.parientes.append(Lista(e, gen))
        self.especies.append(especie)

    def no_pariente(self, id_nodo):
        id_nodo = str(id_nodo)
        for especie in self.especies:
            if especie.id_nodo == id_nodo:
                break
        else:
            print("Especie no encontrada")
            return
        s = "Los siguientes no son parientes de {}:\n".format(id_nodo)
        for e in self.especies:
            if e == especie:
                continue
            for gen in especie.genes:
                if gen in e.genes:
                    break
            else:
                s += "{}\n".format(e)
        print(s.strip())
    
                    
class Especie:

    def __init__(self, id_nodo, genes):
        self.id_nodo = id_nodo
        self.genes = genes
        self.parientes = Lista()

    def __repr__(self):
        genes = ""
        for gen in self.genes:
            genes += gen + "-"
        genes = genes.strip("-")
        s = "ID: {} - Genes: {}".format(self.id_nodo, genes)
        return s

    def __eq__(self, other):
        return self.id_nodo == other.id_nodo


