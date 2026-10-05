from stoicheion_250e_aligned_v1 import A,B,encode,glyph_value,band_address,shell_class

def test_carriers():
    assert glyph_value(A) == 10
    assert glyph_value(B) == 10
    assert encode(10) == A
    assert encode(20) == A+B

def test_all_250_values():
    assert all(glyph_value(encode(n)) == n for n in range(1,251))

def test_3x3_cubed_bands():
    assert band_address(1)["band"] == 1
    assert band_address(9)["band"] == 1
    assert band_address(10)["band"] == 2
    assert band_address(18)["band"] == 2
    assert band_address(19)["band"] == 3
    assert band_address(27)["band"] == 3
    assert band_address(28) == {"cycle":2,"band":1,"row":1,"col":1,"state":1}

def test_184_alignment():
    assert shell_class(184) == "AB_TRANSVERSAL_PLUS4"
    assert 184 % 20 == 4

if __name__ == "__main__":
    test_carriers()
    test_all_250_values()
    test_3x3_cubed_bands()
    test_184_alignment()
    print("0e / STOICHEION 250E TEST PASS")
