#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
USE_MAMBA="${USE_MAMBA:-0}"
ENV_NAME="${ENV_NAME:-openclaw-scientific-reasoning}"

echo "==> OpenClaw-Scientific-Reasoning install"
echo "Root: ${ROOT_DIR}"

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "ERROR: Python not found: ${PYTHON_BIN}"
  exit 1
fi

if [[ "${USE_MAMBA}" == "1" ]]; then
  if ! command -v micromamba >/dev/null 2>&1; then
    echo "ERROR: USE_MAMBA=1 but micromamba is not installed"
    exit 1
  fi

  echo "==> Ensuring micromamba environment exists: ${ENV_NAME}"
  micromamba create -y -n "${ENV_NAME}" python=3.11 || true
  eval "$(micromamba shell hook --shell bash)"
  micromamba activate "${ENV_NAME}"
  PYTHON_BIN="python"
fi

echo "==> Upgrading pip tooling"
"${PYTHON_BIN}" -m pip install --upgrade pip setuptools wheel

echo "==> Installing scientific reasoning packages"
"${PYTHON_BIN}" -m pip install \
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
  networkx

echo "==> Installing Lean core (mandatory)"
bash "${ROOT_DIR}/scripts/install-lean-core.sh"

echo "==> Checking SageMath"
if command -v sage >/dev/null 2>&1; then
  echo "SageMath found on PATH"
else
  echo "WARNING: SageMath executable not found on PATH"
  echo "Install SageMath separately if this host requires Sage support"
fi

echo "==> Registering capabilities"
bash "${ROOT_DIR}/scripts/register-capabilities.sh" || true

echo "==> Running verification"
bash "${ROOT_DIR}/scripts/verify.sh"

echo "==> Install complete"
echo ""
echo "Next steps:"
echo " 1. Review docs/INTEGRATION-GUIDE.md"
echo " 2. Inject docs/STARTUP-BRIEF-SNIPPET.md into agent startup context"
echo " 3. Wire config/router-hints.json into your routing layer"