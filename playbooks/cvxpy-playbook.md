# CVXPY Playbook

## Purpose
CVXPY is a Python-embedded modeling language for convex optimization. Use it for continuous optimization problems where you have explicit objectives and constraints, such as portfolio optimization, resource allocation, and machine learning regularization.

## When to use CVXPY

- Linear programming (LP)
- Quadratic programming (QP)
- Second-order cone programming (SOCP)
- Semidefinite programming (SDP)
- Portfolio optimization with risk constraints
- Machine learning regularization (lasso, ridge)

## When NOT to use CVXPY

- Discrete combinatorial optimization (use OR-Tools)
- Symbolic constraint solving (use Z3)
- Bayesian uncertainty quantification (use PyMC)

## Sample prompts

```
Minimize (x - 2)^2 subject to x >= 0
Find optimal portfolio allocation maximizing return with 10% max volatility
Solve: minimize ||Ax - b||_2^2 subject to ||x||_1 <= 1
```

## Common mistakes

1. **Forgetting to mark variables as convex/concave**: CVXPY will error if problem is not convex
2. **Using Python operators incorrectly**: Use `*` for matrix multiplication, `*=` for in-place
3. **Not specifying solver explicitly when needed**: Some problems need ECOS, SCS, or GLPK

## Fallback tool
OR-Tools (for mixed-integer programs)