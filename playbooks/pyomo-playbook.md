# Pyomo Playbook

## Purpose

Use Pyomo for broader optimization modeling when the problem is larger, more structured, or less cleanly convex than a typical CVXPY problem.

Pyomo is the right tool for:
- mixed-integer optimization
- nonlinear optimization
- production planning
- supply planning
- capacity planning
- operations research models
- structured industrial optimization

## Use Pyomo when

Choose Pyomo when the problem has one or more of these traits:
- integer or binary decision variables
- mixed continuous and discrete decisions
- larger planning model structure
- multi-part operational constraints
- industrial optimization language such as production, plants, warehouses, shifts, capacity, or demand
- model-building needs that go beyond a simple objective and a few convex constraints

## Do not use Pyomo when

Do not choose Pyomo first when:
- the problem is a clean convex optimization that CVXPY can handle directly
- the task is scheduling, routing, packing, or assignment that OR-Tools handles better
- the task is symbolic derivation
- the task is formal proof
- the task is satisfiability or contradiction checking
- the task is uncertainty estimation

## Routing triggers

Typical signals:
- mixed integer
- integer programming
- nonlinear optimization
- production planning
- capacity planning
- supply planning
- operations research
- planning model
- resource allocation model

## Output expectations

A Pyomo execution path should usually return:
- model summary
- decision variables
- objective definition
- solver status
- optimal or feasible solution if found
- objective value
- constraint summary
- errors or infeasibility notes

## Example prompts

1. Build a production planning model with capacity and demand constraints.

2. Solve a mixed-integer resource allocation problem with binary decision variables.

3. Optimize a supply plan across plants and warehouses with capacity limits.

4. Minimize operating cost for a multi-stage process with integer choices.

5. Build an operations research model for staffing and throughput.

## Common mistakes

1. Using Pyomo for a small convex problem
Use CVXPY instead when the problem is a clean convex optimization.

2. Using Pyomo for pure scheduling with hard discrete assignment structure
Use OR-Tools when the problem is mainly scheduling, routing, packing, or assignment.

3. Sending informal business text with no actual model
The task should contain enough structure to define:
- variables
- objective
- constraints

4. Treating Pyomo like a proof tool
Pyomo optimizes. It does not prove correctness in the Lean sense or satisfiability in the Z3 sense.

## Fallback path

- If the problem is really convex and continuous, fallback to CVXPY.
- If the problem is really discrete scheduling or routing, fallback to OR-Tools.
- If the problem first needs symbolic derivation, use SymPy or SageMath before Pyomo.
- If the problem first needs consistency checking, use Z3 before Pyomo.

## Mixed-stage patterns

Common good pairings:
- symbolic_math -> optimization_modeling
- constraint_reasoning -> optimization_modeling
- graph_reasoning -> optimization_modeling

Examples:
- derive equations, then build the optimization model
- verify rules are consistent, then optimize the plan
- analyze a network graph, then optimize capacity or flow

## Minimal decision rule

Use Pyomo when the question is:
"Build or solve a larger structured optimization model."

Use CVXPY when the question is:
"Solve a clean convex optimization."

Use OR-Tools when the question is:
"Find the best discrete schedule or assignment."
