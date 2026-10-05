"""STOICHEION Elemental Expansion — known elements 001..118.

This is a symbolic STOICHEION address register layered on the standard
chemical-element identities. Atomic number/name/symbol are standard chemistry;
STOICHEION fields are model-local addressing metadata.
"""

from dataclasses import dataclass

RAW = """1,H,hydrogen
2,He,helium
3,Li,lithium
4,Be,beryllium
5,B,boron
6,C,carbon
7,N,nitrogen
8,O,oxygen
9,F,fluorine
10,Ne,neon
11,Na,sodium
12,Mg,magnesium
13,Al,aluminium
14,Si,silicon
15,P,phosphorus
16,S,sulfur
17,Cl,chlorine
18,Ar,argon
19,K,potassium
20,Ca,calcium
21,Sc,scandium
22,Ti,titanium
23,V,vanadium
24,Cr,chromium
25,Mn,manganese
26,Fe,iron
27,Co,cobalt
28,Ni,nickel
29,Cu,copper
30,Zn,zinc
31,Ga,gallium
32,Ge,germanium
33,As,arsenic
34,Se,selenium
35,Br,bromine
36,Kr,krypton
37,Rb,rubidium
38,Sr,strontium
39,Y,yttrium
40,Zr,zirconium
41,Nb,niobium
42,Mo,molybdenum
43,Tc,technetium
44,Ru,ruthenium
45,Rh,rhodium
46,Pd,palladium
47,Ag,silver
48,Cd,cadmium
49,In,indium
50,Sn,tin
51,Sb,antimony
52,Te,tellurium
53,I,iodine
54,Xe,xenon
55,Cs,caesium
56,Ba,barium
57,La,lanthanum
58,Ce,cerium
59,Pr,praseodymium
60,Nd,neodymium
61,Pm,promethium
62,Sm,samarium
63,Eu,europium
64,Gd,gadolinium
65,Tb,terbium
66,Dy,dysprosium
67,Ho,holmium
68,Er,erbium
69,Tm,thulium
70,Yb,ytterbium
71,Lu,lutetium
72,Hf,hafnium
73,Ta,tantalum
74,W,tungsten
75,Re,rhenium
76,Os,osmium
77,Ir,iridium
78,Pt,platinum
79,Au,gold
80,Hg,mercury
81,Tl,thallium
82,Pb,lead
83,Bi,bismuth
84,Po,polonium
85,At,astatine
86,Rn,radon
87,Fr,francium
88,Ra,radium
89,Ac,actinium
90,Th,thorium
91,Pa,protactinium
92,U,uranium
93,Np,neptunium
94,Pu,plutonium
95,Am,americium
96,Cm,curium
97,Bk,berkelium
98,Cf,californium
99,Es,einsteinium
100,Fm,fermium
101,Md,mendelevium
102,No,nobelium
103,Lr,lawrencium
104,Rf,rutherfordium
105,Db,dubnium
106,Sg,seaborgium
107,Bh,bohrium
108,Hs,hassium
109,Mt,meitnerium
110,Ds,darmstadtium
111,Rg,roentgenium
112,Cn,copernicium
113,Nh,nihonium
114,Fl,flerovium
115,Mc,moscovium
116,Lv,livermorium
117,Ts,tennessine
118,Og,oganesson"""

@dataclass(frozen=True)
class ElementSlot:
    atomic_number: int
    symbol: str
    name: str
    register: str
    stoicheion_slot: int

def build_register():
    rows = []
    for line in RAW.strip().splitlines():
        z, symbol, name = line.split(",", 2)
        z = int(z)
        rows.append(ElementSlot(
            atomic_number=z,
            symbol=symbol,
            name=name,
            register=f"E{z:03d}",
            stoicheion_slot=z,
        ))
    return tuple(rows)

ELEMENTS = build_register()
BY_Z = {e.atomic_number: e for e in ELEMENTS}
BY_SYMBOL = {e.symbol: e for e in ELEMENTS}

def render_ascii():
    return "\n".join(
        f"{e.register} :: {e.symbol:<2} :: {e.name}"
        for e in ELEMENTS
    )

if __name__ == "__main__":
    print(render_ascii())
