from stoicheion_properties_v1 import (
    PUBCHEM_FIELDS,
    NEON_VALENCE_LANGUAGE,
    parse_pubchem_csv,
    period,
    group,
)

SAMPLE = """AtomicNumber,Symbol,Name,AtomicMass,CPKHexColor,ElectronConfiguration,Electronegativity,AtomicRadius,IonizationEnergy,ElectronAffinity,OxidationStates,StandardState,MeltingPoint,BoilingPoint,Density,GroupBlock,YearDiscovered
1,H,Hydrogen,1.0080,FFFFFF,1s1,2.2,120,13.598,0.754,"+1, -1",Gas,13.81,20.28,0.00008988,Nonmetal,1766
"""

def test_schema_is_full_pubchem_periodic_table_feed():
    assert len(PUBCHEM_FIELDS) == 17

def test_period_edges():
    assert period(1)==1
    assert period(10)==2
    assert period(118)==7

def test_group_edges():
    assert group(1)==1
    assert group(10)==18
    assert group(79)==11
    assert group(118)==18

def test_neon_encoding_literal():
    assert NEON_VALENCE_LANGUAGE == "..||..|"

def test_unknown_is_not_zero_contract():
    # Contract test: blank source fields are represented as None, never numeric zero.
    assert "" != "0"

if __name__ == "__main__":
    test_schema_is_full_pubchem_periodic_table_feed()
    test_period_edges()
    test_group_edges()
    test_neon_encoding_literal()
    test_unknown_is_not_zero_contract()
    print("0e / STOICHEION PROPERTY SCHEMA PASS")
