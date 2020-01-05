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
            "total": -1
        }
        for i in range(0, len(eqs)):
            e = eqs[i]
            rts = rt_map[i] if i in rt_map else []
            ois = [oi for oi in range(0, len(eqs)) if oi != i and oi not in rts]
            for oi in ois:
                oe = eqs[oi]
                u, t = self.get_reduction(e, oe)
                self.update_best(best, i, oi, u, t)
        if best["i"] is not None:
            ne = self.get_reduction(eqs[best["i"]], eqs[best["oi"]])
            rt_map[len(eqs)] = [best["i"], best["oi"]]
            eqs.append(ne)
            return ne

    def update_best(self, best, i, oi, u, t):
        if u == 0:
            return
        if (u < best["unsolved"]) or (u == best["unsolved"] and t < best["total"]):
            best["i"] = i
            best["oi"] = oi
            best["unsolved"] = u
            best["total"] = t

    def get_reduction(self, a, b):
        return 0, 0

    def combine_eqs(self, a, b):
        pass

    def solve(self, eqs, params):
        while not self.solved(eqs, params):
            if not self.add_eq(eqs):
                break
        return {p: self.solution(eqs, p) for p in params}
