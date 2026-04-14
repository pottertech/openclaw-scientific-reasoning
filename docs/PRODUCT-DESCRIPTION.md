# OpenClaw-Scientific-Reasoning

OpenClaw-Scientific-Reasoning is a portable OpenClaw capability pack that equips AI agents with a broad scientific reasoning stack for exact mathematics, scientific computing, optimization, discrete search, formal logic, chemistry, physics, and uncertainty-aware inference.

## Purpose

Use this stack when the task involves:

- symbolic derivation
- equation solving
- numerical simulation
- constrained optimization
- satisfiability checks
- chemistry or physics computation
- probabilistic reasoning from noisy evidence

## What to avoid

Do not use this stack for ordinary conversation, generic writing, or unstructured brainstorming unless the problem has been formalized enough to benefit from scientific or mathematical tooling.

## Tool selection map

| Domain | Tools | Use when... |
|--------|-------|-------------|
| Symbolic math | SymPy, SageMath | exact algebra, derivation, simplification |
| Scientific computing | SciPy, pyneqsys, pyodesys, optlang | numerical simulation, ODE systems |
| Discrete optimization | OR-Tools | scheduling, routing, assignment, packing |
| Continuous optimization | CVXPY | convex optimization with explicit objectives |
| Constraint reasoning | Z3 | satisfiability, logical consistency, policy checks |
| Uncertainty inference | PyMC | posterior estimation, credible intervals |
| Chemistry | RDKit, Cantera, PySCF | molecule analysis, reactions, quantum chemistry |
| Physics | Lcapy, SciPy, Cantera | circuits, transfer functions, thermodynamics |

## Design principles

1. **Portable** - Usable by any OpenClaw agent, not only Brodie
2. **Explicit** - Capabilities, routing hints, and tool purposes are documented
3. **Safe** - Install and uninstall are predictable and reversible
4. **Modular** - Tool wrappers, playbooks, and metadata are separable
5. **OpenClaw-native** - Fits cleanly into existing OpenClaw patterns