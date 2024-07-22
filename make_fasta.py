# Make a fasta file from the BLAST results using simple filter rules
# This can then be used for more specialised MSA and downstream analysis + visualisation
# A. Vargas Richards, 22.07.2024

import subprocess

def to_fasta(blast_results): # create a fasta file with multiple sequences 
    fasta_file = blast_results + '.fasta'
    with open(blast_results, 'r') as results:
        with open(fasta_file, 'w') as fasta:
            for line in results:
                if line.strip(): 
                    break
            for line in results:
                if '>' in line:
                    fasta.write(line)   
                if 'Sbjct' in line:
                    line = ''.join([i for i in line if not i.isdigit()]) 
                    fasta.write(line)
    return

'''
def add_query()

def perform_msa(fasta):
    subprocess.run(["muscle","-in", fasta], shell=True, check=True, capture_output=True)

def verify_msa(fasta):
    

    return 
'''