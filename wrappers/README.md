# Wrappers

This directory contains wrapper contracts and templates for the scientific reasoning tools.

## Contracts

The `contracts/` directory contains JSON schemas that all tool wrappers must implement:

- `base-contract.json` - Base interface for all wrappers
- `symbolic-contract.json` - For SymPy and SageMath
- `optimization-contract.json` - For OR-Tools and CVXPY
- `constraint-contract.json` - For Z3
- `uncertainty-contract.json` - For PyMC

## Templates

The `templates/` directory contains reference wrapper implementations:

- `sympy-wrapper-template.py` - SymPy wrapper
- `scipy-wrapper-template.py` - SciPy wrapper
- `ortools-wrapper-template.py` - OR-Tools wrapper
- `z3-wrapper-template.py` - Z3 wrapper
- `cvxpy-wrapper-template.py` - CVXPY wrapper
- `pymc-wrapper-template.py` - PyMC wrapper

## Usage

Wrappers read JSON from stdin and write JSON to stdout:

```python
import json
data = json.load(sys.stdin)
output = invoke(data["operation"], data["inputs"])
print(json.dumps(output))
```

## Implementing a new wrapper

1. Copy the appropriate contract to use as your schema
2. Implement the wrapper following the contract schema
3. Test with the smoke tests in `tests/wrappers/`