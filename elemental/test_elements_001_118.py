from stoicheion_elements_001_118 import ELEMENTS, BY_Z, BY_SYMBOL

def test_count():
    assert len(ELEMENTS) == 118

def test_contiguous_atomic_numbers():
    assert [e.atomic_number for e in ELEMENTS] == list(range(1, 119))

def test_unique_symbols():
    assert len(BY_SYMBOL) == 118

def test_register_addresses():
    assert ELEMENTS[0].register == "E001"
    assert ELEMENTS[-1].register == "E118"

def test_anchor_elements():
    assert BY_Z[1].symbol == "H"
    assert BY_Z[10].symbol == "Ne"
    assert BY_Z[79].symbol == "Au"
    assert BY_Z[118].symbol == "Og"

def test_stoicheion_slot_matches_atomic_order():
    assert all(e.stoicheion_slot == e.atomic_number for e in ELEMENTS)

if __name__ == "__main__":
    test_count()
    test_contiguous_atomic_numbers()
    test_unique_symbols()
    test_register_addresses()
    test_anchor_elements()
    test_stoicheion_slot_matches_atomic_order()
    print("0e / STOICHEION ELEMENTAL EXPANSION 001-118 PASS")
