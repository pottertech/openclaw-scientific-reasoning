#!/usr/bin/env python3
"""
Z3 wrapper template for OpenClaw-Scientific-Reasoning.
Implements the constraint-contract.json interface.
"""

import json
import sys

def invoke(operation: str, inputs: dict) -> dict:
    """
    Invoke Z3 for constraint reasoning and satisfiability.
    
    Args:
        operation: One of 'check', 'solve'
        inputs: Constraint definitions
    
    Returns:
        JSON-serializable result matching constraint-contract.json
    """
    from z3 import Solver, sat, unsat
    
    result = {
        "status": "unknown",
        "tool_name": "z3",
        "errors": [],
        "metadata": {"operation": operation},
        "result": {}
    }
    
    try:
        if operation in ("check", "solve"):
            s = Solver()
            
            # Add constraints from input
            constraints = inputs.get("constraints", [])
            for constraint in constraints:
                s.add(constraint)
            
            # Check satisfiability
            check_result = str(s.check())
            model = {}
            
            if check_result == "sat":
                m = s.model()
                for const in m:
                    model[str(const)] = str(m[const])
            
            result["result"] = {
                "satisfiable": check_result == "sat",
                "check_result": check_result,
                "model": model
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