#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Registering OpenClaw-Scientific-Reasoning capability metadata"
echo "Source: ${ROOT_DIR}/capabilities/capability-registry-entry.json"
echo ""
echo "NOTE: Replace this script body with host-specific OpenClaw registry integration."
echo "This stub logs the intent to register, allowing operators to wire to their registry."