import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )
    protein_databank_id: Optional[str] = Field(
        description="Presented protein sequence",
        default=None,
    )

    lenght: Optional[int] = Field(
        description="Systematic name of the protein.",
        default=None,
    )

    quary_seq: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    match_seq: Optional[str] = Field(
        description="Data base ID",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Database-present.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f343422e0a20ad580331f6650e34067ef47ccae2"
    )
