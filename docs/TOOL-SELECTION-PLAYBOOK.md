# Tool Selection Playbook

This playbook helps agents select the right tool for a given problem.

## Decision flowchart

```
Is exact symbolic solution needed?
├── YES → Is advanced algebra/number theory required?
│   ├── YES → SageMath
│   └── NO → SymPy
└── NO ↓

Is the problem about circuits/electrical systems?
├── YES → Lcapy
└── NO ↓

Is the problem about molecules/reactions/chemistry?
├── YES → Is quantum chemistry needed?
│   ├── YES → PySCF
│   ├── NO → Is combustion/thermodynamics needed?
│   │   ├── YES → Cantera
│   │   └── NO → RDKit
└── NO ↓

Is the problem about uncertainty/Bayesian inference?
├── YES → PyMC
└── NO ↓

Is the problem a discrete combinatorial optimization?
├── YES → OR-Tools
└── NO ↓

Is the problem about logical constraints/satisfiability?
├── YES → Z3
└── NO ↓

Is the problem continuous convex optimization?
├── YES → CVXPY
└── NO ↓

Default → SciPy
```

## Problem → Tool mapping

| Problem type | Best tool | Alternative |
|-------------|-----------|-------------|
| Simplify expression | SymPy | SageMath |
| Solve polynomial | SymPy | SageMath |
| Integrate symbolically | SymPy | - |
| Circuit analysis | Lcapy | SciPy (numerical) |
| ODE system | SciPy | pyodesys |
| Nonlinear equations | pyneqsys | SciPy root |
| Scheduling | OR-Tools | - |
| Routing | OR-Tools | - |
| Bin packing | OR-Tools | - |
| Linear/quadratic programming | CVXPY | OR-Tools |
| Satisfiability | Z3 | OR-Tools SAT |
| Logical verification | Z3 | - |
| Bayesian inference | PyMC | - |
| Molecule analysis | RDKit | - |
| Combustion | Cantera | - |
| Quantum chemistry | PySCF | - |

## When in doubt

1. Start with SciPy for numerical problems
2. Start with SymPy for symbolic problems
3. Check the example prompts in each playbook for similar problems
4. Use the routing hints in `config/router-hints.json`