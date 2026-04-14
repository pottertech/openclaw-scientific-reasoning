# Uninstallation Guide

## Unregister only (recommended)

Removes integration metadata but keeps packages installed:

```bash
bash scripts/uninstall.sh --mode unregister_only
```

## Full remove

Removes packages from the current environment. Use only if the environment is dedicated to OpenClaw-Scientific-Reasoning:

```bash
bash scripts/uninstall.sh --mode full_remove
```

## What uninstall does

### unregister_only mode

- Calls `scripts/unregister-capabilities.sh`
- Leaves pip packages installed
- Removes capability metadata from agent registry

### full_remove mode

- Calls `scripts/unregister-capabilities.sh`
- Uninstalls all packages via pip
- Does NOT remove SageMath (system-level install)

## Environment cleanup

If you created a dedicated micromamba environment:

```bash
micromamba remove -n openclaw-scientific-reasoning -y
```

## Post-uninstall

After uninstalling, remove or update:
- Startup brief snippet (remove from agent context)
- Router hints (remove from routing layer)
- Any capability registry entries