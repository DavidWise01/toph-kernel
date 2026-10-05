# STOICHEION 250E — Aligned Elemental/Compound Register v1

**STATUS: FROZEN / IMMUTABLE / APPEND-ONLY**

## Primitive alignment

```
. = 1
| = 2

A = ..||..| = 10
B = ||..|.. = 10

A -> B -> A -> B ...   # transversal / switched carrier
```

Compound address lattice:

```
{{3x3}}^{{3}}

band 1 = 3x3 = compound class A
band 2 = 3x3 = compound class B
band 3 = 3x3 = compound class C

3 bands × 9 cells = 27 local elemental/compound states
```

After state 27, the next 27-state compound cycle begins. The band identity is
preserved; it is not flattened into a single 27-state scalar.

## Test result

```
250 addresses generated               PASS
glyph value == address for E001..E250 PASS
A carrier = 10                        PASS
B carrier = 10                        PASS
3×3×3 band addressing                 PASS
E184 class = AB_TRANSVERSAL_PLUS4     PASS
```

E184 was **not inserted as a target**. Under the A/B 20-unit phase pair:

```
184 = 9 × 20 + 4
```

so it lands naturally in the `20n+4` transversal class.

## Scientific boundary

```
E001..E118 = known chemical element identities
E119..E250 = STOICHEION model-local addresses only
```

The extension does not claim that chemistry currently recognizes elements
119–250.

## Register layout

The machine-readable full register is `STOICHEION_250E.csv`.
