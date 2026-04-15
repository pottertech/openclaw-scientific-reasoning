# NetworkX Playbook

## Purpose

Use NetworkX for graph-native reasoning.

NetworkX is the right tool for:
- graph construction
- dependency analysis
- topology analysis
- shortest paths
- connectivity
- centrality
- node importance
- workflow graph analysis
- connected components

## Use NetworkX when

Choose NetworkX when the problem is really about nodes, edges, paths, dependencies, topology, or network structure.

Good fits:
- service dependency graphs
- workflow graphs
- process graphs
- relationship networks
- communication networks
- DAG inspection
- pathfinding
- bottleneck identification

## Do not use NetworkX when

Do not choose NetworkX first when:
- graph language is only metaphorical
- the real task is optimization of routes, assignments, or schedules
- the task is formal proof
- the task is symbolic algebra
- the task is uncertainty estimation
- the task is general writing or loose explanation

## Routing triggers

Typical signals:
- graph
- network
- dependency graph
- workflow graph
- shortest path
- connectivity
- centrality
- topology
- node importance
- connected components

## Output expectations

A NetworkX execution path should usually return:
- graph summary
- node count
- edge count
- connectivity results
- path results if applicable
- centrality or ranking results if applicable
- component analysis
- errors if graph structure is invalid

## Example prompts

1. Analyze this service dependency graph and find the critical nodes.

2. Find disconnected components in this workflow graph.

3. Compute the shortest path between these systems.

4. Determine which nodes are most central in this network.

5. Inspect this dependency graph for bottlenecks or fragile points.

## Common mistakes

1. Using NetworkX for route optimization
If the real goal is to optimize routes or assignments under constraints, use OR-Tools or Pyomo after the graph analysis step.

2. Using NetworkX for non-graph text
The problem should have actual graph structure or an implied graph representation.

3. Using NetworkX for proof or rule satisfiability
Use Lean for formal proof and Z3 for satisfiability or contradiction checks.

4. Confusing pathfinding with routing optimization
Shortest path is graph analysis.
Vehicle routing with constraints is optimization.

## Fallback path

- If the problem is really a routing or assignment optimization, fallback to OR-Tools.
- If the problem is a network flow or larger planning model, graph analysis may feed into Pyomo.
- If the problem is only about policy consistency, fallback to Z3.
- If the graph must support a formal proof claim, hand off to Lean after graph extraction if needed.

## Mixed-stage patterns

Common good pairings:
- graph_reasoning -> optimization_discrete
- graph_reasoning -> optimization_modeling

Examples:
- analyze dependency graph, then optimize resource placement
- compute network relationships, then optimize flow or capacity
- identify connected regions, then assign work by region

## Minimal decision rule

Use NetworkX when the question is:
"What does the graph structure tell us?"

Use OR-Tools or Pyomo when the question becomes:
"What is the best decision over that structure?"
