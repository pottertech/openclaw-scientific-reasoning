#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MODE="${1:-safe}"

echo "==> OpenClaw-Scientific-Reasoning update"
echo "Root: ${ROOT_DIR}"
echo "Mode: ${MODE}"

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
 echo "ERROR: Python not found: ${PYTHON_BIN}"
 exit 1
fi

cd "${ROOT_DIR}"

echo "==> Upgrading pip tooling"
"${PYTHON_BIN}" -m pip install --upgrade pip setuptools wheel

echo "==> Updating runtime requirements"
"${PYTHON_BIN}" -m pip install --upgrade -r requirements.txt

if [[ -f "requirements-dev.txt" ]]; then
 echo "==> Updating dev requirements"
 "${PYTHON_BIN}" -m pip install --upgrade -r requirements-dev.txt
fi

if [[ "${MODE}" == "refresh-lock" ]]; then
 echo "==> Refreshing lock snapshot"
 "${PYTHON_BIN}" -m pip freeze > requirements-lock.txt
fi

echo "==> Re-registering capabilities"
bash scripts/register-capabilities.sh || true

echo "==> Running verification"
bash scripts/verify.sh

echo "==> Running smoke tests if pytest is available"
if "${PYTHON_BIN}" -m pytest --version >/dev/null 2>&1; then
 "${PYTHON_BIN}" -m pytest -q tests/smoke || true
else
 echo "pytest not available, skipping smoke tests"
fi

echo "==> Update complete"
