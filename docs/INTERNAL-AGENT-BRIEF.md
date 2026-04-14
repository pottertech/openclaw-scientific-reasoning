# Internal Agent Brief

OpenClaw-Scientific-Reasoning is installed.

This capability pack provides tools for:

- exact symbolic mathematics
- scientific and numerical computing
- combinatorial search and scheduling
- logic and constraint reasoning
- convex optimization
- chemistry and physics analysis
- Bayesian uncertainty-aware inference

Use this stack when the task requires formal reasoning, scientific computation, constrained decision-making, or uncertainty quantification.

## Rough tool map

| Task | Use this |
|------|----------|
| Symbolic derivation, simplification, exact math | SymPy or SageMath |
| Numerical simulation, ODE systems | SciPy, pyneqsys, pyodesys |
| Circuit and transfer-function analysis | Lcapy |
| Chemistry and physics workflows | RDKit, Cantera, PySCF |
| Scheduling, routing, assignment, combinatorial search | OR-Tools |
| Satisfiability, policy consistency, symbolic constraints | Z3 |
| Numeric optimization with explicit objectives and limits | CVXPY |
| Posterior inference, credible intervals, noisy evidence | PyMC |

## When NOT to activate

Do not activate this stack for ordinary chat unless the task has enough structure to benefit from formal tools.