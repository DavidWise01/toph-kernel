"""Blind cyclic STOICHEION dot/bar scan to 250.

Assumption made explicit from the user's latest example:
  base carrier = '..||..|' (value 10)
  next start   = '||..|..' (left-rotate by 2 glyph slots)
  then switch  = alternate rotation direction after each transversal

Glyph values:
  '.' = 1
  '|' = 2

We preserve the seven-glyph carrier under rotation, so every carrier view
still has scalar value 10. Numeric addresses 1..250 are represented as
whole 10-unit carriers plus a scalar remainder. We then inspect the known
nuclear-shell anchor 184 and all addresses through 250 for structural
coincidences (exact carrier boundaries, repeated remainder classes, and
palindromic/mirror carrier views).

This is a model-local cipher test, not a nuclear-physics derivation.
"""

BASE = "..||..|"
LIMIT = 250
KNOWN_MAGIC = (2,8,20,28,50,82,126,184)

def val(s):
    return sum(1 if c=="." else 2 for c in s)

def rol(s,k):
    k%=len(s)
    return s[k:]+s[:k]

def ror(s,k):
    return rol(s,-k)

def carrier_states():
    # Start at base. First transversal matches the user's supplied next start:
    # '..||..|' -> '||..|..' (left 2). Then alternate L2/R2.
    out=[BASE]
    s=BASE
    left=True
    seen={s}
    for _ in range(32):
        s = rol(s,2) if left else ror(s,2)
        left = not left
        if s in seen:
            break
        out.append(s); seen.add(s)
    return tuple(out)

STATES = carrier_states()

REM = {
  0:"",
  1:".",
  2:"..",
  3:".|",
  4:"||",
  5:"||.",
  6:"|||",
  7:"|||.",
  8:"||||",
  9:"||||.",
}

def encode(n):
    q,r=divmod(n,10)
    # use alternating carrier state by completed block index
    blocks=[STATES[i % len(STATES)] for i in range(q)]
    return "".join(blocks)+REM[r]

def structural(n):
    q,r=divmod(n,10)
    state=STATES[(q-1)%len(STATES)] if q else BASE
    return {
      "n":n,"q10":q,"r10":r,"glyph":encode(n),
      "carrier_state":state,
      "exact_10_boundary": r==0,
      "mirror_carrier": state==state[::-1],
      "remainder_magic": r in (0,2,8),
    }

def scan():
    return [structural(n) for n in range(1,LIMIT+1)]

if __name__=="__main__":
    print("base", BASE, val(BASE))
    print("states", STATES)
    print("184", structural(184))
    print("magic")
    for n in KNOWN_MAGIC:
        print(structural(n))
    print("exact 10 boundaries after 184:",
          [x["n"] for x in scan() if 184 < x["n"] <=250 and x["exact_10_boundary"]])
