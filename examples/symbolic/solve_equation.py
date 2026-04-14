# Symbolic Equation Solving

## Example: Solve x^4 - 5x^2 + 6 = 0

```python
from sympy import symbols, solve, pprint

x = symbols('x')
equation = x**4 - 5*x**2 + 6
solutions = solve(equation, x)

print("Equation: x^4 - 5x^2 + 6 = 0")
print("Solutions:", solutions)
```

**Expected output:**
```
Solutions: [-sqrt(2), sqrt(2), -sqrt(3), sqrt(3)]
```

## Example: Simplify (x^3 - 1)/(x - 1)

```python
from sympy import symbols, simplify

x = symbols('x')
expr = (x**3 - 1)/(x - 1)
simplified = simplify(expr)

print("Original:", expr)
print("Simplified:", simplified)
```

**Expected output:**
```
Simplified: x^2 + x + 1
```

## Example: Symbolically integrate x^2 * exp(x)

```python
from sympy import symbols, integrate, exp

x = symbols('x')
result = integrate(x**2 * exp(x), x)

print("Integral of x^2 * e^x dx:")
pprint(result)
```