from __future__ import annotations
from typing import List, Optional, TextIO, Any


class Citizen:
    """A Citizen: a citizen in a Society.

    === Public Attributes ===
    cid:
        The ID number of this citizen.
    manufacturer:
        The manufacturer of this Citizen.
    model_year:
        The model year of this Citizen.
    job:
        The name of this Citizen's job within the Society.
    rating:
        The rating of this Citizen.

    === Private Attributes ===
    _superior:
        The superior of this Citizen in the society, or None if this Citizen
        does not have a superior.
    _subordinates:
        A list of this Citizen's direct subordinates (that is, Citizens that
        work directly under this Citizen).
    _to_superior:
        A value which is used to record the superior at a specific level.

    === Representation Invariants ===
    - cid > 0
    - 0 <= rating <= 100
    - self._subordinates is in ascending order by the subordinates' IDs
    - If _superior is a Citizen, this Citizen is part of its _subordinates list
    - Each Citizen in _subordinates has this Citizen as its _superior
    """
    cid: int
    manufacturer: str
    model_year: int
    job: str
    rating: int
    _superior: Optional[Citizen]
    _subordinates: List[Citizen]

    def __init__(self, cid: int, name: str, model_year: int,
                 job: str, rating: int) -> None:
        """Initialize this Citizen with the ID <cid>, manufacturer
        <manufacturer>, model year <model_year>, job <job>, and rating <rating>.

        A Citizen initially has no superior and no subordinates.

        >>> c1 = Citizen(1, "Starky Industries", 3042, "Labourer", 50)
        >>> c1.cid
        1
        >>> c1.rating
        50
        """
        self.cid = cid
        self.manufacturer = name
        self.model_year = model_year
        self.job = job
        self.rating = rating
        self._superior = None
        self._subordinates = []
        self._recursive_time = 0


C0 = Citizen(0, "Starky Industries", 3042, "Labourer", 50)
C1 = Citizen(1, "Starky Industries", 3042, "Labourer", 50)
C2 = Citizen(2, "Starky Industries", 3042, "Labourer", 50)
C3 = Citizen(3, "Starky Industries", 3042, "Labourer", 50)
C4 = Citizen(4, "Starky Industries", 3042, "Labourer", 50)
C0._superior = None
C1._superior = C0
C2._superior = C1
C3._superior = C1
C4._superior = C2
C0._subordinates = [C1]
C1.subordinates = [C2, C3]
C2.subordinates = [C4]

C2.set_superior(C0)
C1.set_superior(C2)
for citizen in C2.get_direct_subordinates():
    citizen.become_subordinate_to(C)

C0._superior = None
C1._superior = C2
C2._superior = C0
C3._superior = C2
C4._superior = C1
C0._subordinates = [C2]
C1.subordinates = [C4]
C2.subordinates = [C1, C3]
