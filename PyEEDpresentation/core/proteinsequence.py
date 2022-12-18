import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )

    protein_databank_id: Optional[str] = Field(
        description="Systematic name of the protein.", default=None
    )

    lenght: Optional[str] = Field(
        description="Reference to the corresponding protein sequence", default=None
    )

    quary_seq: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    match_seq: Optional[str] = Field(description="Identifier of fubtion", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Database-present.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="27fd5c8b731c22fb69ecd1464328f868e4827001"
    )
