import pytest


def test_pyomo_import():
    """Test Pyomo can be imported."""
    import pyomo.environ as pe
    assert pe is not None


def test_networkx_import():
    """Test NetworkX can be imported."""
    import networkx as nx
    assert nx is not None


def test_pyomo_basic_model():
    """Test Pyomo can create a simple model."""
    import pyomo.environ as pe
    
    model = pe.ConcreteModel()
    model.x = pe.Var(domain=pe.NonNegativeReals)
    model.obj = pe.Objective(expr=model.x, sense=pe.minimize)
    model.con = pe.Constraint(expr=model.x >= 1)
    
    # Model created successfully
    assert model is not None
    assert len(list(model.component_data_objects(pe.Var))) == 1


def test_networkx_basic_graph():
    """Test NetworkX can create and analyze a simple graph."""
    import networkx as nx
    
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])
    
    # Basic graph properties
    assert G.number_of_nodes() == 4
    assert G.number_of_edges() == 4
    
    # Connectivity check
    assert nx.is_connected(G)


@pytest.mark.skip(reason="Lean is system dependency, not pip installable")
def test_lean_executable():
    """Test Lean executable is available.
    
    This test is skipped by default because Lean requires system-level installation.
    Run verification with: bash scripts/verify.sh
    """
    import subprocess
    result = subprocess.run(['lean', '--version'], capture_output=True, text=True)
    assert result.returncode == 0
