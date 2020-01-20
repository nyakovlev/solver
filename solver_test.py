import unittest
import solver


def get_solver():
    return solver.AggSolver()


class AggSolveTests(unittest.TestCase):
    def test_basic(self):
        params = ["w", "x", "y", "z"]
        eqs = [
            [
                ["w", "x", "y"],
                [18]
            ],
            # [
            #     ["x", "y", "z"],
            #     [21]
            # ],
            [
                ["y", "z", "w"],
                [20]
            ],
            [
                ["z", "w", "x"],
                [19]
            ]
        ]
        s = get_solver()
        ans = {"w": 5, "x": 6, "y": 7, "z": 8}
        res = s.solve(eqs, params)
        self.assertEqual(ans, res, "Solve did not return correct answer.")


if __name__ == "__main__":
    unittest.main()
