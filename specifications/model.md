# PyEED Data Model

PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.

### ProteinSequence
- __protein_sequence_id__
  - Type: [__protein_sequence_id__](#__protein_sequence_id__)
  - Description: Reference to the corresponding protein sequence 
- __genbank_protein_id__
  - Type: string
  - Description: Systematic name of the protein.
- __amino_acid_sequence__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __function__
  - Type: string
  - Description: Identifier of fubtion

### DNASequence


- __dna_sequence_id__
  - Type: string
  - Description: Reference to the corresponding dna sequence
- __genebank_dna_id__
  - Type: string
  - Description: Identifier for the NCBI database
- __Nucleotide__
  - Type: string
  - Description: The Deoxyribonucleic acid sequence of the DNA sequence object.
  ### __protein_sequence_id__
    - Type: string
    - Description: Reference to the corresponding protein sequence to which this DNA sequence translates 
