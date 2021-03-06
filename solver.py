from pprint import pprint
import math


class AggSolver:
    def __init__(self, swap=None, op=None, div=None):
        self.swap = (lambda x: -x) if swap is None else swap
        self.op = (lambda x, y: x + y) if op is None else op
        self.div = (lambda x, ct: x / ct) if div is None else div

    def solve(self, eqs, params):
        res = []
        nparams = {}
        steps = 0
        while True:
            neqs = self.get_cmbs(eqs)
            self.filter_existing(eqs, neqs)
            if len(neqs) == 0:
                break
            neq, score = self.get_next_best(neqs)
            eqs.append(neq)
            print(score, neq)
            if score == 1:
                res.append(neq)
                k, v = self.resolve(neq)
                nparams[k] = v
                self.substitute(eqs, k, v)
                # eqs.append([[k], [v]])
            if len(res) >= len(params):
                break
            steps += 1
        print(nparams)
        return nparams

    def substitute(self, eqs, k, v):
        for eq in eqs:
            for s in [0, 1]:
                if k in eq[s]:
                    for i in range(0, len(eq[s])):
                        if eq[s][i] == k:
                            eq[s][i] = v

    def resolve(self, eq):
        vnms = [i for i in eq[0] + eq[1] if type(i) is str]
        div = len(vnms)
        vnm = vnms[0]
        if vnm in eq[1]:
            eq = [eq[1], eq[0]]
        v = [i for i in eq[1]]
        for i in eq[0]:
            if type(i) is not str:
                v.append(self.swap(i))
        ans = v[0]
        for i in range(1, len(v)):
            ans = self.op(ans, v[i])
        if div > 1:
            ans = self.div(ans, div)
        return vnm, ans

    def get_next_best(self, eqs):
        score = None
        res = None
        for eq in eqs:
            cscore = len(list(set([i for i in eq[0] if type(i) is str] + [i for i in eq[1] if type(i) is str])))
            if cscore > 0:
                if res is None or cscore < score:
                    score = cscore
                    res = eq
        return res, score

    # def get_score(self, eq):
    #     eq = [[i for i in eq[0] if type(i) is str], [i for i in eq[1] if type(i) is str]]
    #     eq = self.reduce(eq)
    #     rm = []
    #     a = [i for i in eq[0]]
    #     b = [i for i in eq[1]]
    #     for i in a:
    #         if i in b:
    #             b.remove(i)
    #             rm.append(i)
    #     for i in rm:
    #         a.remove(i)

    def filter_existing(self, base, ns):
        for i in reversed(range(0, len(ns))):
            for b in base:
                try:
                    if self.match(b, ns[i]):
                        del ns[i]
                except:
                    pass

    def match(self, a, b):
        ea = [[i for i in a[0] if type(i) is str], [i for i in a[1] if type(i) is str]]
        ea = self.reduce(ea)
        ea[0].sort()
        ea[1].sort()
        ea.sort()
        eb = [[i for i in b[0] if type(i) is str], [i for i in b[1] if type(i) is str]]
        eb = self.reduce(eb)
        eb[0].sort()
        eb[1].sort()
        eb.sort()
        return ea == eb

    def reduce(self, eq):
        c = [{}, {}]
        for i in [0, 1]:
            for v in eq[i]:
                if v not in c[i]:
                    c[i][v] = 0
                c[i][v] += 1
        cs = list(c[0].items()) + list(c[1].items())
        gcd = None
        for i in range(1, len(cs)):
            gcd = math.gcd(cs[i][1], (cs[i - 1][1] if gcd is None else gcd))
        if gcd == 1:
            return eq
        for i in [0, 1]:
            c[i] = {k: v / gcd for k, v in c[i].items()}
            c[i] = [k for k, v in c[i].items() for j in range(0, int(v))]
        return c

    def get_cmbs(self, eqs):
        res = []
        for i in range(0, len(eqs)):
            eq = eqs[i]
            seqs = eqs[i + 1:]
            for seq in seqs:
                res.append(self.cmb(eq, seq))
                res.append(self.cmb(eq, [seq[1], seq[0]]))
        return res

    def cmb(self, eq1, eq2):
        a = eq1[0] + eq2[0]
        b = eq1[1] + eq2[1]
        rm = []
        for i in a:
            if i in b:
                b.remove(i)
                rm.append(i)
        for i in rm:
            a.remove(i)
        return [a, b]
