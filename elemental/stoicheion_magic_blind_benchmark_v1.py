"""Blind STOICHEION / nuclear-magic benchmark v1.

Purpose:
    Test the literal available primitive pieces WITHOUT encoding 168/169
    or the nuclear magic sequence into the generator.

Available numeric definitions:
    fib: 0,1,1,2,3,5,8,13,... standard recurrence
    bif/rfib: reverse traversal of the same Fibonacci register
    -3+4: arithmetic value +1

Because '^' has not been given a unique executable operator definition,
we test the two least-assumptive bilateral readings:
    A) aligned forward x reverse multiplication
    B) all forward/reverse Fibonacci cross-products <= 250

Expected physics anchors are used ONLY after generation for comparison:
    2,8,20,28,50,82,126
"""

MAGIC = (2, 8, 20, 28, 50, 82, 126)
LIMIT = 250

def fibs(limit=LIMIT):
    xs = [0, 1]
    while xs[-1] <= limit:
        xs.append(xs[-1] + xs[-2])
    return tuple(x for x in xs if x <= limit)

def aligned_forward_reverse_products():
    f = fibs()
    r = tuple(reversed(f))
    return tuple(a*b for a,b in zip(f,r) if a*b <= LIMIT)

def cross_products():
    f = fibs()
    return tuple(sorted({
        a*b for a in f for b in f
        if a*b <= LIMIT
    }))

def arithmetic_offset():
    return -3 + 4

def benchmark():
    aligned = aligned_forward_reverse_products()
    crossed = cross_products()
    return {
        "fib": fibs(),
        "offset": arithmetic_offset(),
        "aligned_products": aligned,
        "cross_products": crossed,
        "magic_hits": tuple(m for m in MAGIC if m in crossed),
        "magic_misses": tuple(m for m in MAGIC if m not in crossed),
        "contains_168": 168 in crossed,
        "contains_169": 169 in crossed,
        "contains_170": 170 in crossed,
        "unique_169": crossed.count(169) == 1 and 168 not in crossed and 170 not in crossed,
    }

if __name__ == "__main__":
    r = benchmark()
    for k,v in r.items():
        print(f"{k}: {v}")
    assert r["offset"] == 1
    assert r["magic_hits"] == (2,8)
    assert r["magic_misses"] == (20,28,50,82,126)
    assert r["contains_168"]
    assert r["contains_169"]
    assert r["contains_170"]
    assert not r["unique_169"]
    print("RESULT: BLIND TEST DOES NOT ISOLATE 169 OR REPRODUCE MAGIC SEQUENCE")
