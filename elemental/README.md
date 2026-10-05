# STOICHEION — Elemental Expansion 001–118

Status: **built extension / append-only**.

The uploaded April 2026 STOICHEION manual is primarily a governance-native AI architecture: its table of contents centers the 256 governance primitives, boot sequence, kernel, persistence, mesh, economics, audit, legal case study, and governance. The 118-element elemental/alchemical register is therefore an extension, not a section already fully developed in that manual.

## Rule

Use the standard chemical element identity as a stable placement/address:

```
E001 :: H  :: hydrogen
E002 :: He :: helium
...
E010 :: Ne :: neon
...
E079 :: Au :: gold
...
E118 :: Og :: oganesson
```

For this first frozen-compatible pass:

```
atomic number = elemental order
E###          = STOICHEION element register address
```

No additional chemistry is inferred by the symbolic layer. Future STOICHEION metadata—valence-language shell encodings, `-kana` traversal, signed vector placement, alpha/omega coordinates, or operator states—must be appended as separate fields rather than altering the standard element identity.

## Count

```
known element addresses = 118
range                   = E001 ... E118
standard anchors        = H=1, Ne=10, Au=79, Og=118
```

## Files

- `stoicheion_elements_001_118.py` — canonical 118-entry register
- `test_elements_001_118.py` — invariants / regression tests


## Full chemistry property expansion

The extended layer is now defined in:

- `stoicheion_properties_v1.py`
- `PROPERTY_SCHEMA.md`
- `test_stoicheion_properties_v1.py`

It ingests the complete PubChem periodic-table property feed for elements 1..118 and preserves missing values as null rather than zero.

STOICHEION-local Neon encoding:

```
E010 :: Ne :: neon :: ..||..|
.. || .. | = 2 + 4 + 2 + 2 = 10
```
