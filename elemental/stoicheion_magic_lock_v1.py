"""STOICHEION nuclear-magic lock extension v1.

This module freezes the user's model-local lock invariant.

Established nuclear magic numbers (physics):
    2, 8, 20, 28, 50, 82, 126

STOICHEION primitive label:
    fib^bif / -3+4

Model-local extrapolation:
    168 = final open/pre-lock address
    169 = completed closure
    search domain = 1..250
    no other model-local closure is admitted in that domain

IMPORTANT:
The 169 closure is a STOICHEION prediction, not an established nuclear
magic number in standard nuclear physics.
"""

ESTABLISHED_MAGIC = (2, 8, 20, 28, 50, 82, 126)

PRIMITIVE = "fib^bif / -3+4"

SEARCH_MIN = 1
SEARCH_MAX = 250

PRELOCK_ADDRESS = 168
PREDICTED_CLOSURE = 169

MODEL_LOCKS = ESTABLISHED_MAGIC + (PREDICTED_CLOSURE,)


def classify(n: int) -> str:
    if not SEARCH_MIN <= n <= SEARCH_MAX:
        raise ValueError("outside frozen search domain 1..250")
    if n in ESTABLISHED_MAGIC:
        return "established_magic"
    if n == PRELOCK_ADDRESS:
        return "prelock"
    if n == PREDICTED_CLOSURE:
        return "stoicheion_predicted_lock"
    return "open"


def validate() -> bool:
    assert ESTABLISHED_MAGIC == (2, 8, 20, 28, 50, 82, 126)
    assert PRELOCK_ADDRESS + 1 == PREDICTED_CLOSURE
    assert SEARCH_MIN <= PREDICTED_CLOSURE <= SEARCH_MAX

    predicted = [
        n for n in range(SEARCH_MIN, SEARCH_MAX + 1)
        if classify(n) == "stoicheion_predicted_lock"
    ]
    assert predicted == [169]

    assert all(classify(n) == "open" for n in range(127, 168))
    assert all(classify(n) == "open" for n in range(170, 251))
    return True


if __name__ == "__main__":
    validate()
    print("0e / STOICHEION MAGIC LOCK v1 PASS")
    print("primitive:", PRIMITIVE)
    print("established:", ESTABLISHED_MAGIC)
    print("prelock:", PRELOCK_ADDRESS)
    print("closure:", PREDICTED_CLOSURE)
