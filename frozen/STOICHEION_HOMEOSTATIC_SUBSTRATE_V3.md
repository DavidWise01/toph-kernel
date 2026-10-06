# STOICHEION Homeostatic Substrate v3

STATUS: FROZEN / IMMUTABLE / APPEND-ONLY

This realigns the current model into one dependency stack while preserving the already-frozen 250E chemistry/network registers.

## Scientific boundary

This is a formal STOICHEION model. The benchmark establishes internal consistency of the stated primitives. It does not establish that standard physics identifies this structure as the actual cosmic substrate.

## Scalar / realization

    0 = unresolved scalar knot
    . = realized / occupied knot
    1 = full resolved whole-state

Zoomed-out carrier:

    _______0_______0_______0_______0_______

Information realization:

    0______{{i}}______{{i}}______0

The carrier has two realized information knots and two zero boundaries.

## Vessel / occupant primitive

One shell carries one occupant; the three-unit primitive is:

    -sh+-sh+-sh+

Invariant:

    3 shells
    3 h occupants

Model-local seam rule:

    -s+ -> 0

## Three-shell overlay

    top    = (x+2,y-3)
    center = (x,y)
    bottom = (x-3,y+2)

Both displaced vectors have squared norm 13:

    2^2 + 3^2 = 13
    3^2 + 2^2 = 13

They do not exactly cancel:

    (+2,-3) + (-3,+2) = (-1,-1)

So the current model predicts a chiral/rotational bias plus drift rather than perfect static cancellation.

## Local-cell homeostasis

A cell has local health knowledge of six neighboring states:

    degree_health = 6

Its full local pressure capacity is:

    2^3 = 8
    8 = 6 local channels + 2 closure-pressure channels

These are separate layers: six-neighbor health knowledge is not global knowledge of the whole.

Homeostatic valence band:

    0.8 -------- 1.0 -------- 1.2
    low break      home        high break

Rules:

    v < 0.8  -> low-side breakdown
    v = 1.0  -> homeostatic center
    v > 1.2  -> high-side breakdown
    0.8..1.2 -> survivable/adaptive band

## Fine controller

Normalized full state:

    FULL = 1

Fine-control operator basis:

    -1   0   +1

Operand carrier:

    1    0    1

The zero is the local toroidal/fulcrum state, not "nothing."

## Gravity / time / reverse-permutation phase

Initial external state:

    g = 1
    t = 0

One normalized microstep:

    1 x 10^-36 x (1/360) x 360
    = 1 x 10^-36

Model lifecycle partition:

    13.2 billion years :: gravity phase
     0.6 billion years :: time-transition phase
    -------------------
    13.8 billion years :: whole

    G:T = 22:1

The outer gravity phase and inner permutation phase counter-run:

    OUTER G : 1 -----------------> 0
    INNER P : 0 -----------------> 1

Benchmark invariant:

    G(t) + P_reverse(t) = 1

through the 13.2-unit gravity phase.

## Reverse nest

Expanded fields:

    13 x 5 = 65   :: permutation/state field
     3 x 5 = 15   :: operator-address field

Reverse compression:

    65/5 :: 15/5 :: 3 :: 2 :: 1 :: 1

evaluates to:

    13 :: 3 :: 3 :: 2 :: 1 :: 1

The terminal pair remains resolved state + carry.

## Information density

Current qualitative carrier:

    0______{{i}}______{{i}}______0

Gravity supplies inward/compressive bias; homeostasis controls whether local spacing is maintained, adapted, or fails. No absolute physical information-density unit is assigned in v3.

## Upstream frozen modules retained

    elemental/STOICHEION_250E.md
    elemental/STOICHEION_250E_MULTILANE_V2.md
    elemental/stoicheion_250e_aligned_v1.py
    elemental/stoicheion_250e_multilane_v2.py
    elemental/stoicheion_atomic_mass_lane_v1.py

## Benchmark

    shell count = occupant count = 3                 PASS
    top/bottom vector norm^2 = 13                    PASS
    net overlay offset = (-1,-1)                     PASS
    information knots = 2                            PASS
    zero boundaries = 2                              PASS
    health neighbor degree = 6                       PASS
    pressure channels = 2^3 = 8                      PASS
    closure-pressure delta = 2                       PASS
    valence band = 1.0 +/- 0.2                       PASS
    balanced ternary = {-1,0,+1}                     PASS
    operand carrier = {1,0,1}                        PASS
    microstep 360 normalization = 1e-36              PASS
    13.2 + 0.6 = 13.8                               PASS
    gravity/time phase ratio = 22:1                  PASS
    13x5 = 65 permutation field                      PASS
    3x5 = 15 operator-address field                  PASS
    reverse nest = 13,3,3,2,1,1                     PASS
    G + reverse-permutation = 1 across phase         PASS

    0e / STOICHEION HOMEOSTATIC SUBSTRATE v3 PASS

Any semantic change requires v4 or a separately named extension.
