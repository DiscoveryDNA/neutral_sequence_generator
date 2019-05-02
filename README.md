# neutral_sequence_generator

Creates a DNA sequence that has motifs distributed at a specified frequency seperated by a neutral sequence that purposefully does not contain the motifs. This program uses [SiteOut](https://github.com/levantapatin/siteout
) which was developed by researchers at Harvard University. 

## code
- `Neutral_Sequence_Generator_Notebook.ipynb`: Looks at the structure and functions of the program
- `Neutral_Sequence_Generator.py`: This script program that does the work producing neutral sequences with the TFBS. To use call the `sequence_generator()` function with your parameters.
- `SiteOut.py`: This is the algorithm used to produce the neutral sequence.
  
## example_outputs

- `/my_example.faa`: This is the fasta file that contains the neutral sequences
- `/Sequences.txt & /Motifs.txt`: These files are used by `siteout.py` to produce the sequences
-  `motif_pfm/`: This folder contains four transcription factor binding site position frequency matrices
  that are most involved in drosophila development. To create your own motif_pfm folder download pfm from JASPAR database,
  I had to modify these by deleting all words and letters before the position frequencies.
  
## control_seqs

There are three different types of control sequences:
- There are 500 random sequence files that were generated with no TFBS motifs. These are the neutral_XXX.fa files.

- There are 2000 sequence files that were generated with a motif probability of .25 for each motif. 
Meaning there are 500 of each of four motifs, where that motif is at a probability of .25 and the rest are at 0.
These are named freq_0.25XYYY.fa Where the 0.25 represents the probability. X represents which motif it is in the list
of motifs and YYY represents which number of the 500 it is.

- There are a large number of sequences that had systematically generated motif probabilities. The probability of each 
motif was able to be controlled independently. Each motif was cycled through a probability ranging from .01-.1. 
These are named freqrange_X_Y_W_Z.fa Where each letter represents the percent probability that the motif appears in the sequence.
  
## References

Estrada J, Ruiz-Herrero T, Scholes C, Wunderlich Z, DePace AH (2016)
SiteOut: An Online Tool to Design Binding Site-Free DNA Sequences.
PLoS ONE 11(3): e0151740. https://doi.org/10.1371/journal.pone.0151740

