"""Smoke tests for OpenClaw-Scientific-Reasoning imports."""

import pytest


def test_import_sympy():
    import sympy  # noqa: F401


def test_import_optlang():
    import optlang  # noqa: F401


def test_import_pyneqsys():
    import pyneqsys  # noqa: F401


def test_import_pyodesys():
    import pyodesys  # noqa: F401


def test_import_lcapy():
    import lcapy  # noqa: F401


def test_import_scipy():
    import scipy  # noqa: F401


def test_import_rdkit():
    import rdkit  # noqa: F401


def test_import_cantera():
    import cantera  # noqa: F401


def test_import_pyscf():
    import pyscf  # noqa: F401


def test_import_ortools():
    import ortools  # noqa: F401


def test_import_z3():
    import z3  # noqa: F401


def test_import_cvxpy():
    import cvxpy  # noqa: F401


def test_import_pymc():
    import pymc  # noqa: F401


if __name__ == "__main__":
    pytest.main([__file__, "-q"])