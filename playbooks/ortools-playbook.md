# OR-Tools Playbook

## Purpose
OR-Tools (Operations Research Tools) by Google is a fast and scalable optimization library. Use it for combinatorial optimization, scheduling, routing, packing, assignment, and other discrete optimization problems.

## When to use OR-Tools

- Vehicle routing and TSP variants
- Worker or task assignment
- Bin packing and container loading
- Job shop scheduling
- Crew scheduling (airlines, trains)
- Boolean satisfiability (SAT mode)

## When NOT to use OR-Tools

- Continuous convex optimization (use CVXPY)
- Symbolic mathematics (use SymPy)
- Satisfiability of non-boolean constraints (check if Z3 SMT solver is better)

## Sample prompts

```
Assign 5 workers to 5 jobs to minimize total cost
Find the shortest path visiting 10 cities
Pack 50 boxes of various sizes into minimum bins
```

## Common mistakes

1. **Not setting the solver type correctly**: CP-SAT is usually fastest for combinatorial problems
2. **Forgetting to add the search phase**: Some problems need explicit `EnumerateLargeSolutions`
3. **Using wrong routing model**: Use the appropriate model type for your routing problem

## Fallback tool
Z3 (for constraint satisfaction with complex logical constraints)