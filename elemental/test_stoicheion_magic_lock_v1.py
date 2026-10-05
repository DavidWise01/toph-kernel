from stoicheion_magic_lock_v1 import (
    ESTABLISHED_MAGIC,
    PRIMITIVE,
    PRELOCK_ADDRESS,
    PREDICTED_CLOSURE,
    SEARCH_MIN,
    SEARCH_MAX,
    classify,
)

def test_established_sequence():
    assert ESTABLISHED_MAGIC == (2, 8, 20, 28, 50, 82, 126)

def test_primitive_literal():
    assert PRIMITIVE == "fib^bif / -3+4"

def test_address_to_closure():
    assert PRELOCK_ADDRESS == 168
    assert PREDICTED_CLOSURE == 169
    assert PRELOCK_ADDRESS + 1 == PREDICTED_CLOSURE

def test_no_other_predicted_locks_to_250():
    xs = [n for n in range(SEARCH_MIN, SEARCH_MAX + 1)
          if classify(n) == "stoicheion_predicted_lock"]
    assert xs == [169]

def test_gap_after_known_magic():
    assert all(classify(n) == "open" for n in range(127,168))
    assert classify(168) == "prelock"
    assert classify(169) == "stoicheion_predicted_lock"
    assert all(classify(n) == "open" for n in range(170,251))

if __name__ == "__main__":
    test_established_sequence()
    test_primitive_literal()
    test_address_to_closure()
    test_no_other_predicted_locks_to_250()
    test_gap_after_known_magic()
    print("0e / STOICHEION MAGIC LOCK TEST PASS")
