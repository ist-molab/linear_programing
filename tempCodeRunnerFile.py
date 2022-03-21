    A = [[3, 2], [1, 2]]
    b = [12, 8]
    c = [-1, -1]
    solver = Solver(c, A, b, method='naive')
    ans = solver.optimize()
    print(ans)