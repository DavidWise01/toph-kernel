"""STOICHEION elemental property expansion for elements 1..118.

Authoritative chemistry feed:
  PubChem periodic-table CSV:
  https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/CSV

STOICHEION fields are symbolic metadata layered on top of chemistry.
Missing PubChem values remain missing; unknown is never coerced to zero.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from io import StringIO
import csv
import json
from pathlib import Path
from urllib.request import urlopen

PUBCHEM_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/CSV"

PUBCHEM_FIELDS = (
    "AtomicNumber",
    "Symbol",
    "Name",
    "AtomicMass",
    "CPKHexColor",
    "ElectronConfiguration",
    "Electronegativity",
    "AtomicRadius",
    "IonizationEnergy",
    "ElectronAffinity",
    "OxidationStates",
    "StandardState",
    "MeltingPoint",
    "BoilingPoint",
    "Density",
    "GroupBlock",
    "YearDiscovered",
)

NEON_ATOMIC_NUMBER = 10
NEON_VALENCE_LANGUAGE = "..||..|"


def period(z: int) -> int:
    for upper, p in ((2,1),(10,2),(18,3),(36,4),(54,5),(86,6),(118,7)):
        if z <= upper:
            return p
    raise ValueError(z)


def group(z: int):
    rows = {
        1:[1,18],
        2:[1,2,13,14,15,16,17,18],
        3:[1,2,13,14,15,16,17,18],
        4:list(range(1,19)),
        5:list(range(1,19)),
        6:[1,2,3,*range(4,19)],
        7:[1,2,3,*range(4,19)],
    }
    starts={1:1,2:3,3:11,4:19,5:37,6:55,7:87}
    p=period(z)
    off=z-starts[p]
    if p in (6,7) and off>2:
        if off<=16:
            return None
        off-=14
    return rows[p][off]


def _num(s):
    if s is None or s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return s


@dataclass(frozen=True)
class ElementRecord:
    atomic_number: int
    symbol: str
    name: str
    period: int
    group: int | None
    atomic_mass: float | str | None
    cpk_hex_color: str | None
    electron_configuration: str
    electronegativity_pauling: float | None
    atomic_radius_pm: float | None
    ionization_energy_ev: float | None
    electron_affinity_ev: float | None
    oxidation_states: str | None
    standard_state: str
    melting_point_k: float | None
    boiling_point_k: float | None
    density_g_cm3: float | None
    category: str
    year_discovered: str
    stoicheion_address: str
    stoicheion_valence_language: str | None
    stoicheion_note: str | None


def from_pubchem_row(row: dict[str,str]) -> ElementRecord:
    z=int(row["AtomicNumber"])
    return ElementRecord(
        atomic_number=z,
        symbol=row["Symbol"],
        name=row["Name"],
        period=period(z),
        group=group(z),
        atomic_mass=_num(row["AtomicMass"]),
        cpk_hex_color=row["CPKHexColor"] or None,
        electron_configuration=row["ElectronConfiguration"],
        electronegativity_pauling=_num(row["Electronegativity"]),
        atomic_radius_pm=_num(row["AtomicRadius"]),
        ionization_energy_ev=_num(row["IonizationEnergy"]),
        electron_affinity_ev=_num(row["ElectronAffinity"]),
        oxidation_states=row["OxidationStates"] or None,
        standard_state=row["StandardState"],
        melting_point_k=_num(row["MeltingPoint"]),
        boiling_point_k=_num(row["BoilingPoint"]),
        density_g_cm3=_num(row["Density"]),
        category=row["GroupBlock"],
        year_discovered=row["YearDiscovered"],
        stoicheion_address=f"E{z:03d}",
        stoicheion_valence_language=NEON_VALENCE_LANGUAGE if z==NEON_ATOMIC_NUMBER else None,
        stoicheion_note="NEON 10 :: full bounded shell" if z==NEON_ATOMIC_NUMBER else None,
    )


def parse_pubchem_csv(text: str) -> tuple[ElementRecord,...]:
    rows=list(csv.DictReader(StringIO(text)))
    if [int(r["AtomicNumber"]) for r in rows] != list(range(1,119)):
        raise ValueError("expected contiguous PubChem elements 1..118")
    return tuple(from_pubchem_row(r) for r in rows)


def fetch_pubchem(timeout: int=30) -> tuple[ElementRecord,...]:
    with urlopen(PUBCHEM_URL, timeout=timeout) as r:
        return parse_pubchem_csv(r.read().decode("utf-8"))


def write_snapshot(records, out_json: str|Path, out_csv: str|Path):
    records=tuple(records)
    Path(out_json).write_text(
        json.dumps([asdict(r) for r in records], indent=2, ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    fields=list(asdict(records[0]).keys())
    with Path(out_csv).open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow(asdict(r))


if __name__ == "__main__":
    here=Path(__file__).resolve().parent
    records=fetch_pubchem()
    write_snapshot(
        records,
        here/"stoicheion_elements_001_118_full.json",
        here/"stoicheion_elements_001_118_full.csv",
    )
    ne=records[9]
    assert ne.atomic_number == 10 and ne.symbol == "Ne"
    assert ne.stoicheion_valence_language == "..||..|"
    print("0e / STOICHEION FULL PROPERTY EXPANSION 001-118 PASS")
