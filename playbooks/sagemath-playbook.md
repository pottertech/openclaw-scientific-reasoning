# SageMath Playbook

## Purpose
SageMath (Sage) is a free open-source mathematics software system that combines the power of many packages including SymPy, Maxima, GAP, and more. Use it for advanced algebraic geometry, number theory, group theory, and as a unified interface to many mathematical tools.

## When to use SageMath

- Advanced algebraic geometry problems
- Number theoretic computations
- Group theory and representation theory
- Cryptographic algorithm exploration
- Complex multi-tool mathematical workflows
- When you need an interface to multiple math systems

## When NOT to use SageMath

- Simple symbolic algebra (SymPy is faster and lighter)
- Production numerical computing (SciPy/NumPy are more efficient)
- When Sage is not installed on the target system

## Sample prompts

```
Solve x^5 - x^3 + 2*x - 1 = 0 over QQ
Compute the Galois group of x^4 - 2
Find all roots of unity of order 12
```

## Common mistakes

1. **Not checking if Sage is installed**: Run `sage --version`
2. **Using Sage syntax in SymPy**: They share some syntax but differ in many ways
3. **Assuming Sage cell server is running**: For notebook mode, ensure the Sage kernel is active

## Fallback tool
SymPy (for pure symbolic work when Sage is unavailable)