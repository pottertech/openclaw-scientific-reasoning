# Mixed Problem Solving

## Example: Multi-stage reasoning

```python
"""
Example: Combine symbolic solving with optimization.
Find the maximum of f(x) = -x^2 + 4x over [0, 5] and verify it satisfies constraint x^2 <= 25.
"""
from sympy import symbols, diff, solve

x = symbols('x')
f = -x**2 + 4*x

# Find critical point
df = diff(f, x)
critical = solve(df, x)
print(f"Critical point: {critical}")

# Evaluate at critical point
val = f.subs(x, critical[0])
print(f"Maximum value: {val}")

# Verify constraint
print(f"Constraint x^2 <= 25 satisfied: {critical[0]**2 <= 25}")

# Use OR-Tools to assign tasks to workers with cost minimization
from ortools.sat.python import cp_model

model = cp_model.CpModel()
workers = range(3)
tasks = range(3)
costs = [[9, 2, 7], [6, 5, 3], [4, 8, 1]]

x_vars = {}
for w in workers:
    for t in tasks:
        x_vars[w, t] = model.NewBoolVar(f"w{w}_t{t}")

for w in workers:
    model.Add(sum(x_vars[w, t] for t in tasks) == 1)
for t in tasks:
    model.Add(sum(x_vars[w, t] for w in workers) == 1)

model.Minimize(sum(costs[w][t] * x_vars[w, t] for w in workers for t in tasks))

solver = cp_model.CpSolver()
solver.Solve(model)

print("Optimal assignment:")
for w in workers:
    for t in tasks:
        if solver.Value(x_vars[w, t]):
            print(f"  Worker {w} -> Task {t} (cost {costs[w][t]})")
```