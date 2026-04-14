# PyMC Playbook

## Purpose
PyMC is a Bayesian statistical modeling library for probabilistic programming. Use it for posterior inference, parameter estimation, uncertainty quantification, and Bayesian machine learning.

## When to use PyMC

- Estimating parameters given noisy observations
- Computing credible intervals for quantities of interest
- Comparing hypotheses given evidence
- Predictive modeling with uncertainty
- Bayesian regression and hierarchical models

## When NOT to use PyMC

- Exact symbolic computation (use SymPy)
- Deterministic optimization without uncertainty (use CVXPY)
- Large-scale combinatorial optimization (use OR-Tools)

## Sample prompts

```
Given 8 heads in 10 coin flips, what's the posterior for bias p?
Find a 95% credible interval for the mean of Normal(0,1) given observations
Is treatment A better than treatment B given noisy outcomes?
```

## Common mistakes

1. **Not checking convergence**: Always check trace plots and R-hat statistics
2. **Using too few samples**: MCMC needs many samples for accurate posterior estimates
3. **Forgetting to check for numeric errors**: Some models have improper posteriors

## Fallback tool
SciPy (for simple frequentist statistics without full Bayesian inference)