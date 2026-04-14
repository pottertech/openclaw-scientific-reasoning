# Installation Guide

## Prerequisites

- Python 3.11 or higher
- pip or micromamba (optional, for environment isolation)
- Git (for cloning)

## Quick Install

```bash
git clone <repo-url> openclaw-scientific-reasoning
cd openclaw-scientific-reasoning
bash scripts/install.sh
```

## Install Options

### Standard pip install

```bash
bash scripts/install.sh
```

### With micromamba environment isolation

```bash
USE_MAMBA=1 ENV_NAME=sci-reasoning bash scripts/install.sh
```

### Custom Python binary

```bash
PYTHON_BIN=/path/to/python bash scripts/install.sh
```

## What the install script does

1. Verifies Python environment
2. Creates micromamba environment if requested
3. Upgrades pip, setuptools, wheel
4. Installs all scientific reasoning packages
5. Checks for SageMath
6. Registers capabilities
7. Runs verification

## Verification

After install, run:

```bash
bash scripts/verify.sh
```

## Post-install steps

1. Review `docs/INTEGRATION-GUIDE.md` for your specific agent integration
2. Inject `docs/STARTUP-BRIEF-SNIPPET.md` into your agent's startup context
3. Wire `config/router-hints.json` into your routing layer
4. Test with examples from `examples/` directory