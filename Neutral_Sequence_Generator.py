"""To use, change the directory for motif_reader and 
use sequence generator with your desired parameters"""


import random
from Bio import motifs
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import os


"""motif_reader looks in the folder that contains 
the .pfm for motifs (downloaded from Jaspar) 
and reads and saves each motif in the folder"""
def motif_reader(path_name):
    motif_list =[]
    for filename in os.listdir(path_name):
        print(filename)
        with open(path_name + filename) as handle:
             word = motifs.read(handle, "pfm")
             handle.close()
        motif = str(word.consensus)
        print(motif)
        motif_list.append(motif)

    return motif_list


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'motif_pfm/')
motifs_test = motif_reader(filename)


"""Creates a list of the motifs with the proportion
 of the motifs determined by the probabilities and length"""

def motif_dist(motifs, probabilities, length):
	dist = []
	for i,j in zip(motifs,probabilities):
		repeats = round((j*length)/len(i))
		for k in range(0, repeats):
			dist.append(i)

	dist.append('A')
	random.shuffle(dist)
	return dist

"""Writes the Sequence.txt file, used for siteout.py, using the distribution and the list of motifs"""
def write_seq_txt(dist, motifs):

	seq_txt = open("example_outputs/Sequences.txt", "w")
	for i in dist:
		
		
		mot = str(motifs.pop())
		seq_txt.write(mot+",")
		seq_txt.write(str(i) + "")
		seq_txt.write("\n")

	seq_txt.close()


"""Writes the Motifs.txt file, used for siteout.py

Motifs.txt contains the motifs that siteout will exclude from the neutral sequences"""
def write_motif_txt(motifs):
	mot_txt = open("example_outputs/motifs.txt", "w")
	for i in range(1, len(motifs)+1 ):
		mot_txt.write("> motif" + str(i))
		mot_txt.write("\n")
		mot_txt.write(motifs[i-1])
		mot_txt.write("\n")
	mot_txt.close()


"""Uses Python2 to run siteout.py"""
import subprocess
def siteout_call(GC):
	process = subprocess.run("C:/Python27/python.exe siteout.py .05 50 "+'50'+ " example_outputs/Sequences.txt example_outputs/motifs.txt")


"""creates a distribution of numbers that add 
up to the amount of netural sequence we need to 
create a sequence with the desired length and number of motifs"""
def distribution(length, probability):
	divisions = (length * (probability/8))
	length = length - (8*divisions)
	rand_col = []
	for i in range(0, int(divisions)):
		rand_col.append(random.random())

	total = sum(rand_col)
	sum_k = []
	for j in rand_col:
		sum_k.append(round((j/total)*length))

	if sum_k == []:
		sum_k = [int(length)]
	return sum_k

"""This is the function that develops one neutral sequence using all the previous functions."""
def main(length, probabilities, GC_percent=50.0):

	motifs = motifs_test
	motif_list = motif_dist(motifs,probabilities, length)
	numbers = distribution(length, sum(probabilities))
	write_seq_txt(numbers, motif_list)
	write_motif_txt(motifs)
	siteout_call(str(GC_percent))


"""This brings together all functions 
and creates a fasta file that has number randomly generated sequences with a random enhancer functionality"""
def sequence_generator(length, motif_frequencies,number, filename="example_outputs/my_example.faa"):

    write=[]
    for i in range(0,number):

        main(length,motif_frequencies)

        generated_sequence = SeqIO.read("example_outputs/neutralseq.fa", "fasta")
        generated_sequence = generated_sequence.seq
        

        
        enhancer = str(random.randint(0,1))
        output = SeqRecord(generated_sequence, id=str(i+1)+'|'+enhancer, name="random", description="This is a randomly generated sequence")
        write.append(output)

    SeqIO.write(write, filename, "fasta")

#Sample call
sequence_generator(1000,[.005,.005,.005,.006],24)


