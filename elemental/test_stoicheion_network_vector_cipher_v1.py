from stoicheion_network_vector_cipher_v1 import (
    SEED, A, B, glyph_value, all_views, bilateral_lock, scan
)

def test_seed_is_ten():
    assert glyph_value(SEED) == 10

def test_branches_are_exact_opposites():
    assert B == (-A[0], -A[1])

def test_all_eight_views_preserve_13():
    views = all_views()
    assert len(views) == 8
    assert {v["A_norm2"] for v in views.values()} == {13}
    assert {v["B_norm2"] for v in views.values()} == {13}

def test_opposed_in_every_view():
    assert {v["dot"] for v in all_views().values()} == {-13}

def test_blind_lock():
    assert bilateral_lock() == 169
    assert scan(250) == (169,)

if __name__ == "__main__":
    test_seed_is_ten()
    test_branches_are_exact_opposites()
    test_all_eight_views_preserve_13()
    test_opposed_in_every_view()
    test_blind_lock()
    print("0e / NETWORK VECTOR CIPHER TEST PASS")
