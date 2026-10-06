from fractions import Fraction
from toroid5_commit_clock_v1 import *

def test_literal_cell():
    assert PHASES == (Fraction(0,1),Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5),Fraction(1,1))
    assert TRANSFER_QUANTUM == Fraction(1,5)

def test_one_cycle():
    c=Toroid5CommitClock()
    seq=[]
    for _ in range(5):
        seq.append(c.step())
    assert [r.phase for r in seq] == [Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5),Fraction(1,1)]
    assert [r.committed for r in seq] == [False,False,False,False,True]
    assert c.commits == 1
    w=c.wrap()
    assert w.phase == 0 and w.wrapped

def test_no_early_wrap():
    c=Toroid5CommitClock()
    c.step()
    try:
        c.wrap()
        assert False
    except RuntimeError:
        pass

def test_long_run_exactness():
    b=benchmark(10000)
    assert b["transfer_steps"] == 50000
    assert b["commits"] == 10000
    assert b["exact_phase_error"] == 0

def test_closure_gate():
    assert closure_gate(-1,0,1)
    assert not closure_gate(-1,0,0)
    assert not closure_gate(0,0,1)

if __name__=="__main__":
    test_literal_cell(); test_one_cycle(); test_no_early_wrap(); test_long_run_exactness(); test_closure_gate()
    print("0e / TOROID-5 DETERMINISTIC COMMIT CLOCK TEST PASS")
