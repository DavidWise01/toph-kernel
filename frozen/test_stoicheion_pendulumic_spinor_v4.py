from decimal import Decimal
from stoicheion_pendulumic_spinor_v4 import *

def test_spinors():
    assert norm2(S1)==norm2(S2)==13
    assert vector_sum(S1,S2)==(1,1)

def test_pendulum():
    c=full_swing()
    assert len(c)==2601
    assert c[:4]==[Decimal("13"),Decimal("12.99"),Decimal("12.98"),Decimal("12.97")]
    assert c[1300]==Decimal("0")
    assert c[-4:]==[Decimal("12.97"),Decimal("12.98"),Decimal("12.99"),Decimal("13")]
    assert all(c[i]==c[-1-i] for i in range(len(c)))

def test_fallouts():
    assert len(full_swing())-1==2600
    assert 2600==26*100
    assert (-1)+0+(+1)==0

if __name__=="__main__":
    test_spinors(); test_pendulum(); test_fallouts()
    print("0e / STOICHEION PENDULUMIC SPINOR v4 TEST PASS")
