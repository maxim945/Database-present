```mermaid
classDiagram
    ProteinSequence *-- - __protein_sequence_id__ -
    
    class ProteinSequence {
        +- __protein_sequence_id__ - protein_sequence_id
        +string genbank_protein_id
        +string amino_acid_sequence
        +string function
    }
    
    class DNASequence {
        +string dna_sequence_id
        +string genebank_dna_id
        +string Nucleotide
        +string protein_sequence_id
    }
    
```