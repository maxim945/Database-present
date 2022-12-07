import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field


@forge_signature
class Equivalence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("equivalenceINDEX"),
        xml="@id",
    )
    reference_position: int = Field(
        ...,
        description="Equivalent position in the reference sequence",
    )

    sequence_position: int = Field(
        ...,
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Rinkudatabase.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e33d4626923743fb9c990ac83d5d3345ebf6e63f"
    )
