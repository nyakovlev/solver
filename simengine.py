import yaml


CFILE = "sample_csts.yml"


class Solver:
    def __init__(self, props):
        self.props = props
        self.rcst_map = {}
        self.comp_map = {}
        for i, d in props.items():
            self.add(i, d)
        self.cache = {}
        self.comps = {
            "add": lambda x, y: x + y,
            "mult": lambda x, y: x * y
        }
        self.convs = {
            "recip": lambda d, x: 1/x,
            "minus": lambda d, x: -x
        }

    def add(self, name, d):
        t = d["type"] if "type" in d else "raw"
        if t == "cst":
            self.add_cst(name, d)
        elif t == "computed":
            self.add_computed(name, d)

    def add_cst(self, name, d):
        k = tuple(d["k"])
        if k not in self.rcst_map:
            self.rcst_map[k] = []
        self.rcst_map[k].append({
            "dst": name,
            "v": d["v"]
        })

    def add_computed(self, name, d):
        self.comp_map[(name,)] = d

    def solve(self):
        pass

    def get(self, path):
        # if fully-defined, return def
        # if not, create best definition from upstream and downstream csts
        # cache csts for future lookup; remove cache when new csts affect value
        path = tuple(path)
        if path in self.comp_map:
            return self.compute(self.comp_map[path])
        if path in self.rcst_map:
            d = self.rcst_map[path]
            if len(d) > 0:
                return d[0]["v"]

    def compute(self, d):
        agg = None
        agg_f = self.comps[d["method"]] if "method" in d else self.comps["add"]
        for link in d["links"]:
            v = self.get(link["src"])
            if "convs" in link:
                for c in link["convs"]:
                    v = self.conv(v, c)
            agg = v if agg is None else agg_f(agg, v)
        return agg

    def conv(self, v, op):
        return self.convs[op["type"]](op, v)


if __name__ == "__main__":
    with open(CFILE, "r") as f:
        layout = yaml.safe_load(f)
    s = Solver(layout)
    print(s.get(["circuit_1_i"]))
