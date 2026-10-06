"""STOICHEION Homeostatic Substrate v3 — frozen alignment kernel.

Consolidates the currently confirmed model-local primitives without rewriting
the already-frozen 250E chemistry/network registers.

Scientific boundary: these are STOICHEION model rules and internal-consistency
benchmarks, not claims that standard physics identifies this structure as the
physical cosmic substrate.
"""
from decimal import Decimal

SCALAR_ZERO = "0"
REALIZED_DOT = "."
FULL_STATE = Decimal("1")

SHELL_UNIT = "-sh+"
SHELL_TRIPLE = "-sh+-sh+-sh+"
SHELL_COUNT = 3
OCCUPANT = "h"
OCCUPANT_COUNT = 3

TOP_OFFSET = (2, -3)
CENTER_OFFSET = (0, 0)
BOTTOM_OFFSET = (-3, 2)

INFO_CARRIER = "0______{{i}}______{{i}}______0"
INFO_KNOT_COUNT = 2
ZERO_BOUNDARY_COUNT = 2

HEALTH_NEIGHBOR_DEGREE = 6
PRESSURE_CHANNELS = 2 ** 3
PRESSURE_CLOSURE_CHANNELS = PRESSURE_CHANNELS - HEALTH_NEIGHBOR_DEGREE

VALENCE_LOW = Decimal("0.8")
VALENCE_HOME = Decimal("1.0")
VALENCE_HIGH = Decimal("1.2")

BALANCED_TERNARY = (-1, 0, 1)
OPERAND_CARRIER = (1, 0, 1)

MICROSTEP = Decimal("1e-36") * (Decimal(1) / Decimal(360)) * Decimal(360)

GRAVITY_YEARS_BILLION = Decimal("13.2")
TIME_YEARS_BILLION = Decimal("0.6")
TOTAL_YEARS_BILLION = Decimal("13.8")

PERMUTATION_FIELD = 13 * 5
OPERATOR_ADDRESS_FIELD = 3 * 5
REVERSE_NEST = (
    Decimal(65) / Decimal(5),
    Decimal(15) / Decimal(5),
    Decimal(3), Decimal(2), Decimal(1), Decimal(1),
)

def norm2(v):
    x, y = v
    return x*x + y*y

def net_offset():
    return (
        TOP_OFFSET[0] + CENTER_OFFSET[0] + BOTTOM_OFFSET[0],
        TOP_OFFSET[1] + CENTER_OFFSET[1] + BOTTOM_OFFSET[1],
    )

def gravity_fraction(elapsed_billion_years):
    t = Decimal(elapsed_billion_years)
    if t <= 0:
        return Decimal(1)
    if t >= GRAVITY_YEARS_BILLION:
        return Decimal(0)
    return Decimal(1) - t / GRAVITY_YEARS_BILLION

def reverse_permutation_fraction(elapsed_billion_years):
    return Decimal(1) - gravity_fraction(elapsed_billion_years)

def valence_state(v):
    v = Decimal(v)
    if v < VALENCE_LOW:
        return "LOW_BREAKDOWN"
    if v > VALENCE_HIGH:
        return "HIGH_BREAKDOWN"
    if v == VALENCE_HOME:
        return "HOMEOSTATIC"
    return "ADAPTIVE"

def validate():
    assert SHELL_COUNT == OCCUPANT_COUNT == 3
    assert SHELL_TRIPLE.count("h") == 3

    assert norm2(TOP_OFFSET) == 13
    assert norm2(BOTTOM_OFFSET) == 13
    assert net_offset() == (-1, -1)

    assert INFO_CARRIER.count("{{i}}") == INFO_KNOT_COUNT
    assert INFO_CARRIER.startswith("0") and INFO_CARRIER.endswith("0")

    assert HEALTH_NEIGHBOR_DEGREE == 6
    assert PRESSURE_CHANNELS == 8
    assert PRESSURE_CLOSURE_CHANNELS == 2

    assert VALENCE_HOME - VALENCE_LOW == Decimal("0.2")
    assert VALENCE_HIGH - VALENCE_HOME == Decimal("0.2")

    assert BALANCED_TERNARY == (-1, 0, 1)
    assert OPERAND_CARRIER == (1, 0, 1)

    assert MICROSTEP == Decimal("1e-36")

    assert GRAVITY_YEARS_BILLION + TIME_YEARS_BILLION == TOTAL_YEARS_BILLION
    assert GRAVITY_YEARS_BILLION / TIME_YEARS_BILLION == Decimal(22)

    assert PERMUTATION_FIELD == 65
    assert OPERATOR_ADDRESS_FIELD == 15
    assert REVERSE_NEST == (
        Decimal(13), Decimal(3), Decimal(3),
        Decimal(2), Decimal(1), Decimal(1)
    )

    for x in ("0", "3.3", "6.6", "9.9", "13.2"):
        g = gravity_fraction(x)
        p = reverse_permutation_fraction(x)
        assert g + p == Decimal(1)

    return True

if __name__ == "__main__":
    validate()
    print("0e / STOICHEION HOMEOSTATIC SUBSTRATE v3 PASS")
