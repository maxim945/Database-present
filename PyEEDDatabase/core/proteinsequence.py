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
        description="Presented protein sequence", default=None
    )

    lenght: Optional[int] = Field(
        description="Systematic name of the protein.", default=None
    )

    quary_seq: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    match_seq: Optional[str] = Field(description="Data base ID", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Database-present.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="4962d841eda2768dfe97ff986f36b328575466f4"
    )
