"""STOICHEION / network vector cipher benchmark v1.

Literal user inputs:
    seed glyph: {{ . . | | . . | }} = 10
    centered kernel: -+505+-
    branch A: (x+2, y-3)
    branch B: (x-2, y+3)

We interpret u/d/l/r/mirror/inv/upside-down as the 8 unique square
(D4) view transforms. rev/backwards reverses branch/traversal order and
does not create a ninth geometric orientation.

No chemistry or nuclear magic number is fed into the generator.

Lock criterion for this network cipher:
    both opposed branches preserve the same squared vector norm under
    every external view; the bilateral forward/reverse lock address is
    norm2(A) * norm2(B).

This is a model-local network/cipher invariant, not nuclear physics.
"""

SEED = ". . | | . . |"
KERNEL = "-+505+-"
A = (2, -3)
B = (-2, 3)
LIMIT = 250

# 8 unique D4 transforms of the square.
TRANSFORMS = {
    "u":            (( 1, 0), ( 0, 1)),
    "d":            ((-1, 0), ( 0,-1)),
    "l":            (( 0,-1), ( 1, 0)),
    "r":            (( 0, 1), (-1, 0)),
    "mirror":       ((-1, 0), ( 0, 1)),
    "inv":          (( 1, 0), ( 0,-1)),
    "diag":         (( 0, 1), ( 1, 0)),
    "upside_down":  (( 0,-1), (-1, 0)),
}

ALIASES = {
    "rev": "reverse_traversal",
    "backwards": "reverse_traversal",
}

def glyph_value(seed: str) -> int:
    return sum(1 if c == "." else 2 if c == "|" else 0 for c in seed)

def mv(M, v):
    return (
        M[0][0]*v[0] + M[0][1]*v[1],
        M[1][0]*v[0] + M[1][1]*v[1],
    )

def norm2(v):
    return v[0]*v[0] + v[1]*v[1]

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1]

def all_views():
    out = {}
    for name,M in TRANSFORMS.items():
        a = mv(M,A)
        b = mv(M,B)
        out[name] = {
            "A": a,
            "B": b,
            "A_norm2": norm2(a),
            "B_norm2": norm2(b),
            "dot": dot(a,b),
        }
    return out

def bilateral_lock():
    views = all_views()
    norms_a = {v["A_norm2"] for v in views.values()}
    norms_b = {v["B_norm2"] for v in views.values()}
    if len(norms_a) != 1 or len(norms_b) != 1:
        return None
    return next(iter(norms_a)) * next(iter(norms_b))

def scan(limit=LIMIT):
    lock = bilateral_lock()
    return tuple(n for n in range(1, limit+1) if n == lock)

def validate():
    assert glyph_value(SEED) == 10
    assert B == (-A[0], -A[1])
    views = all_views()
    assert len(views) == 8
    assert {v["A_norm2"] for v in views.values()} == {13}
    assert {v["B_norm2"] for v in views.values()} == {13}
    assert {v["dot"] for v in views.values()} == {-13}
    assert bilateral_lock() == 169
    assert scan(250) == (169,)
    return True

if __name__ == "__main__":
    validate()
    print("seed_value:", glyph_value(SEED))
    for name,v in all_views().items():
        print(name, v)
    print("bilateral_lock:", bilateral_lock())
    print("scan_1_250:", scan())
    print("0e / NETWORK VECTOR CIPHER BLIND SCAN PASS")
