#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
FAIL=0

check_python_import() {
  local label="$1"
  local module="$2"

  if "${PYTHON_BIN}" - <<PY >/dev/null 2>&1
import ${module}
PY
  then
    echo "[PASS] ${label}"
  else
    echo "[FAIL] ${label}"
    FAIL=1
  fi
}

echo "==> Verifying OpenClaw-Scientific-Reasoning"

check_python_import "SymPy" "sympy"
check_python_import "optlang" "optlang"
check_python_import "pyneqsys" "pyneqsys"
check_python_import "pyodesys" "pyodesys"
check_python_import "Lcapy" "lcapy"
check_python_import "SciPy" "scipy"
check_python_import "RDKit" "rdkit"
check_python_import "Cantera" "cantera"
check_python_import "PySCF" "pyscf"
check_python_import "OR-Tools" "ortools"
check_python_import "Z3" "z3"
check_python_import "CVXPY" "cvxpy"
check_python_import "PyMC" "pymc"

if command -v sage >/dev/null 2>&1; then
  echo "[PASS] SageMath executable"
else
  echo "[WARN] SageMath executable not found"
fi

echo "==> Running tiny smoke checks"

"${PYTHON_BIN}" - <<'PY' || FAIL=1
import sympy as sp
x = sp.symbols('x')
assert sp.expand((x + 1) ** 2) == x**2 + 2*x + 1
print("SymPy smoke ok")
PY

"${PYTHON_BIN}" - <<'PY' || FAIL=1
import cvxpy as cp
x = cp.Variable()
prob = cp.Problem(cp.Minimize((x - 2)**2), [x >= 0])
prob.solve()
assert x.value is not None
print("CVXPY smoke ok")
PY

"${PYTHON_BIN}" - <<'PY' || FAIL=1
from z3 import Int, Solver
x = Int('x')
s = Solver()
s.add(x > 1, x < 5)
assert str(s.check()) == "sat"
print("Z3 smoke ok")
PY

if [[ "${FAIL}" -ne 0 ]]; then
  echo "==> Verification failed"
  exit 1
fi

echo "==> Verification passed"