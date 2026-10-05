from truth_state import TruthKernel, Evidence, Status

def run():
    k = TruthKernel()
    assert k.classify(Evidence("V0", .995, independent_support=2)) == Status.VERIFIED
    assert k.current_verified.claim_id == "V0"
    assert k.classify(Evidence("U1", .60)) == Status.QUARANTINED
    assert k.current_verified.claim_id == "V0"
    assert k.classify(Evidence("N1", .999, independent_support=4, aligns_with_current=False)) == Status.NON_ALIGNED
    assert k.current_verified.claim_id == "V0"
    assert not k.should_reverify()
    assert k.should_reverify(downstream_contradictions=3)
    assert k.classify(Evidence("V1", .997, independent_support=3)) == Status.VERIFIED
    assert (k.past_verified.claim_id, k.current_verified.claim_id) == ("V0", "V1")
    assert k.classify(Evidence("V2", .999, independent_support=4)) == Status.VERIFIED
    assert (k.past_verified.claim_id, k.current_verified.claim_id) == ("V1", "V2")
    assert [x.claim_id for x in k.history] == ["V0"]
    print("0e / TOPH FROZEN TRUTH-STATE PASS")

if __name__ == "__main__":
    run()
