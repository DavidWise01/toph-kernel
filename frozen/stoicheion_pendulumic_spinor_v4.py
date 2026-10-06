"""STOICHEION pendulumic spinor v4.

Model-local benchmark:
  S1=(-2,+3), S2=(+3,-2)
  norm^2(S1)=norm^2(S2)=13
  pendulum scalar: 13 -> 0 -> 13 in 0.01 steps

Scientific boundary: 13 is the squared Euclidean norm of each supplied vector,
not its Euclidean magnitude. The pendulum interpretation is STOICHEION-local.
"""
from decimal import Decimal

S1=(-2,3)
S2=(3,-2)
MAX=Decimal("13")
STEP=Decimal("0.01")

def norm2(v):
    return v[0]*v[0]+v[1]*v[1]

def vector_sum(a,b):
    return (a[0]+b[0],a[1]+b[1])

def half_swing():
    n=int(MAX/STEP)
    return [MAX-STEP*i for i in range(n+1)]

def full_swing():
    down=half_swing()
    up=[STEP*i for i in range(1,int(MAX/STEP)+1)]
    return down+up

def validate():
    assert norm2(S1)==13
    assert norm2(S2)==13
    assert vector_sum(S1,S2)==(1,1)
    h=half_swing()
    c=full_swing()
    assert len(h)==1301
    assert len(c)==2601
    assert c[0]==MAX and c[-1]==MAX
    assert c[1300]==Decimal("0")
    assert all(c[i]==c[-1-i] for i in range(len(c)))
    assert len(c)-1==2600
    assert 2600==26*100
    assert (-1)+0+(+1)==0
    return True

if __name__=="__main__":
    validate()
    print("0e / STOICHEION PENDULUMIC SPINOR v4 PASS")
