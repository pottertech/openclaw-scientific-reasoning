# OpenClaw-Scientific-Reasoning Tool Inventory

This document provides a comprehensive inventory of all tools included in the OpenClaw-Scientific-Reasoning capability pack.

## Symbolic Mathematics

### SymPy
- **Purpose**: Pure Python symbolic mathematics
- **Core capabilities**: Algebra, calculus, matrix operations, polynomial manipulation, set theory, boolean algebra
- **Install name**: `sympy`
- **Wrapper contract**: `symbolic-contract.json`

### SageMath
- **Purpose**: Unified mathematics system integrating many tools
- **Core capabilities**: Advanced algebra, number theory, algebraic geometry, group theory
- **Install name**: System installation (not pip)
- **Wrapper contract**: `symbolic-contract.json`

## Scientific Computing

### SciPy
- **Purpose**: Numerical scientific computing
- **Core capabilities**: Integration, ODE solving, optimization, linear algebra, statistics, signal processing
- **Install name**: `scipy`
- **Wrapper contract**: `scientific-contract.json`

### pyneqsys
- **Purpose**: Numerical equation system solving
- **Core capabilities**: Systems of nonlinear equations, root finding
- **Install name**: `pyneqsys`
- **Wrapper contract**: `scientific-contract.json`

### pyodesys
- **Purpose**: Numerical ODE system solving
- **Core capabilities**: ODE system integration, stiff systems, chemical kinetics
- **Install name**: `pyodesys`
- **Wrapper contract**: `scientific-contract.json`

### optlang
- **Purpose**: Interface to optimization solvers
- **Core capabilities**: Constraint-based optimization for systems biology
- **Install name**: `optlang`
- **Wrapper contract**: `optimization-contract.json`

### Lcapy
- **Purpose**: Symbolic circuit analysis
- **Core capabilities**: Circuit analysis, transfer functions, Laplace transforms, impedance
- **Install name**: `lcapy`
- **Wrapper contract**: `scientific-contract.json`

## Discrete Optimization

### OR-Tools
- **Purpose**: Combinatorial and discrete optimization
- **Core capabilities**: Scheduling, routing, assignment, bin packing, vehicle routing, SAT
- **Install name**: `ortools`
- **Wrapper contract**: `optimization-contract.json`

## Continuous Optimization

### CVXPY
- **Purpose**: Convex optimization modeling
- **Core capabilities**: Linear, quadratic, second-order cone, semidefinite programming
- **Install name**: `cvxpy`
- **Wrapper contract**: `optimization-contract.json`

## Constraint Reasoning

### Z3
- **Purpose**: SMT solver and constraint reasoning
- **Core capabilities**: Satisfiability checking, logical verification, symbolic execution
- **Install name**: `z3-solver`
- **Wrapper contract**: `constraint-contract.json`

## Uncertainty Inference

### PyMC
- **Purpose**: Bayesian probabilistic programming
- **Core capabilities**: MCMC posterior inference, credible intervals, hierarchical models
- **Install name**: `pymc`
- **Wrapper contract**: `uncertainty-contract.json`

## Chemistry

### RDKit
- **Purpose**: Cheminformatics and molecular modeling
- **Core capabilities**: SMILES parsing, fingerprints, substructure search, property calculation
- **Install name**: `rdkit`
- **Wrapper contract**: `chemistry-contract.json`

### Cantera
- **Purpose**: Thermodynamics and chemical kinetics
- **Core capabilities**: Combustion, equilibrium, reaction mechanisms, thermodynamic properties
- **Install name**: `cantera`
- **Wrapper contract**: `chemistry-contract.json`

### PySCF
- **Purpose**: Ab initio quantum chemistry
- **Core capabilities**: HF, DFT, MP2 calculations, electronic structure
- **Install name**: `pyscf`
- **Wrapper contract**: `chemistry-contract.json`

## Tool Status Reporting

When using any tool from this stack, report:
1. Tool name and version
2. Status (running/complete/failed)
3. Key results in human-readable format
4. Any errors encountered