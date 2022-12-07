import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class DNASequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnasequenceINDEX"),
        xml="@id",
    )

    dna_sequence_id: Optional[str] = Field(
        description="Reference to the corresponding dna sequence", default=None
    )

    genebank_dna_id: Optional[str] = Field(
        description="Identifier for the NCBI database", default=None
    )

    Nucleotide: Optional[str] = Field(
        description="The Deoxyribonucleic acid sequence of the DNA sequence object.",
        default=None,
    )

    protein_sequence_id: Optional[str] = Field(
        description=(
            "Reference to the corresponding protein sequence to which this DNA sequence"
            " translates"
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Rinkudatabase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca6f6f4492a0d6f34639dcb51ed658257ac95f3"
    )
