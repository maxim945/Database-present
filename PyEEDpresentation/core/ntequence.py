import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ntequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("ntequenceINDEX"),
        xml="@id",
    )
    protein_databank_id: Optional[str] = Field(
        description="Systematic name of the protein.",
        default=None,
    )

    lenght: Optional[str] = Field(
        description="Reference to the corresponding protein sequence",
        default=None,
    )

    quary_seq: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    match_seq: Optional[str] = Field(
        description="Identifier of",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Database-present.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4de257347df8802f941497e112be583b688db8a0"
    )
