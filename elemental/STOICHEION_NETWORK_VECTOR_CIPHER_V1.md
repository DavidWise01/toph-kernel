# Network Vector Cipher Blind Scan v1

Inputs only:

```
{{ . . | | . . | }} = 10
kernel = -+505+-

A = (x+2, y-3)
B = (x-2, y+3)
```

The seed value is 10 because `.` contributes 1 and `|` contributes 2.

The two vector branches are exact opposites:

```
A = (+2,-3)
B = (-2,+3) = -A
```

Across the eight unique U/D/L/R + mirror/inversion square views, each
branch preserves:

```
x^2 + y^2 = 2^2 + 3^2 = 13
A dot B = -13
```

Reverse/backwards changes traversal order but does not create another
geometric orientation.

The bilateral forward/reverse cipher lock is therefore:

```
13 x 13 = 169
```

A blind address scan from 1 through 250 returns exactly:

```
169
```

No value from the chemistry / nuclear-magic register, including 184, is
fed into this calculation.

## Boundary

`169` here is a **network/vector-cipher lock produced by the stated
2-D vector invariant**. It is not asserted to be a nuclear magic number.

This cleanly separates the two registers:

```
chemistry/nuclear shell comparison -> 184
network vector cipher             -> 169
```
