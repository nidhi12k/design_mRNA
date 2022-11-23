# design_mRNA

## Introduction
A program to generate mRNA from cDNA sequences  

## 1. Prerequisites
python=3.7  
biopython  
ViennaRNA

Create and activate environment  
```
        $ conda env create --file=env.yaml  
        $ conda activate design_mrna
```
  
    
##  2. Run

    python3 ./script.py -i <path to FASTA file with cDNA sequence>
  
  
## 3. Output  
rna_seq_ss.ps file will be reated with secondary strucure of RNA sequence.  


