#!/usr/bin/env python3
"""
OR-Tools wrapper template for OpenClaw-Scientific-Reasoning.
Implements the optimization-contract.json interface.
"""

import json
import sys

def invoke(operation: str, inputs: dict) -> dict:
    """
    Invoke OR-Tools for combinatorial optimization.
    
    Args:
        operation: One of 'solve_cp', 'solve_routing', 'solve_sat'
        inputs: Problem definition
    
    Returns:
        JSON-serializable result matching optimization-contract.json
    """
    result = {
        "status": "unknown",
        "tool_name": "ortools",
        "errors": [],
        "metadata": {"operation": operation},
        "result": {}
    }
    
    try:
        if operation == "solve_cp":
            from ortools.sat.python import cp_model
            
            model = cp_model.CpModel()
            
            # Create variables
            variables = {}
            for var_info in inputs.get("variables", []):
                name = var_info["name"]
                lb = var_info.get("lb", 0)
                ub = var_info.get("ub", 1000)
                if var_info.get("integer", True):
                    variables[name] = model.NewIntVar(lb, ub, name)
                else:
                    variables[name] = model.NewIntVar(lb, ub, name)
            
            # Add constraints
            for constraint in inputs.get("constraints", []):
                if constraint["type"] == "linear":
                    expr = sum(
                        variables[v["var"]] * v["coeff"]
                        for v in constraint["vars"]
                    )
                    model.Add(expr <= constraint.get("ub", 1000))
                    model.Add(expr >= constraint.get("lb", 0))
            
            # Set objective
            objective_vars = inputs.get("objective_vars", [])
            model.Minimize(sum(variables[v["var"]] * v["coeff"] for v in objective_vars))
            
            # Solve
            solver = cp_model.CpSolver()
            status = solver.Solve(model)
            
            solution = {k: solver.Value(v) for k, v in variables.items()}
            
            result["result"] = {
                "optimal_value": solver.ObjectiveValue(),
                "optimal_solution": solution,
                "solver_status": "optimal" if status == 2 else "unknown",
                "solve_time_ms": solver.WallTime()
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