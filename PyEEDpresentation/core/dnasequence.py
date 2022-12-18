import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class DNASequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnasequenceINDEX"),
        xml="@id",
    )
    protein_databank_id: Optional[str] = Field(
        description="Systematic name of the protein.",
        default=None,
    )

    dna_equence: Optional[str] = Field(
        description="Reference to the corresponding protein sequence",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Database-present.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6affc56251f449940e49749c3ebcfe67df774820"
    )
