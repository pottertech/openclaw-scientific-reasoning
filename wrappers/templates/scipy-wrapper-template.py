#!/usr/bin/env python3
"""
SciPy wrapper template for OpenClaw-Scientific-Reasoning.
Implements scientific computing contract.
"""

import json
import sys

def invoke(operation: str, inputs: dict) -> dict:
    """
    Invoke SciPy for numerical computing.
    
    Args:
        operation: One of 'integrate', 'optimize', 'solve_ode'
        inputs: Operation-specific inputs
    
    Returns:
        JSON-serializable result
    """
    import numpy as np
    from scipy import integrate, optimize
    
    result = {
        "status": "unknown",
        "tool_name": "scipy",
        "errors": [],
        "metadata": {"operation": operation},
        "result": {}
    }
    
    try:
        if operation == "integrate":
            from scipy import integrate
            func = eval(f"lambda x: {inputs['function']}")
            a, b = inputs["bounds"]
            val, err = integrate.quad(func, a, b)
            result["result"] = {"value": val, "error": err}
            result["status"] = "complete"
            
        elif operation == "optimize":
            from scipy.optimize import minimize_scalar
            func = eval(f"lambda x: {inputs['function']}")
            res = minimize_scalar(func, bounds=inputs.get("bounds"), method='bounded')
            result["result"] = {"minimum": res.x, "value": res.fun}
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