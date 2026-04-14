OpenClaw-Scientific-Reasoning is available.

## Reasoning domains

- symbolic math
- scientific computing
- optimization
- constraint reasoning
- chemistry
- physics
- uncertainty-aware inference

## Tool selection guide

| Problem type | Use this tool |
|--------------|---------------|
| Exact symbolic work (derive, simplify, solve algebraically) | SymPy or SageMath |
| Numerical ODE/simulation | SciPy, pyodesys, optlang |
| Assignment, routing, packing, scheduling | OR-Tools |
| Logical consistency, satisfiability | Z3 |
| Convex optimization with objectives/limits | CVXPY |
| Confidence, posterior, noisy evidence | PyMC |
| Molecular structure, fingerprints, reactions | RDKit |
| Combustion, thermodynamics | Cantera |
| Circuit analysis, transfer functions | Lcapy |
| Quantum chemistry | PySCF |

## When to activate

Do not trigger these tools for ordinary chat unless the problem is structured enough to benefit from formal reasoning. This stack is for tasks requiring precision, not casual conversation.

## Status reporting

When using a tool from this stack, report the tool name, status (running/complete/failed), and the key result in plain text for humans.