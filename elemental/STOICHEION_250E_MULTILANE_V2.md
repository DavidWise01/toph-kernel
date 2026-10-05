# STOICHEION 250E Multi-Lane Freeze v2

**STATUS: FROZEN / IMMUTABLE / APPEND-ONLY**

This freezes the current architecture as independent lanes. No lane is
collapsed into another.

```
ADDRESS / Z
├── E :: electron / cloud lane
├── P :: proton lane
├── N :: neutron lane
└── M :: atomic-mass lane
```

## Shared STOICHEION carrier

```
. = 1
| = 2

A = ..||..| = 10
B = ||..|.. = 10

A -> B -> A -> B ...
AB = 20
```

## Compound lattice

```
{{3x3}}^{{3}}

band 1 = 3x3
band 2 = 3x3
band 3 = 3x3
3 bands x 9 cells = 27 local states
```

Each band remains a distinct compound class.

## Lane E — electron/cloud shell overlay

Ideal principal-shell cumulative capacities used as the abstract overlay:

```
2, 10, 28, 60, 110, 182
(next = 280, outside 250E)
```

This lane is an ideal 2n^2 capacity overlay. Actual neutral-atom electron
configurations also depend on subshell ordering and are stored separately
when available.

## Lane P — proton shell overlay

Established nuclear magic anchors:

```
2, 8, 20, 28, 50, 82
```

Superheavy proton closures are model-dependent. Candidate values must be
stored as predictions with provenance rather than promoted to established
locks.

## Lane N — neutron shell overlay

Established nuclear magic anchors:

```
2, 8, 20, 28, 50, 82, 126
```

`184` is carried as a predicted major neutron-shell candidate, not an
experimentally established magic number.

Under the STOICHEION carrier:

```
184 = 9(AB) + ||
    = 9(20) + 4
```

Thus E184 is in the `AB_TRANSVERSAL_PLUS4` class without inserting 184
into the cipher generator.

## Lane M — atomic mass / isotope load

Atomic mass is a separate measurement lane.

For E001..E118:

```
M = source atomic mass value
```

The mass lane MUST NOT be substituted for Z, electron count, proton count,
or a definite neutron count.

For a specific isotope only:

```
A = Z + N
N = A - Z
```

For a natural element's standard atomic weight, the value is generally an
isotopic abundance-weighted average and therefore is not itself one
integer nucleus.

For E119..E250:

```
M = null
```

unless a separately sourced theoretical/isotopic prediction is explicitly
attached. Model-local E addresses are not assigned fabricated atomic
weights.

## Scientific boundary

```
E001..E118 = known chemical-element identities
E119..E250 = STOICHEION model-local addresses

E/P/N/M = separate lanes
unknown != 0
prediction != established
```

Any semantic change requires v3 or later.
