# Logic and Constraint Satisfaction

## Example: Check satisfiability

```python
from z3 import Int, Solver, sat

x = Int('x')

s = Solver()
s.add(x > 1)
s.add(x < -1)

result = s.check()
print("Constraints:", ["x > 1", "x < -1"])
print("Satisfiable?", result == sat)
```

**Expected output:**
```
Constraints: ['x > 1', 'x < -1']
Satisfiable? False
```

## Example: Find a satisfying assignment

```python
from z3 import Int, Real, Solver, sat

x = Int('x')
y = Int('y')

s = Solver()
s.add(x + 2*y == 10)
s.add(x - y == 2)

result = s.check()
if result == sat:
    model = s.model()
    print(f"x = {model[x]}")
    print(f"y = {model[y]}")
```

**Expected output:**
```
x = 6
y = 4
```