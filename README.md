# neutral_sequence_generator
Creates a DNA sequence that has motifs distributed at a specified frequency seperated by a neutral sequence that purposefully does not contain the motifs.

Uses SiteOut which was developed by researchers at Harvard University

GitHub:
https://github.com/levantapatin/siteout

Research Paper:
Estrada J, Ruiz-Herrero T, Scholes C, Wunderlich Z, DePace AH (2016)
SiteOut: An Online Tool to Design Binding Site-Free DNA Sequences.
PLoS ONE 11(3): e0151740. https://doi.org/10.1371/journal.pone.0151740


Use:

Neutral_Sequence_Generator_Notebook.ipynb

  -Look at the structure and functions of the program
  
Neutral_Sequence_Generator.py

  -The program that uses the does the work producing neutral sequences with the TFBS
  
  -To use call the sequence_generator() function with your parameters
  
SiteOut.py

  -This was the algorithm used to produce the neutral sequence
  
example_outputs

  /my_example.faa
  
    -This is the fasta file that contains the neutral sequences
    
  /Sequences.txt & /Motifs.txt
  
    -These files are used by siteout.py to produce the sequences
    
motif_pfm/

  This folder contains four transcription factor binding site position frequency matrices
  that are most involved in drosophila development.
  
  To create your own motif_pfm folder download pfm from JASPAR database,
  I had to modify these by deleting all words and letters before the position frequencies.
