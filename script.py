import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import RNA
from rna_tools import Seq as sq



def command_Parse():
	parser = argparse.ArgumentParser(prog='python3 script.py', usage='%(prog)s -i <path to input fasta file of cDNA sequence> ',
    		description='Generates mRNA from cDNA sequence', epilog="***** mRNA Designer *****")
	# def check_input(file):
	#	pass

	parser.add_argument("-i", "--input", help='Enter the path to the FASTA file', required=True)
	parser.add_argument("-cdna", "--cdna", help='Set flag if the FASTA file contains cDNA sequence', required=False, action="store_true", default=False)
	parser.add_argument("-cds", "--cds", help='Set flag if the FASTA file contains coding sequence', required=False, action="store_true", default=False)
	return parser


def read_fasta(inputFile) -> Seq:
	fasta_sequences = SeqIO.parse(open(inputFile),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
	return sequence

# Get complementary of cDNA and replace Ts to Us
def cdna2mrna(sequence) -> str:
	mrnaSeq = str(Seq(sequence).complement())
	mrnaSeq = mrnaSeq.upper().replace("T","U")
	return mrnaSeq
# Get RNA sequence from CDS sequence
def cds2mrna(seq):
	mrnaSeq = seq.upper().replace("T","U")
	return mrnaSeq

def getSecondaryStructure(seq):
	# creting a fold_compound object
	fc = RNA.fold_compound(seq)
	# fc = RNA.fold_compound(seq)
	# compute minimum free energy and corresponding structure
	ss, mfe = fc.mfe()
	print("Minumum free energy: {:6.2f}".format(mfe))
	return fc, ss, mfe


def drawss(ss, seq):
	seq = sq.RNASequence(seq)
	
	# Creates rna_seq_ss.ps file in current dir 
	seq.predict_ss("RNAfold", constraints=ss)


def main():
	#parse cmd args
	parser = command_Parse()
	args = parser.parse_args()
	inputFile = args.input

	sequence = read_fasta(inputFile)

	if args.cds:
		mrnaSeq = cds2mrna(sequence)
		print(f"mRNA Sequence : {mrnaSeq}\n")
	elif args.cdna:
		mrnaSeq = cdna2mrna(sequence)
		print(f"mRNA Sequence : {mrnaSeq}\n")
	else:
		print("Please set flag -cds/--cds or -cdna/--cdna")
		exit()

	fc, ss, mfe=getSecondaryStructure(mrnaSeq)
	drawss(ss, mrnaSeq)
	print("rna_seq_ss.ps file created with secondary structure of RNA\n")


if __name__ == "__main__":
	main()