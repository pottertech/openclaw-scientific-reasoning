# Chemistry: Molecule Analysis

## Example: Parse SMILES and compute Morgan fingerprint

```python
from rdkit import Chem
from rdkit.Chem import AllChem

# Parse caffeine SMILES
smiles = "Cncnc(C)C(=O)n1cnc2c1c(=O)n(c(=O)n2C)C"
mol = Chem.MolFromSmiles(smiles)

# Add hydrogens
mol = Chem.AddHs(mol)

# Compute Morgan fingerprint
fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)

print(f"SMILES: {smiles}")
print(f"Atoms: {mol.GetNumAtoms()}")
print(f"Bonds: {mol.GetNumBonds()}")
print(f"MW: {AllChem.CalcExactMolWt(mol):.2f}")
print(f"LogP: {AllChem.CalcCrippenLogP(mol):.2f}")
```

**Expected output:**
```
SMILES: Cncnc(C)C(=O)n1cnc2c1c(=O)n(c(=O)n2C)C
Atoms: 24
Bonds: 25
MW: 194.19
LogP: 0.52
```