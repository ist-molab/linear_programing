import numpy as np
from itertools import combinations


class Solver:
    def __init__(self, c, A, b):
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
        self.num_constraints, self.num_var = self.A.shape
        self.exA = np.hstack((self.A, np.diag(np.ones(self.num_constraints))))
        self.exc = np.hstack((self.c, np.zeros(self.num_constraints)))

    def optimize(self):
        idx_list = combinations(
            np.arange(self.num_constraints + self.num_var), self.num_constraints)

        opt_val = np.inf
        opt_sol = np.zeros(self.num_constraints + self.num_var)

        for idx in idx_list:
            try:
                vals = np.linalg.solve(self.exA[:, idx], self.b)
            except:
                vals = np.linalg.pinv(self.exA[:, idx]) @ self.b
            temp_sol = np.zeros(self.num_constraints + self.num_var)
            for i, val in zip(idx, vals):
                temp_sol[i] = val
            temp_val = self.exc @ temp_sol
            if not (temp_sol + 1e-5 >= 0).all():
                continue
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
    A = [[3, 1, 2], [1, 3, 0], [0, 2, 4]]
    b = [60, 36, 48]
    c = [-150, -200, -300]
    solver = Solver(c, A, b)
    ans = solver.optimize()
    print(ans)
