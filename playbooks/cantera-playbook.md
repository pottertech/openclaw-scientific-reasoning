# Cantera Playbook

## Purpose
Cantera is a toolkit for thermodynamic, chemical kinetics, and transport calculations. Use it for combustion simulation, reaction mechanism analysis, thermodynamic property calculation, and chemical equilibrium.

## When to use Cantera

- Combustion and flame simulation
- Chemical equilibrium calculations
- Reaction mechanism analysis
- Thermodynamic property lookup (Cp, H, S)
- Species and phase equilibrium

## When NOT to use Cantera

- Molecular structure analysis (use RDKit)
- Symbolic circuit analysis (use Lcapy)
- Quantum chemistry (use PySCF)

## Sample prompts

```
Calculate the adiabatic flame temperature for methane-air
Find the equilibrium composition at 1000K and 1 atm
Simulate a plug flow reactor with a given mechanism
```

## Common mistakes

1. **Not having a valid mechanism file**: Cantera needs CTI or XML mechanism files
2. **Confusing ideal gas with other models**: Be explicit about the phase model
3. **Forgetting to set temperature/pressure units**: Cantera uses SI units (K, Pa)

## Fallback tool
RDKit (for molecular structure) or SciPy (for general scientific computing)