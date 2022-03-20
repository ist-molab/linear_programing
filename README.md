## linear programing solver
Only support naive brute force algorithm and support inequality standard form like below so far.
```
min     c@x
s.t.    A@x <= b
```

## how to use 
The interface is almost same as [scipy.optimize.linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

```
from linprog import Solver
A = [[3, 2], [1, 2]]
b = [12, 8]
c = [-1, -1]
solver = Solver(c, A, b)
ans = solver.optimize()
print(ans)
"""
{'x': array([2., 3.]), 'slack': array([0., 0.]), 'fun': -5.0}
"""
```
