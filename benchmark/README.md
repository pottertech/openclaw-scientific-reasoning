# Benchmark Results - OpenClaw-Scientific-Reasoning

**⚠️ NOTE: These are preliminary tool-execution results, NOT a true A/B comparison.**

## Current Results (14-task minimum viable pass)

| Category | LLM-only | Brodie | Delta |
|----------|----------|--------|-------|
| symbolic_math | 13.0 | 13.0 | +0.0 |
| constraint_reasoning | 13.0 | 12.0 | -1.0 |
| discrete_scheduling | 13.0 | 12.0 | -1.0 |
| optimization | 13.0 | 13.5 | +0.5 |
| graph_reasoning | 13.0 | 12.0 | -1.0 |
| uncertainty_inference | 13.0 | 13.0 | +0.0 |
| formal_reasoning | 13.0 | 13.0 | +0.0 |
| **OVERALL** | **13.0** | **12.6** | **-0.4** |

## Issues with Current Run

1. **LLM-only is simulated** - placeholder scores of 13, not actual LLM-only runs
2. **Code generation bugs** - e.g., C1 solver checks combined constraints instead of individual
3. **Scoring is heuristic** - not human evaluation

## How to Run Properly

### Step 1: Run LLM-only baseline

For each task, run with the LLM WITHOUT tool hints:

```
Task S1: "Differentiate and simplify: f(x) = (x^3 + 2x)^2"
[No tools, no routing hints - pure LLM response]
```

Record the response and score it.

### Step 2: Run Brodie with tools

For each task, run with full routing and tool access.

### Step 3: Compare and score

Use the `benchmark_results.csv` template and score both responses.

## Proper Scoring

Each response should be scored by a human on:
- **Correctness** (0-4): Is the answer mathematically correct?
- **Completeness** (0-4): Did it fully address the question?
- **Verifiability** (0-4): Can you verify the answer independently?
- **Hallucination** (0-4): Any unsupported claims? (4=grounded, 0=fabricated)
- **Execution** (0-4): Quality of any computed/solver output

## Files

- `tasks_14.csv` - 14 benchmark tasks (2 per category)
- `tasks_full_35.csv` - Full 35-task set
- `benchmark_results.csv` - Results template
- `run_benchmark.py` - Automated tool execution runner (for Mode B)

## Next Steps

1. Run actual LLM-only baselines for each task
2. Fix code generators in run_benchmark.py
3. Have human evaluators score responses
4. Compute proper deltas