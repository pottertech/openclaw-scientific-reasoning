# PySCF Playbook

## Purpose
PySCF is a Python-based computational chemistry program for ab initio calculations. Use it for Hartree-Fock, density functional theory (DFT), second-order Møller-Plesset perturbation theory (MP2), and other quantum chemistry methods.

## When to use PySCF

- Quantum chemistry calculations (HF, DFT, MP2)
- Electronic structure calculations
- Computing molecular orbital energies
- Ground state energy calculations
- Property calculation (dipole, polarizability)

## When NOT to use PySCF

- Molecular structure analysis (use RDKit)
- Combustion simulation (use Cantera)
- General numerical simulation (use SciPy)

## Sample prompts

```
Calculate the ground state energy of water (H2O) with STO-3G basis
Run a Hartree-Fock calculation on hydrogen fluoride
Compute the dipole moment of water at HF/6-31G level
```

## Common mistakes

1. **Not choosing appropriate basis set**: Larger basis sets are more accurate but slower
2. **Confusing restricted and unrestricted calculations**: Use RHF/UHF for open-shell systems
3. **Forgetting to specify molecular geometry correctly**: PySCF needs Cartesian or internal coordinates

## Fallback tool
RDKit (for molecular structure) or SciPy (for general computing)