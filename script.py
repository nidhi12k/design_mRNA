import argparse
from Bio import SeqIO



def command_Parse():
	parser = argparse.ArgumentParser(prog='python3 script.py', usage='%(prog)s -i <path to input fasta file of CDS> ',
    		description='Generates mRNA from cDNA sequence', epilog="***** mRNA Designer *****")
	# def check_input(file):


	parser.add_argument("-i", "--input", help='Enter the path to the FASTA file', required=True)
	
	return parser


def read_fasta(inputFile):
	fasta_sequences = SeqIO.parse(open(inputFile),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
	return sequence




def main():
	#parse cmd args
	parser = command_Parse()
	args = parser.parse_args()
	inputFile = args.input

	sequence = read_fasta(inputFile)



if __name__ == "__main__":
	main()