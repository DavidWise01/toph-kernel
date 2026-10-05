from stoicheion_250e_multilane_v2 import *

def test_lanes_stay_separate():
    x = lane_flags(126)
    assert x["neutron_magic_established"] is True
    assert x["proton_magic_established"] is False
    assert x["electron_ideal_close"] is False

def test_184_is_prediction_only():
    x = lane_flags(184)
    assert x["neutron_magic_predicted"] is True
    assert x["neutron_magic_established"] is False

def test_mass_extension_is_not_fabricated():
    assert atomic_mass_status(118, 294.0) == "KNOWN_SOURCE_VALUE"
    assert atomic_mass_status(119, None) == "UNASSIGNED_MODEL_EXTENSION"

def test_isotope_relation():
    assert nominal_neutron_count(20, 40) == 20
    assert nominal_neutron_count(82, 208) == 126

if __name__ == "__main__":
    test_lanes_stay_separate()
    test_184_is_prediction_only()
    test_mass_extension_is_not_fabricated()
    test_isotope_relation()
    print("0e / STOICHEION 250E MULTI-LANE TEST PASS")
