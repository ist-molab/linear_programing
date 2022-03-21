## Linear programing solver
Only support naive brute force algorithm and support inequality standard form like below so far.
```
min     c@x
s.t.    A@x <= b
```

## How to use 
The interface is almost same as [scipy.optimize.linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

```
A = [[3, 2], [1, 2]]
b = [12, 8]
c = [-1, -1]
solver = Solver(c, A, b, method='naive')
ans = solver.optimize()
print(ans)
"""
{'x': array([2., 3.]), 'slack': array([0., 0.]), 'fun': -5.0}
"""
```


## refs
scipy implementation  
- [simplex](https://github.com/scipy/scipy/blob/v1.8.0/scipy/optimize/_linprog_simplex.py)  
- [interior point](https://github.com/scipy/scipy/blob/v1.8.0/scipy/optimize/_linprog_ip.py)
- [revised simplex](https://github.com/scipy/scipy/blob/v1.8.0/scipy/optimize/_linprog_rs.py)