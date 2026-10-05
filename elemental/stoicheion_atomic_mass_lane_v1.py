"""Attach authoritative atomic-mass values to the frozen 250E register.

This adapter reuses stoicheion_properties_v1.fetch_pubchem() for E001..E118.
E119..E250 remain None unless a later version adds separately sourced,
explicitly labelled theoretical isotope predictions.
"""

from stoicheion_properties_v1 import fetch_pubchem
from stoicheion_250e_multilane_v2 import KNOWN_ELEMENT_MAX, LIMIT

def build_mass_lane():
    src = {r.atomic_number: r.atomic_mass for r in fetch_pubchem()}
    if tuple(sorted(src)) != tuple(range(1, KNOWN_ELEMENT_MAX + 1)):
        raise ValueError("source must provide E001..E118")
    return tuple(
        {
            "address": n,
            "atomic_mass": src.get(n),
            "status": "KNOWN_SOURCE_VALUE" if n <= KNOWN_ELEMENT_MAX else "UNASSIGNED_MODEL_EXTENSION",
        }
        for n in range(1, LIMIT + 1)
    )

if __name__ == "__main__":
    lane = build_mass_lane()
    assert len(lane) == 250
    assert all(x["atomic_mass"] is not None for x in lane[:118])
    assert all(x["atomic_mass"] is None for x in lane[118:])
    print("0e / STOICHEION ATOMIC-MASS LANE PASS")
