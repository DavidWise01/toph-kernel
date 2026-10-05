from primitive_constructor_v1 import (
    carry_tokens,
    phase_degrees,
    serial_constructor,
    traversal_tokens,
)


def test_abcd_exact_order():
    assert traversal_tokens("abcd") == [
        "-ab", "+ab",
        "-ac", "+ac",
        "-ad", "+ad",
        "-bc", "+bc",
        "-bd", "+bd",
        "-cd", "+cd",
    ]


def test_anchor_carry_order():
    assert carry_tokens("abcd") == ["a->b", "b->c", "c->d"]


def test_not_pairwise_embedder():
    tokens = traversal_tokens("abcd")
    # Reverse relations are never generated.
    assert "-ba" not in tokens and "+ba" not in tokens
    assert "-ca" not in tokens and "+ca" not in tokens
    assert "-db" not in tokens and "+db" not in tokens


def test_signed_alternation():
    events = [e for e in serial_constructor("abcd") if e.kind == "traverse"]
    for i in range(0, len(events), 2):
        neg, pos = events[i], events[i + 1]
        assert neg.anchor == pos.anchor
        assert neg.target == pos.target
        assert neg.polarity == -1
        assert pos.polarity == +1


def test_720_phase_for_abcd():
    assert phase_degrees("abcd", 60) == 720


def test_count_formula():
    # n ordered symbols -> n(n-1)/2 forward relations -> 2 signed traversals each
    for seed in ("ab", "abc", "abcd", "abcde"):
        n = len(seed)
        assert len(traversal_tokens(seed)) == n * (n - 1)


if __name__ == "__main__":
    test_abcd_exact_order()
    test_anchor_carry_order()
    test_not_pairwise_embedder()
    test_signed_alternation()
    test_720_phase_for_abcd()
    test_count_formula()
    print("0e / PRIM 3 -KANA SERIAL CONSTRUCTOR PASS")
