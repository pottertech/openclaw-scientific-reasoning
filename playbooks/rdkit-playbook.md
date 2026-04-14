# RDKit Playbook

## Purpose
RDKit is a collection of cheminformatics and molecular modeling tools. Use it for molecular structure analysis, SMILES parsing, fingerprint generation, substructure searching, and molecular property calculation.

## When to use RDKit

- Parsing SMILES or mol files
- Computing molecular fingerprints (Morgan, MACCS, etc.)
- Substructure searching
- Molecular property calculation (MW, LogP, TPSA)
- Reaction SMARTS parsing
- 2D/3D structure generation

## When NOT to use RDKit

- Circuit analysis (use Lcapy)
- Thermodynamics or combustion (use Cantera)
- Quantum chemistry (use PySCF)

## Sample prompts

```
Parse the SMILES for caffeine ( Cncnc(C)C(=O)n)c1'
Compute the Morgan fingerprint for ethanol
Find all rotatable bonds in a molecule
```

## Common mistakes

1. **Not sanitizing molecules**: Call `AllChem.SanitizeMol()` after reading
2. **Using wrong fingerprint type**: Morgan fingerprints are usually best for similarity
3. **Forgetting to add hydrogen atoms**: Many inputs need `AddHs()` for accurate properties

## Fallback tool
Cantera (for reaction mechanisms and combustion)