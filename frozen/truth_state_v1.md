# TOPH Frozen Truth-State Kernel

Status: **FROZEN / APPEND-ONLY / EXCEPTION-REVERIFY**

## Active register
```
{ past_verified, current_verified }
```

Only two verified truth states remain on the hot path.

## Candidate states
- `verified` — aligns with root truth / verified prior corpus; eligible to carry forward.
- `quarantined` — unresolved; preserved, isolated, non-reproductive until evidence reaches challenge threshold.
- `non_aligned` — conflicts with current known truth/corpus consensus; preserved with provenance, not labeled bad, non-reproductive by default.

## Merit review
Promotion is based on evidence quality, provenance, reproducibility, independent support, consistency with observation, and explanatory/predictive weight. Rhetoric, popularity, or promised substance do not substitute for evidence.

## Carry rule
Verified state carries forward without full re-verification on ordinary cycles.

Re-verification is exception-driven only:
- material contradictory evidence
- broken provenance
- changed source
- expiration of a time-sensitive claim
- sufficient downstream contradiction

## Supersession
```
archive <- past_verified <- current_verified <- new_verified
```

History is never silently overwritten.

## Frozen invariant
```
HOT = {past, current}
COLD = {history, quarantine, non_aligned}
WRITE = append only
REVERIFY = exception only
```
