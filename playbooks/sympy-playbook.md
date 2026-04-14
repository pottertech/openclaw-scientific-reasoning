# SymPy Playbook

## Purpose
SymPy is a Python library for symbolic mathematics. Use it for exact algebraic derivation, equation solving, differentiation, integration, matrix operations, and series expansion.

## When to use SymPy

- The problem admits an exact closed-form solution
- You need to simplify a rational expression
- Derivative or integral has an exact symbolic form
- Polynomial factorization or root finding over ℚ or ℝ
- Matrix operations with symbolic entries
- Boolean algebra or set operations

## When NOT to use SymPy

- Numerical approximation only (use SciPy instead)
- Large-scale linear algebra (use NumPy/MATLAB)
- ODE solving when numerical integration is needed (use SciPy odeint)
- High-performance matrix operations (use NumPy directly)

## Sample prompts

```
Simplify: (x^3 - 1)/(x - 1)
Solve: x^2 - 5x + 6 = 0
Differentiate: x^2 * sin(x)
Integrate: x^2 * exp(x) dx
Compute: Matrix([[1, 2], [3, 4]]).det()
```

## Common mistakes

1. **Forgetting to import**: `from sympy import *`
2. **Using Python math functions on SymPy objects**: Use `sympy.sin(x)` not `math.sin(x)`
3. **Not declaring symbols**: `x = Symbol('x')` before use
4. **Assuming infinite precision**: SymPy is exact but can be slow for very large expressions

## Fallback tool
SciPy (for numerical approximations when symbolic is too slow)

## Output format
Report tool name, status, and result clearly. Show the simplified result and note if the expression was expanded, factored, or solved.