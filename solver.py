from pprint import pprint


class AggSolver:
    def __init__(self, swap=None, op=None, div=None):
        self.swap = (lambda x: -x) if swap is None else swap
        self.op = (lambda x, y: x + y) if op is None else op
        self.div = (lambda x, ct: x / ct) if div is None else div

    def solution(self, eqs, p):
        for e in eqs:
            for si, s in enumerate(e):
                vs = [i for i in s if type(i) is str]
                if len(vs) == 1 and vs[0] == p:
                    return e[int(not si)]

    def solved(self, eqs, params):
        return not any([self.solution(eqs, p) is None for p in params])

    def add_eq(self, eqs, rt_map=None):
        if rt_map is None:
            rt_map = {}
        best = {
            "i": None,
            "oi": None,
            "unsolved": -1,
            "total": -1,
            "flip": False
        }
        for i in range(0, len(eqs)):
            e = eqs[i]
            rts = rt_map[i] if i in rt_map else []
            ois = [oi for oi in range(0, len(eqs)) if oi != i and oi not in rts]
            for oi in ois:
                oe = eqs[oi]
                u, t, f = self.get_reduction(e, oe)
                self.update_best(best, i, oi, u, t, f)
        if best["i"] is not None:
            pprint(best)
            ne = self.combine_eqs(eqs[best["i"]], eqs[best["oi"]])
            rt_map[len(eqs)] = [best["i"], best["oi"]]
            eqs.append(ne)
            return ne

    def update_best(self, best, i, oi, u, t, f):
        if u == 0:
            return
        if u < t:
            if (u < best["unsolved"]) or (u == best["unsolved"] and t < best["total"]):
                best["i"] = i
                best["oi"] = oi
                best["unsolved"] = u
                best["total"] = t
                best["flip"] = f

    def get_reduction(self, a, b):
        for e in [a, b]:
            for ei in [0, 1]:
                e[ei] = [i for i in e[ei] if type(i) is str]
        t = len(list(set(a[0] + a[1] + b[0] + b[1])))
        u1 = self.get_u(a[0] + b[0], a[1] + b[1])
        u2 = self.get_u(a[0] + b[1], a[1] + b[0])
        if 0 < u2 < u1:
            return u2, t, True
        else:
            return u1, t, False

    def get_u(self, a, b):
        a = [i for i in a]
        b = [i for i in b]
        rm = []
        for i in a:
            if i in b:
                rm.append(i)
                b.remove(i)
        for i in rm:
            a.remove(i)
        return len(list(set(a + b)))

    def combine_eqs(self, a, b):
        pass

    def solve(self, eqs, params):
        while not self.solved(eqs, params):
            if not self.add_eq(eqs):
                break
        return {p: self.solution(eqs, p) for p in params}
