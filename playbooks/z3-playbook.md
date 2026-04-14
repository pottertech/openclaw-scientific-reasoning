# Z3 Playbook

## Purpose
Z3 is an SMT (Satisfiability Modulo Theories) solver by Microsoft. Use it for logical constraint solving, satisfiability checking, verification, and symbolic execution.

## When to use Z3

- Checking if a set of logical constraints is satisfiable
- Verification of system properties (e.g., if admin then audit)
- Solving systems of constraints over integers, reals, arrays
- Program verification and symbolic execution
- Scheduling with complex logical constraints

## When NOT to use Z3

- Continuous convex optimization (use CVXPY)
- Large-scale combinatorial optimization (use OR-Tools)
- Pure numerical simulation (use SciPy)

## Sample prompts

```
Is (x > 0 and x < -1) satisfiable?
Check if these three constraints are consistent
Find a model where user is admin implies audit is enabled
```

## Common mistakes

1. **Not checking the result properly**: Always check `s.check()` returns `sat`
2. **Forgetting to get the model**: Use `s.model()` to extract variable assignments
3. **Using Python equality with Z3**: Use `x == y` not `x = y` for Z3 expressions

## Fallback tool
OR-Tools (for large-scale combinatorial scheduling)