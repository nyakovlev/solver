# A conv is a module with a set of inputs and outputs.
#   A module will have controls for fwd, bwd, and deriv (& deriv^2)
# A node is basically a connection! (connects to everything and equates value)
#   Holds all generated/realized data for template
#   How persistent values exist (like control plane config) is an unanswered question
# A CST is used to constrain nodes
#   Nodes can link to CSTs, just like they link to convs
#   CSTs can have exact values, closest values, min or max

class Solver:
    def __init__(self):
        pass

    def solve(self, model):
        model = self.compile_model(model)

    def compile_model(self, model):
        res = {
            "nodes": [],
            "convs": []
        }
        return res


if __name__ == "__main__":
    pass
