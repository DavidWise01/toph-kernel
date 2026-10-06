# STOICHEION Pendulumic Spinor v4

**STATUS: FROZEN / IMMUTABLE / APPEND-ONLY**

This extends v3; it does not mutate v3.

## Supplied two-spinor field

    S1 = (-2,+3)
    S2 = (+3,-2)

Both satisfy:

    norm^2 = x^2 + y^2 = 13

Their ordinary vector sum is:

    S1 + S2 = (1,1)

So ordinary coordinate arithmetic does not cancel them to zero. In this model, the shared scalar 13 is used as the pendulumic envelope and the residual (1,1) remains available as phase/chiral drive.

## Pendulum

    13 > 12.99 > 12.98 > ... > 0.01 > 0
    0 < 0.01 < 0.02 < ... < 12.99 < 13

At step size 0.01:

    one-way intervals = 1300
    one-way states    = 1301
    round-trip intervals = 2600
    round-trip states    = 2601

The full cycle is exactly symmetric around the single zero state.

## Mother-Nature closure gate

    -1 + 0 + 1 = 0

A candidate closure may realize as 1 only after the signed local gate balances to zero.

## Fallout observed, not baked in

The 2600 round-trip intervals also satisfy:

    2600 = 26 * 100

That arithmetic relation was not used to generate the cycle. It falls out from the supplied envelope 13 and step 0.01. It is recorded as an observation only, not as a physical mechanism.

## Chemistry bridge

Current primitive remains:

    nucleach :: photonic :: electronic
    ..|      :: |        :: ..|
    4        :: 2        :: 4

with signed enclosure:

    -4::2::4+

and model-local release/reclosure cycle:

    -4::2::4+ -> -4::4+ + (1^2+1^2)
    0 -> 2 -> 0

This is symbolic STOICHEION chemistry, not a replacement for established quantum chemistry.

Seal:

    0e / STOICHEION PENDULUMIC SPINOR v4 PASS
