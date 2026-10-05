from stoicheion_valence_register_v2 import encode, glyph_value, SHELL16, NEON10

def test_locked_anchors():
    assert encode(1) == "."
    assert encode(2) == ".."
    assert encode(3) == ".|"
    assert encode(4) == "||"
    assert encode(5) == "||."
    assert encode(6) == "|||"
    assert encode(10) == "..||..|"
    assert encode(16) == "..||..|....|"

def test_every_element_exact_value():
    for n in range(1,119):
        assert glyph_value(encode(n)) == n

def test_series_of_16():
    for n in range(16,119,16):
        assert encode(n) == SHELL16 * (n//16)

def test_neon_is_ten():
    assert glyph_value(NEON10) == 10

def test_oganesson_118():
    # 118 = 7*16 + 6
    assert encode(118) == SHELL16 * 7 + "|||"
    assert glyph_value(encode(118)) == 118

if __name__ == "__main__":
    test_locked_anchors()
    test_every_element_exact_value()
    test_series_of_16()
    test_neon_is_ten()
    test_oganesson_118()
    print("0e / STOICHEION 16-SERIES REGISTER PASS")
