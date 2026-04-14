# SciPy Playbook

## Purpose
SciPy is a Python library for scientific computing that provides numerical integration, interpolation, optimization, linear algebra, statistics, and more. Use it for numerical simulation, data analysis, and scientific computation where exact symbolic solutions are not available.

## When to use SciPy

- Numerical integration (quad, trapz, simps)
- Solving ODE systems (solve_ivp, odeint)
- Numerical optimization (minimize, root)
- Sparse linear algebra
- Statistical tests and distributions
- Signal processing and FFT

## When NOT to use SciPy

- Exact symbolic algebra (use SymPy)
- Discrete combinatorial optimization (use OR-Tools)
- Constraint satisfaction / SAT (use Z3)
- Bayesian inference (use PyMC)

## Sample prompts

```
Integrate sin(x) from 0 to pi numerically
Solve dy/dt = -k*y with y(0)=1, k=0.5 on [0,5]
Find the minimum of x^4 - 14*x^3 + 60*x^2 - 70*x
```

## Common mistakes

1. **Confusing SciPy and NumPy**: SciPy builds on NumPy; import `scipy.integrate` not just `numpy`
2. **Not providing correct initial conditions for ODEs**
3. **Using scalar optimization on vector problems**: Ensure your objective handles arrays correctly

## Fallback tool
SymPy (for exact symbolic integration or solving when possible)