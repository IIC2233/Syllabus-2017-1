import copy


class AN:

    def __init__(self, sc=None, dd=None):
        self.dd = dd
        self.sc = sc
        self.hc = {}

    def tres(self, val, future_dd_val):
        if self.sc == future_dd_val:
            self.hc[val] = AN(sc=val, dd=self)
            return True
        for c in self.hc.values():
            c.tres(val, future_dd_val)
        return False

    def nif(self, sc, cm_):
        if self.sc == sc:
            return cm_
        for c in self.hc.values():
            out = c.nif(sc, cm_ + [c.sc])
            if out is not None:
                return out
        return None

    def deno(self, cm_):

        if len(cm_) == 0:
            aux = copy.copy(self.dd.hc[self.sc])
            del self.dd.hc[self.sc]
            return aux
        next = cm_.pop(0)
        return self.hc[next].deno(cm_)

    def tres_ned_cm(self, ned, cm_):
        if len(cm_) == 0:
            self.hc[ned.sc] = ned
            return

        next = cm_.pop(0)
        self.hc[next].tres_ned_cm(ned, cm_)

    def inte(self, val_origen, val_destino):
        cm_1 = self.nif(val_origen, [])
        cm_2 = self.nif(val_destino, [])
        aux_1 = self.deno(copy.copy(cm_1))
        aux_2 = self.deno(copy.copy(cm_2))
        self.tres_ned_cm(aux_2, cm_1[:-1])
        self.tres_ned_cm(aux_1, cm_2[:-1])


if __name__ == "__main__":
    an = AN(4)
    an.tres(2, 4)
    an.tres(3, 4)
    an.tres(1, 2)
    an.tres(5, 2)
    an.tres(6, 3)
    an.tres(8, 2)
    an.tres(7, 3)
    an.tres(7, 6)
    an.tres(10, 11)
    out = an.nif(7, [])
    print(out)
    an.deno(out)
    an_n = AN(15)
    cm_aux = [2, 5]
    an.tres_ned_cm(an_n, cm_aux)
    an.inte(2, 6)
