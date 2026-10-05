# STOICHEION cyclic dot/bar scan 1..250

This benchmark uses the latest carrier interpretation:

```
. = 1
| = 2

base = ..||..| = 10
next = ||..|..     # left rotation by two glyph slots
then switch direction
```

Because rotating a glyph string does not change its scalar value, every
seven-glyph carrier state remains worth 10.

For address n:

```
n = 10q + r

representation =
q rotated 10-unit carriers
+
a canonical remainder r
```

The scan checks 184 as a held-out known shell candidate and then maps every
address through 250. It reports structural coincidences only; it does not
claim those are physical shell closures.
