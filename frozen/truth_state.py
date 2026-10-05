"""TOPH frozen truth-state kernel."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List

class Status(str, Enum):
    VERIFIED = "verified"
    QUARANTINED = "quarantined"
    NON_ALIGNED = "non_aligned"

@dataclass(frozen=True)
class Evidence:
    claim_id: str
    confidence: float
    provenance_ok: bool = True
    reproducible: bool = True
    independent_support: int = 1
    aligns_with_current: Optional[bool] = None

@dataclass(frozen=True)
class VerifiedState:
    claim_id: str
    confidence: float

@dataclass
class TruthKernel:
    threshold: float = 0.99
    challenge_threshold: int = 2
    past_verified: Optional[VerifiedState] = None
    current_verified: Optional[VerifiedState] = None
    history: List[VerifiedState] = field(default_factory=list)
    quarantine: List[Evidence] = field(default_factory=list)
    non_aligned: List[Evidence] = field(default_factory=list)

    def classify(self, e: Evidence) -> Status:
        merits_ok = e.provenance_ok and e.reproducible and e.independent_support >= self.challenge_threshold
        if e.aligns_with_current is False:
            self.non_aligned.append(e)
            return Status.NON_ALIGNED
        if e.confidence >= self.threshold and merits_ok:
            self._promote(e)
            return Status.VERIFIED
        self.quarantine.append(e)
        return Status.QUARANTINED

    def _promote(self, e: Evidence) -> None:
        state = VerifiedState(e.claim_id, e.confidence)
        if self.past_verified is not None:
            self.history.append(self.past_verified)
        self.past_verified = self.current_verified
        self.current_verified = state

    def should_reverify(self, *, contradictory_evidence=False, provenance_broken=False,
                        source_changed=False, time_sensitive_expired=False,
                        downstream_contradictions=0, contradiction_threshold=2) -> bool:
        return any((contradictory_evidence, provenance_broken, source_changed,
                    time_sensitive_expired,
                    downstream_contradictions >= contradiction_threshold))

    def hot_state(self):
        return self.past_verified, self.current_verified
