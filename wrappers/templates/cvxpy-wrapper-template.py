#!/usr/bin/env python3
"""
CVXPY wrapper template for OpenClaw-Scientific-Reasoning.
Implements the optimization-contract.json interface.
"""

import json
import sys

def invoke(operation: str, inputs: dict) -> dict:
    """
    Invoke CVXPY for convex optimization.
    
    Args:
        operation: One of 'solve'
        inputs: Problem definition (objective, constraints)
    
    Returns:
        JSON-serializable result matching optimization-contract.json
    """
    import cvxpy as cp
    
    result = {
        "status": "unknown",
        "tool_name": "cvxpy",
        "errors": [],
        "metadata": {},
        "result": {}
    }
    
    try:
        if operation == "solve":
            # Parse variables
            variables = {}
            for var_name in inputs.get("variable_names", []):
                variables[var_name] = cp.Variable()
            
            # Parse objective
            objective_expr = inputs["objective"]
            if inputs.get("objective_type") == "minimize":
                objective = cp.Minimize(objective_expr)
            else:
                objective = cp.Maximize(objective_expr)
            
            # Parse constraints
            constraints = inputs.get("constraints", [])
            
            # Form and solve problem
            problem = cp.Problem(objective, constraints)
            problem.solve(solver=inputs.get("solver", cp.ECOS))
            
            optimal_value = problem.value if problem.value is not None else float('inf')
            optimal_solution = {k: v.value for k, v in variables.items()}
            
            result["result"] = {
                "optimal_value": optimal_value,
                "optimal_solution": optimal_solution,
                "solver_status": str(problem.status),
                "solve_time_ms": 0
            }
            result["status"] = "complete"
            
        else:
            result["errors"].append(f"Unknown operation: {operation}")
            result["status"] = "failed"
            
    except Exception as e:
        result["errors"].append(str(e))
        result["status"] = "failed"
    
    return result


if __name__ == "__main__":
    data = json.load(sys.stdin)
    output = invoke(data["operation"], data["inputs"])
    print(json.dumps(output, indent=2))