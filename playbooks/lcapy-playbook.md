# Lcapy Playbook

## Purpose
Lcapy is a Python library for symbolic circuit analysis. It uses SymPy for symbolic manipulation and can analyze circuits containing resistors, capacitors, inductors, sources, and complex impedance. Use it for circuit analysis, transfer functions, and system dynamics.

## When to use Lcapy

- Circuit analysis with resistors, inductors, capacitors
- Finding transfer functions for RLC circuits
- Impedance and admittance calculations
- Bode plot generation for control systems
- Laplace and Fourier analysis of circuits

## When NOT to use Lcapy

- Molecular or chemical analysis (use RDKit or Cantera)
- General numerical simulation (use SciPy)
- Discrete optimization problems (use OR-Tools)

## Sample prompts

```
Analyze a series RLC circuit with voltage source
Find the transfer function for a low-pass RC filter
Compute impedance of parallel R and C at frequency 1kHz
```

## Common mistakes

1. **Confusing time-domain and frequency-domain**: Lcapy handles both; be explicit about which you want
2. **Not declaring Laplace variables correctly**: Use proper s-domain notation
3. **Forgetting to use .simplify()**: Circuit expressions can be complex; simplify for readability

## Fallback tool
SciPy (for numerical frequency response analysis)