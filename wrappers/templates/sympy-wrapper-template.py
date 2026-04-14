#!/usr/bin/env python3
"""
SymPy wrapper template for OpenClaw-Scientific-Reasoning.
Implements the symbolic-contract.json interface.
"""

import json
import sys
from typing import Any

def invoke(operation: str, inputs: dict) -> dict:
    """
    Invoke SymPy for symbolic mathematics operations.
    
    Args:
        operation: One of 'simplify', 'solve', 'differentiate', 'integrate', 'factor'
        inputs: Operation-specific inputs
    
    Returns:
        JSON-serializable result matching symbolic-contract.json
    """
    import sympy as sp
    
    result = {
        "status": "unknown",
        "tool_name": "sympy",
        "errors": [],
        "metadata": {"operation": operation},
        "result": {}
    }
    
    try:
        if operation == "simplify":
            expr = sp.sympify(inputs["expression"])
            simplified = sp.simplify(expr)
            result["result"] = {
                "expression": str(simplified),
                "expression_type": "simplified",
                "simplified": simplified != expr
            }
            result["status"] = "complete"
            
        elif operation == "solve":
            expr = sp.sympify(inputs["expression"])
            solutions = sp.solve(expr, inputs.get("symbol", sp.Symbol("x")))
            result["result"] = {
                "expression": str(solutions),
                "expression_type": "solutions",
                "solution_count": len(solutions),
                "solutions": [str(s) for s in solutions]
            }
            result["status"] = "complete"
            
        elif operation == "differentiate":
            expr = sp.sympify(inputs["expression"])
            symbol = sp.Symbol(inputs["symbol"])
            derivative = sp.diff(expr, symbol)
            result["result"] = {
                "expression": str(derivative),
                "expression_type": "derivative"
            }
            result["status"] = "complete"
            
        elif operation == "integrate":
            expr = sp.sympify(inputs["expression"])
            symbol = sp.Symbol(inputs["symbol"])
            integral = sp.integrate(expr, symbol)
            result["result"] = {
                "expression": str(integral),
                "expression_type": "integral"
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