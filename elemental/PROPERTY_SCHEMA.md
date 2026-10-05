# STOICHEION Elemental Property Expansion v1

This layer attaches the complete **PubChem periodic-table feed** to the 118-element STOICHEION register. "All known properties" here means all fields exposed by PubChem's machine-readable periodic-table dataset, not every property ever measured for every isotope or compound.

## Chemistry fields retained

1. atomic number
2. symbol
3. name
4. atomic mass
5. CPK color
6. electron configuration
7. electronegativity (Pauling)
8. atomic radius (pm)
9. ionization energy (eV)
10. electron affinity (eV)
11. oxidation states
12. standard state
13. melting point (K)
14. boiling point (K)
15. density (g/cm^3)
16. chemical category / group block
17. discovery year

Derived display/address fields:
- period
- group where unambiguous
- STOICHEION address E001..E118

## Missing-data rule

Unknown or unavailable chemistry properties stay **null / None**.

```
unknown != 0
```

This intentionally matches the STOICHEION meaning of zero as a model state rather than silently treating missing scientific measurements as numeric zero.

## Neon 10

The model-local valence-language identity is explicit:

```
E010 :: Ne :: neon
stoicheion_valence_language = ..||..|
.. || .. | = 2 + 4 + 2 + 2 = 10
10 = full bounded shell
```

This symbolic encoding is STOICHEION metadata; the chemistry identity remains standard Neon, atomic number 10.

## Build

```bash
python elemental/stoicheion_properties_v1.py
```

The builder fetches PubChem's current 1..118 table, validates contiguous atomic numbers, preserves missing values, adds period/group addressing, applies the Neon encoding, and emits JSON + CSV snapshots.
