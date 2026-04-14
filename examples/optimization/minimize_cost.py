# Constraint Optimization

## Example: Minimize cost subject to resource constraints

```python
import cvxpy as cp

# Variables
x = cp.Variable()
y = cp.Variable()

# Objective: minimize 2*x + 3*y
objective = cp.Minimize(2*x + 3*y)

# Constraints
constraints = [
    x + y >= 10,
    x >= 0,
    y >= 0,
    2*x - y <= 5
]

# Solve
problem = cp.Problem(objective, constraints)
problem.solve()

print("Status:", problem.status)
print("Optimal value:", problem.value)
print("x =", x.value)
print("y =", y.value)
```

**Expected output:**
```
Status: optimal
Optimal value: 25.0
x = 2.5
y = 7.5
```

## Example: Worker assignment

```python
from ortools.sat.python import cp_model

model = cp_model.CpModel()

# 3 workers, 3 jobs
workers = range(3)
jobs = range(3)

# Variables: x[w][j] = 1 if worker w does job j
x = {}
for w in workers:
    for j in jobs:
        x[w, j] = model.NewBoolVar(f"x_{w}_{j}")

# Each worker assigned to exactly one job
for w in workers:
    model.Add(sum(x[w, j] for j in jobs) == 1)

# Each job assigned to exactly one worker
for j in jobs:
    model.Add(sum(x[w, j] for w in workers) == 1)

# Solve
solver = cp_model.CpSolver()
solver.Solve(model)

# Print assignment
for w in workers:
    for j in jobs:
        if solver.Value(x[w, j]) == 1:
            print(f"Worker {w} -> Job {j}")
```