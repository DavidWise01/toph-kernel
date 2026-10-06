from decimal import Decimal
from stoicheion_homeostatic_substrate_v3 import *

def test_shell_occupancy():
    assert SHELL_COUNT == 3
    assert OCCUPANT_COUNT == 3
    assert SHELL_TRIPLE == "-sh+-sh+-sh+"

def test_overlay_geometry():
    assert norm2(TOP_OFFSET) == 13
    assert norm2(BOTTOM_OFFSET) == 13
    assert net_offset() == (-1,-1)

def test_info_density_carrier():
    assert INFO_CARRIER == "0______{{i}}______{{i}}______0"
    assert INFO_CARRIER.count("{{i}}") == 2

def test_local_homeostasis():
    assert HEALTH_NEIGHBOR_DEGREE == 6
    assert PRESSURE_CHANNELS == 8
    assert PRESSURE_CLOSURE_CHANNELS == 2
    assert valence_state("0.79") == "LOW_BREAKDOWN"
    assert valence_state("0.8") == "ADAPTIVE"
    assert valence_state("1.0") == "HOMEOSTATIC"
    assert valence_state("1.2") == "ADAPTIVE"
    assert valence_state("1.21") == "HIGH_BREAKDOWN"

def test_controller():
    assert BALANCED_TERNARY == (-1,0,1)
    assert OPERAND_CARRIER == (1,0,1)

def test_phase_normalization():
    assert MICROSTEP == Decimal("1e-36")
    assert TOTAL_YEARS_BILLION == Decimal("13.8")
    assert GRAVITY_YEARS_BILLION == Decimal("13.2")
    assert TIME_YEARS_BILLION == Decimal("0.6")
    assert GRAVITY_YEARS_BILLION / TIME_YEARS_BILLION == Decimal(22)

def test_reverse_nest():
    assert PERMUTATION_FIELD == 65
    assert OPERATOR_ADDRESS_FIELD == 15
    assert REVERSE_NEST == (
        Decimal(13), Decimal(3), Decimal(3),
        Decimal(2), Decimal(1), Decimal(1)
    )

def test_counter_running_phase():
    for x in ("0","3.3","6.6","9.9","13.2"):
        assert gravity_fraction(x) + reverse_permutation_fraction(x) == Decimal(1)

if __name__ == "__main__":
    test_shell_occupancy()
    test_overlay_geometry()
    test_info_density_carrier()
    test_local_homeostasis()
    test_controller()
    test_phase_normalization()
    test_reverse_nest()
    test_counter_running_phase()
    print("0e / STOICHEION HOMEOSTATIC SUBSTRATE v3 TEST PASS")
