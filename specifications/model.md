# PyEED Data Model

PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.

### ProteinSequence

- __protein_databank_id__
  - Type: string
  - Description: Presented protein sequence  
- __lenght__
  - Type: int
  - Description: Systematic name of the protein.
- __quary_seq__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __match_seq__
  - Type: string
  - Description: Data base ID



### DNASequence

- __protein_databank_id__
  - Type: string
  - Description: Reference to the Translated DNA from the matching Protein sequence
- __dna_sequence__
  - Type: string
  - Description: Presented protein sequence


 
