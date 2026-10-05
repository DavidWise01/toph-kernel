"""TOPH PRIM 3 / -kana serial constructor.

Distinct from pairwise embedding:
- preserves seed order
- walks one anchor forward over later symbols
- emits signed traversal in -,+ order
- appends an explicit carry before advancing the anchor
- never emits reverse duplicates (ba, ca, ...)
"""

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class Event:
    kind: str
    anchor: str
    target: Optional[str]
    polarity: Optional[int]
    token: str


def serial_constructor(seed: Iterable[str]) -> List[Event]:
    symbols = list(seed)
    if len(symbols) < 2:
        raise ValueError("seed must contain at least two symbols")
    if len(set(symbols)) != len(symbols):
        raise ValueError("seed symbols must be distinct")

    events: List[Event] = []

    for i, anchor in enumerate(symbols[:-1]):
        for target in symbols[i + 1:]:
            events.append(Event("traverse", anchor, target, -1, f"-{anchor}{target}"))
            events.append(Event("traverse", anchor, target, +1, f"+{anchor}{target}"))

        # append-only carry: advance the active anchor after its forward walk
        events.append(
            Event("carry", anchor, symbols[i + 1], None, f"{anchor}->{symbols[i + 1]}")
        )

    return events


def traversal_tokens(seed: Iterable[str]) -> List[str]:
    return [e.token for e in serial_constructor(seed) if e.kind == "traverse"]


def carry_tokens(seed: Iterable[str]) -> List[str]:
    return [e.token for e in serial_constructor(seed) if e.kind == "carry"]


def phase_degrees(seed: Iterable[str], step_degrees: int = 60) -> int:
    """Signed traversal count times the requested phase step."""
    return len(traversal_tokens(seed)) * step_degrees


if __name__ == "__main__":
    seed = "abcd"
    print("seed:", f"-{seed}+")
    print("traverse:", " ".join(traversal_tokens(seed)))
    print("carry:", " | ".join(carry_tokens(seed)))
    print("phase:", phase_degrees(seed), "degrees")
