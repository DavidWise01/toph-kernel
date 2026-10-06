"""TOROID-5 deterministic commit clock.

Model-local purpose: five exact transfer intervals carry an unresolved 0
through internal phases and realize a commit only at the fifth transfer.
The closure witness 1 is identified with the next cycle origin 0.

Scientific boundary: this is a finite-state/control abstraction, not a claim
about a physical clock or chemistry mechanism.
"""
from fractions import Fraction
from dataclasses import dataclass

PHASES = tuple(Fraction(i,5) for i in range(6))
TRANSFER_QUANTUM = Fraction(1,5)
UNIQUE_TOROIDAL_PHASES = 5

@dataclass(frozen=True)
class StepResult:
    phase_index: int
    phase: Fraction
    committed: bool
    wrapped: bool

class Toroid5CommitClock:
    def __init__(self):
        self.phase_index = 0
        self.commits = 0

    @property
    def phase(self):
        return Fraction(self.phase_index, 5)

    def step(self):
        self.phase_index += 1
        committed = self.phase_index == 5
        wrapped = False
        out_phase = Fraction(self.phase_index, 5)
        if committed:
            self.commits += 1
        return StepResult(self.phase_index, out_phase, committed, wrapped)

    def wrap(self):
        if self.phase_index != 5:
            raise RuntimeError("wrap requires completed closure at phase 1")
        self.phase_index = 0
        return StepResult(0, Fraction(0,1), False, True)

    def run_cycle(self):
        out=[]
        for _ in range(5):
            out.append(self.step())
        out.append(self.wrap())
        return out

def closure_gate(neg=-1, zero=0, pos=1):
    return (neg + zero + pos) == 0

def benchmark(cycles=100000):
    c = Toroid5CommitClock()
    steps = 0
    for _ in range(cycles):
        for expected in range(1,6):
            r=c.step()
            steps += 1
            assert r.phase == Fraction(expected,5)
            assert r.committed == (expected==5)
        w=c.wrap()
        assert w.phase == 0 and w.wrapped
    assert c.commits == cycles
    assert steps == 5*cycles
    return {
        "cycles": cycles,
        "transfer_steps": steps,
        "commits": c.commits,
        "exact_phase_error": Fraction(0,1),
        "closure_gate": closure_gate(),
    }

def validate():
    assert PHASES == (Fraction(0,1),Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5),Fraction(1,1))
    assert TRANSFER_QUANTUM == Fraction(1,5)
    assert UNIQUE_TOROIDAL_PHASES == 5
    assert closure_gate()
    b=benchmark(1000)
    assert b["transfer_steps"] == 5000
    assert b["commits"] == 1000
    assert b["exact_phase_error"] == 0
    return True

if __name__=="__main__":
    validate()
    print("0e / TOROID-5 DETERMINISTIC COMMIT CLOCK PASS")
