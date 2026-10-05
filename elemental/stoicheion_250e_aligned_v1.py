"""STOICHEION 250E aligned register v1 — FROZEN / APPEND-ONLY.

Model-local rules:
  . = 1
  | = 2
  A = '..||..|' = 10
  B = '||..|..' = 10
  A/B alternate by completed 10-unit carrier blocks.
  {{3x3}}^{{3}} = 27 local states per compound cycle:
      3 bands × 9 cells, each band a distinct compound class.

E001..E118 preserve the known chemical-element identities.
E119..E250 are STOICHEION model-local addresses only, NOT claims of known
chemical elements.

184 is not injected as a lock. It falls into the AB_TRANSVERSAL_PLUS4
class because 184 mod 20 = 4.
"""

A = "..||..|"
B = "||..|.."
LIMIT = 250

REMAINDER = {
    0:"", 1:".", 2:"..", 3:".|", 4:"||",
    5:"||.", 6:"|||", 7:"|||.", 8:"||||", 9:"||||."
}

def glyph_value(s: str) -> int:
    return sum(1 if c=="." else 2 if c=="|" else 0 for c in s)

def encode(n: int) -> str:
    if not 1 <= n <= LIMIT:
        raise ValueError(n)
    q, r = divmod(n, 10)
    blocks = [A if i % 2 == 0 else B for i in range(q)]
    return "".join(blocks) + REMAINDER[r]

def band_address(n: int):
    z = n - 1
    cycle, state0 = divmod(z, 27)
    band0, cell0 = divmod(state0, 9)
    row0, col0 = divmod(cell0, 3)
    return {
        "cycle": cycle + 1,
        "band": band0 + 1,
        "row": row0 + 1,
        "col": col0 + 1,
        "state": state0 + 1,
    }

def shell_class(n: int) -> str:
    m = n % 20
    if m == 0:  return "AB_PHASE_CLOSE"
    if m == 4:  return "AB_TRANSVERSAL_PLUS4"
    if m == 10: return "A_HALF_PHASE"
    return "OPEN"

def validate():
    assert glyph_value(A) == 10
    assert glyph_value(B) == 10
    assert all(glyph_value(encode(n)) == n for n in range(1,251))
    assert band_address(1) == {"cycle":1,"band":1,"row":1,"col":1,"state":1}
    assert band_address(27)["state"] == 27
    assert band_address(28) == {"cycle":2,"band":1,"row":1,"col":1,"state":1}
    assert shell_class(184) == "AB_TRANSVERSAL_PLUS4"
    assert encode(10) == A
    assert encode(20) == A+B
    return True

if __name__ == "__main__":
    validate()
    print("0e / STOICHEION 250E ALIGNED REGISTER v1 PASS")
