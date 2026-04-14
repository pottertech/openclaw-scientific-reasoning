# Uncertainty and Bayesian Inference

## Example: Conjugate normal posterior estimation

```python
import numpy as np

# Observed data (8 heads out of 10 flips)
data = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]  # 1 = heads, 0 = tails
n = len(data)
k = sum(data)

# Prior Beta(1, 1) (uniform)
alpha_prior, beta_prior = 1, 1

# Posterior Beta(alpha + k, beta + n - k)
alpha_post = alpha_prior + k
beta_post = beta_prior + (n - k)

# Posterior mean
posterior_mean = alpha_post / (alpha_post + beta_post)

print(f"Observations: {n} flips, {k} heads")
print(f"Prior: Beta({alpha_prior}, {beta_prior})")
print(f"Posterior: Beta({alpha_post}, {beta_post})")
print(f"Posterior mean: {posterior_mean:.4f}")
```

**Expected output:**
```
Observations: 10 flips, 8 heads
Prior: Beta(1, 1)
Posterior: Beta(9, 3)
Posterior mean: 0.7500
```