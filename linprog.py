import numpy as np
from itertools import combinations


class Solver:
    def __init__(self, c, A, b):
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
        self.num_constraints, self.num_var = self.A.shape
        self.exA = np.hstack((self.A, np.diag(np.ones(self.num_constraints))))
        self.exb = np.hstack((self.b, np.zeros(self.num_constraints)))
        self.exc = np.hstack((self.c, np.zeros(self.num_constraints)))

    def optimize(self):
        idx_list = combinations(
            np.arange(self.num_constraints + self.num_var), self.num_var)

        opt_val = np.inf
        opt_sol = np.zeros(self.num_constraints + self.num_var)

        for idx in idx_list:
            vals = np.linalg.solve(self.exA[:, idx], self.exb[list(idx)])
            temp_sol = np.zeros(self.num_constraints + self.num_var)
            for i, val in zip(idx, vals):
                temp_sol[i] = val
            temp_val = self.exc @ temp_sol
            if temp_val < opt_val:
                opt_val = temp_val
                opt_sol = temp_sol

        ret = {
            'x': opt_sol[:self.num_var],
            'slack': opt_sol[self.num_var:],
            'fun': opt_val
        }

        return ret


if __name__ == '__main__':
    A = [[3, 2], [1, 2]]
    b = [12, 8]
    c = [-1, -1]
    solver = Solver(c, A, b)
    ans = solver.optimize()
    print(ans)
