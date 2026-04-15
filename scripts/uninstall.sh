#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MODE="unregister_only"

if [[ "${1:-}" == "--mode" && -n "${2:-}" ]]; then
  MODE="${2}"
fi

echo "==> OpenClaw-Scientific-Reasoning uninstall"
echo "Mode: ${MODE}"

bash "${ROOT_DIR}/scripts/unregister-capabilities.sh" || true

if [[ "${MODE}" == "full_remove" ]]; then
  echo "==> Removing pip-installed packages from the current environment"
  "${PYTHON_BIN}" -m pip uninstall -y \
    sympy \
    optlang \
    pyneqsys \
    pyodesys \
    lcapy \
    scipy \
    rdkit \
    cantera \
    pyscf \
    ortools \
    z3-solver \
    cvxpy \
    pymc \
    pyomo \
    networkx || true

  echo "NOTE: SageMath is not removed by this script."
  echo "NOTE: Lean is not removed by this script (managed by elan)."
  echo "To remove Lean: elan self-uninstall"
fi

echo "==> Uninstall complete"
