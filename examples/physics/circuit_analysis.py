# Physics: Circuit Analysis

## Example: Series RC circuit impedance

```python
from lcapy import Circuit

# Create series RC circuit with voltage source
cct = Circuit("""
V 1 0 {V_ac}
R 1 2 R
C 2 0 C
""")

# Get impedance at frequency omega
omega = 1000  # rad/s
Z = cct.impedance(omega)

print("Circuit: Series RC")
print(f"Impedance at omega={omega}:")
print(Z)
```

**Expected output:**
```
Circuit: Series RC
Impedance at omega=1000:
(1/R + j*C*omega)**(-1)
```

## Example: Low-pass RC filter transfer function

```python
from lcapy import Circuit

# Low-pass RC filter
cct = Circuit("""
Vi 1 0
R 1 2 R
C 2 0 C
Vo 2 0
""")

# Get transfer function Vo/Vi
H = cct.transfer(1, 0, 2, 0)
H_s = H(s='j*omega')

print("Low-pass RC filter transfer function:")
print(H_s)
```

**Note**: This example assumes Lcapy is installed. For numerical analysis, use SciPy.