"""STOICHEION 250E independent-lane overlay v2.

Frozen architecture:
  E = electron/cloud
  P = proton
  N = neutron
  M = atomic mass

No lane is collapsed into another.
"""

LIMIT = 250

ELECTRON_IDEAL_CUMULATIVE = (2, 10, 28, 60, 110, 182)
PROTON_MAGIC_ESTABLISHED = (2, 8, 20, 28, 50, 82)
NEUTRON_MAGIC_ESTABLISHED = (2, 8, 20, 28, 50, 82, 126)
NEUTRON_MAGIC_PREDICTED = (184,)

KNOWN_ELEMENT_MAX = 118

def lane_flags(address: int) -> dict:
    if not 1 <= address <= LIMIT:
        raise ValueError(address)
    return {
        "electron_ideal_close": address in ELECTRON_IDEAL_CUMULATIVE,
        "proton_magic_established": address in PROTON_MAGIC_ESTABLISHED,
        "neutron_magic_established": address in NEUTRON_MAGIC_ESTABLISHED,
        "neutron_magic_predicted": address in NEUTRON_MAGIC_PREDICTED,
        "chemistry_status": "KNOWN_ELEMENT" if address <= KNOWN_ELEMENT_MAX else "MODEL_LOCAL_EXTENSION",
    }

def atomic_mass_status(address: int, atomic_mass):
    if address <= KNOWN_ELEMENT_MAX:
        return "SOURCE_VALUE_REQUIRED" if atomic_mass is None else "KNOWN_SOURCE_VALUE"
    if atomic_mass is None:
        return "UNASSIGNED_MODEL_EXTENSION"
    return "PREDICTED_VALUE_REQUIRES_PROVENANCE"

def nominal_neutron_count(z: int, isotope_mass_number: int) -> int:
    """Valid only for a specific isotope mass number A, not average atomic weight."""
    if isotope_mass_number < z:
        raise ValueError("A must be >= Z")
    return isotope_mass_number - z

def validate():
    assert lane_flags(2)["electron_ideal_close"]
    assert lane_flags(2)["proton_magic_established"]
    assert lane_flags(2)["neutron_magic_established"]

    assert lane_flags(126)["neutron_magic_established"]
    assert not lane_flags(126)["proton_magic_established"]

    assert lane_flags(184)["neutron_magic_predicted"]
    assert not lane_flags(184)["neutron_magic_established"]

    assert atomic_mass_status(118, 294.0) == "KNOWN_SOURCE_VALUE"
    assert atomic_mass_status(119, None) == "UNASSIGNED_MODEL_EXTENSION"
    assert nominal_neutron_count(82, 208) == 126
    return True

if __name__ == "__main__":
    validate()
    print("0e / STOICHEION 250E MULTI-LANE FREEZE v2 PASS")
