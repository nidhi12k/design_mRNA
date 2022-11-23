# design_mRNA

## Introduction
A program to generate mRNA from cDNA sequences  

## 1. Prerequisites
python=3.7  
biopython  
ViennaRNA  
rna-tools

Create and activate environment  
```
        $ conda env create --file=env.yaml  
        $ conda activate design_mrna
```
  
    
##  2. Run

    python3 ./script.py -i <path to FASTA file with cDNA sequence>
  
  
## 3. Output  
rna_seq_ss.ps file will be reated with secondary strucure of RNA sequence.  
  
eGFP Secondary structure predicted  
![eGFP](https://github.com/nidhi12k/design_mRNA/blob/main/eGFP/rna_seq_ss.ps)  
  
  


