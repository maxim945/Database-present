import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Systematic name of the protein.",
    )

    amino_acid_sequence: str = Field(
        ...,
        description="The amino acid sequence of the protein sequence object.",
    )

    nr_id: Optional[str] = Field(
        description="Identifier for the NCBI NR database",
        default=None,
    )

    uniprot_id: Optional[str] = Field(
        description="Identifier for the UniProt database",
        default=None,
    )

    pdb_id: List[str] = Field(
        description="Identifier for the PDB database",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/Rinkudatabase.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e33d4626923743fb9c990ac83d5d3345ebf6e63f"
    )
