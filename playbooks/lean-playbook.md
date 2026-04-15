# Lean Playbook

## Purpose

Use Lean for formal reasoning and machine-checked proof.

Lean is the right tool for:
- formal proof
- theorem proving
- invariant verification
- correctness proofs
- formalization of logical claims
- machine-checked reasoning
- safety and soundness proofs

## Use Lean when

Choose Lean when the user explicitly wants proof-grade correctness, not just a plausible explanation.

Good fits:
- prove this invariant
- verify this safety property
- formalize this claim
- produce a machine-checked proof
- prove an algorithm preserves a property
- prove a logical statement always holds

## Do not use Lean when

Do not choose Lean first when:
- the user only wants a quick consistency check
- the task is ordinary symbolic manipulation
- the task is scheduling or routing
- the task is optimization
- the task is uncertainty inference
- the task is casual explanation

## Routing triggers

Typical signals:
- prove
- formal proof
- theorem
- invariant
- formalize
- machine checked
- verified correctness
- proof assistant
- prove formally
- verify formally
- correctness proof
- safety proof

## Output expectations

A Lean execution path should usually return:
- proof goal summary
- formal statement summary
- proof status
- theorem or lemma names if created
- verification result
- errors if proof fails or the statement is malformed
- notes on assumptions or missing formal definitions

## Example prompts

1. Prove this invariant formally.

2. Formalize this safety claim and verify it.

3. Produce a machine-checked proof that this algorithm preserves the stated property.

4. Verify that this transition system always preserves the safety invariant.

5. Formalize these logical assumptions and prove the target claim.

## Common mistakes

1. Using Lean for quick satisfiability checks
Use Z3 when the main question is:
"Can these rules all hold together?"

2. Using Lean for ordinary algebra or calculus
Use SymPy or SageMath for symbolic derivation.

3. Using Lean for optimization
Use OR-Tools, CVXPY, or Pyomo depending on the optimization type.

4. Using Lean without a formal statement
Lean needs a claim, property, theorem, or invariant stated clearly enough to formalize.

## Fallback path

- If the task is really satisfiability or contradiction detection, fallback to Z3.
- If the task is exact symbolic derivation, fallback to SymPy or SageMath.
- If the task is just an informal explanation, fallback to general reasoning.
- Do not silently fall back from formal proof to approximate reasoning when proof-grade output was explicitly requested.

## Mixed-stage patterns

Common good pairings:
- symbolic_math -> formal_reasoning
- formal_reasoning -> optimization_convex
- formal_reasoning -> optimization_modeling

Examples:
- derive a property symbolically, then prove it formally
- formalize a safety invariant, then optimize inside that verified structure
- prove that a rule system preserves a required property, then solve the resulting constrained optimization

## Lean vs Z3

Use Lean when the question is:
"Prove this formally."

Use Z3 when the question is:
"Check whether these rules are satisfiable or contradictory."

That distinction matters.

## Minimal decision rule

Use Lean when the result must be:
- formal
- machine checked
- proof-grade
- correctness-oriented

If the user only needs:
- feasibility
- contradiction detection
- quick symbolic reasoning
- optimization
then Lean is usually not the first tool.
