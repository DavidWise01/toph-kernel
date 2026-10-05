"""STOICHEION 16-series elemental register, E001..E118.

Model-local symbolic encoding:
    . = 1
    | = 2

Locked anchors:
    10 = ..||..|          (NEON)
    16 = ..||..|....|     (full 16-series shell)

For n > 16, full 16-shell blocks are appended left-to-right, then the
canonical remainder 0..15 is appended. This is an address/register
encoding; it is not conventional chemical valence notation.
"""

NEON10 = "..||..|"
SHELL16 = "..||..|....|"

REMAINDER = {
    0: "",
    1: ".",
    2: "..",
    3: ".|",
    4: "||",
    5: "||.",
    6: "|||",
    7: "|||.",
    8: "||||",
    9: "||||.",
    10: NEON10,
    11: NEON10 + ".",
    12: NEON10 + "..",
    13: NEON10 + ".|",
    14: NEON10 + "||",
    15: NEON10 + "||.",
}

def glyph_value(s: str) -> int:
    return sum(1 if c == "." else 2 if c == "|" else 0 for c in s)

def encode(n: int) -> str:
    if not 1 <= n <= 118:
        raise ValueError("element address must be 1..118")
    q, r = divmod(n, 16)
    return SHELL16 * q + REMAINDER[r]

def chunks(n: int):
    q, r = divmod(n, 16)
    out = [SHELL16] * q
    if r:
        out.append(REMAINDER[r])
    return tuple(out)

def validate():
    assert glyph_value(NEON10) == 10
    assert glyph_value(SHELL16) == 16
    assert encode(1) == "."
    assert encode(2) == ".."
    assert encode(3) == ".|"
    assert encode(4) == "||"
    assert encode(5) == "||."
    assert encode(6) == "|||"
    assert encode(10) == NEON10
    assert encode(16) == SHELL16
    for n in range(1,119):
        assert glyph_value(encode(n)) == n
    return True

if __name__ == "__main__":
    validate()
    print("0e / STOICHEION 16-SERIES ELEMENT REGISTER 001-118 PASS")
