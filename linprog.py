import numpy as np
import _linprog_naive


class Solver:
    def __init__(self, c, A, b, method):
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
        self.num_constraints, self.num_var = self.A.shape
        self.exA = np.hstack((self.A, np.diag(np.ones(self.num_constraints))))
        self.exb = np.hstack((self.b, np.zeros(self.num_constraints)))
        self.exc = np.hstack((self.c, np.zeros(self.num_constraints)))
        self.method = method

    def optimize(self):
        if self.method == 'naive':
            solver = _linprog_naive.Solver(c, A, b)
        return solver.optimize()


if __name__ == '__main__':
    A = [[1, 3], [1, 1], [2, 1]]
    b = [9, 4, 6]
    c = [-2, -3]
    solver = Solver(c, A, b, method='naive')
    ans = solver.optimize()
    print(ans)
