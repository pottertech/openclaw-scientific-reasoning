# Routing Guide

This guide explains how to route problems to the correct reasoning domain in OpenClaw-Scientific-Reasoning.

## Domain routing table

| Prompt keywords | Domain | Tool |
|-----------------|--------|------|
| derive, simplify, symbolic, exact, algebra | symbolic_math | SymPy, SageMath |
| simulate, numerical, ode, differential equation | scientific_computing | SciPy, pyodesys |
| schedule, assign, route, packing, TSP | optimization_discrete | OR-Tools |
| minimize, maximize, objective, convex | optimization_continuous | CVXPY |
| satisfiable, contradiction, verify, proof | constraint_reasoning | Z3 |
| uncertainty, posterior, Bayesian, credible | uncertainty_inference | PyMC |
| molecule, reaction, SMILES, fingerprint | chemistry | RDKit, Cantera |
| circuit, impedance, transfer, Laplace | physics | Lcapy |

## Routing algorithm

1. **Keyword matching**: Scan prompt for domain keywords
2. **Priority resolution**: If multiple matches, use highest priority
3. **Fallback**: If no match, use general-purpose scientific computing (SciPy)

## Router hints JSON

The `config/router-hints.json` file contains structured routing data. Agents should:

1. Load router hints at startup
2. Match incoming prompts against keyword lists
3. Route to the highest-priority matching domain
4. Return "unknown" if no match with suggestion to use SciPy

## Multi-domain problems

For problems spanning multiple domains:

1. Identify primary domain (largest match)
2. Execute primary domain tool
3. If result needs secondary domain processing, cascade
4. Report results from both domains if relevant

## Example routing

**Prompt**: "Minimize x + 2y subject to x + y >= 10 and x >= 0, y >= 0"

- Keywords: minimize, objective, constraint
- Domain: optimization_continuous
- Tool: CVXPY

**Prompt**: "Find the roots of x^5 - x^3 + 2"

- Keywords: roots, polynomial
- Domain: symbolic_math
- Tool: SymPy