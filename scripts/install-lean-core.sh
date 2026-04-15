#!/usr/bin/env bash
set -euo pipefail

echo "==> Installing Lean core dependency"

if command -v lean >/dev/null 2>&1; then
    echo "Lean already available"
    exit 0
fi

if command -v elan >/dev/null 2>&1; then
    echo "elan found, installing Lean toolchain"
    elan toolchain install stable
    exit 0
fi

echo "ERROR: Lean is mandatory for OpenClaw-Scientific-Reasoning but was not found."
echo "Install elan and Lean, then rerun scripts/install.sh"
exit 1
