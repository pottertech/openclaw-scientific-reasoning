# OpenClaw-Scientific-Reasoning

A unified reasoning toolkit for symbolic math, scientific computing, optimization, constraint solving, and uncertainty-aware inference.

OpenClaw-Scientific-Reasoning is a portable capability pack for OpenClaw AI agents. It installs and documents a scientific reasoning stack that enables symbolic mathematics, numerical analysis, optimization, formal constraints, chemistry, physics, and probabilistic inference.

This repo includes:

- installation and removal scripts
- update tooling
- verification tooling
- capability metadata
- agent playbooks
- router hints
- wrapper contracts
- integration guidance
- smoke tests

## Included tools

- SymPy
- optlang
- pyneqsys
- pyodesys
- Lcapy
- SciPy
- RDKit
- Cantera
- PySCF
- SageMath
- OR-Tools
- Z3
- CVXPY
- PyMC

## Capability domains

- symbolic math
- scientific computing
- optimization
- constraint reasoning
- uncertainty-aware inference
- chemistry
- physics

## Quick install

```bash
git clone <repo-url> openclaw-scientific-reasoning
cd openclaw-scientific-reasoning
bash scripts/install.sh
bash scripts/verify.sh
```

## Quick update

```bash
cd openclaw-scientific-reasoning
bash scripts/update.sh
```

To refresh the lock file for reproducible installs:

```bash
bash scripts/update.sh refresh-lock
```

## Quick uninstall

```bash
bash scripts/uninstall.sh --mode unregister_only
```

Or for a dedicated environment:

```bash
bash scripts/uninstall.sh --mode full_remove
```

## What this repo is for

Use this capability pack when an OpenClaw agent needs:

* symbolic derivation
* exact algebra
* numerical simulation
* constrained optimization
* logic or satisfiability checks
* scientific computing
* chemistry or physics analysis
* uncertainty-aware inference from noisy evidence

Do not activate this stack for ordinary chat, generic writing, or loose brainstorming unless the problem has been structured enough to benefit from formal reasoning tools.

## Verification

Run:

```bash
bash scripts/verify.sh
```

This checks imports and basic runtime readiness.

## OpenClaw integration

This repo is designed to support:

* capability registration
* startup brief injection
* router hint registration
* wrapper contract reuse
* agent-facing playbooks

See:

* `docs/INTEGRATION-GUIDE.md`
* `docs/STARTUP-BRIEF-SNIPPET.md`
* `config/router-hints.json`

## Repo layout

```
openclaw-scientific-reasoning/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── VERSION
├── manifest.json
├── requirements.txt
├── requirements-dev.txt
├── Makefile
├── docs/
│   ├── PRODUCT-DESCRIPTION.md
│   ├── INTERNAL-AGENT-BRIEF.md
│   ├── INSTALL.md
│   ├── UNINSTALL.md
│   ├── INTEGRATION-GUIDE.md
│   ├── ROUTING-GUIDE.md
│   ├── STARTUP-BRIEF-SNIPPET.md
│   ├── TOOL-SELECTION-PLAYBOOK.md
│   └── TOOL-INVENTORY.md
├── capabilities/
│   ├── capability-registry-entry.json
│   ├── symbolic_math.json
│   ├── scientific_computing.json
│   ├── optimization.json
│   ├── constraint_reasoning.json
│   ├── uncertainty_inference.json
│   ├── chemistry.json
│   └── physics.json
├── playbooks/
│   ├── sympy-playbook.md
│   ├── sagemath-playbook.md
│   ├── scipy-playbook.md
│   ├── lcapy-playbook.md
│   ├── rdkit-playbook.md
│   ├── cantera-playbook.md
│   ├── pyscf-playbook.md
│   ├── ortools-playbook.md
│   ├── z3-playbook.md
│   ├── cvxpy-playbook.md
│   └── pymc-playbook.md
├── wrappers/
│   ├── README.md
│   ├── contracts/
│   │   ├── base-contract.json
│   │   ├── symbolic-contract.json
│   │   ├── optimization-contract.json
│   │   ├── constraint-contract.json
│   │   └── uncertainty-contract.json
│   └── templates/
│       ├── sympy-wrapper-template.py
│       ├── scipy-wrapper-template.py
│       ├── ortools-wrapper-template.py
│       ├── z3-wrapper-template.py
│       ├── cvxpy-wrapper-template.py
│       └── pymc-wrapper-template.py
├── scripts/
│   ├── install.sh
│   ├── uninstall.sh
│   ├── verify.sh
│   ├── update.sh
│   ├── register-capabilities.sh
│   └── unregister-capabilities.sh
├── examples/
│   ├── symbolic/
│   ├── optimization/
│   ├── constraints/
│   ├── uncertainty/
│   ├── chemistry/
│   ├── physics/
│   └── mixed/
├── tests/
│   ├── smoke/
│   ├── routing/
│   ├── wrappers/
│   └── integration/
└── config/
    ├── scientific-reasoning.env.example
    ├── agent-integration.example.json
    └── router-hints.json
```

## Version

Current version: `0.1.0`