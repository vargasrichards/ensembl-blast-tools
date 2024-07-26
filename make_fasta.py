# Make a fasta file from the BLAST results using simple filter rules
# This can then be used for more specialised MSA and downstream analysis + visualisation
# A. Vargas Richards, 07.2024

import os, rest_api # rest api provides the method for fetching 

def to_fasta(blast_results): # create a fasta file with multiple sequences 
    fasta_file = blast_results + '.fasta'
    with open(blast_results, 'r') as results:
        with open(fasta_file, 'w') as fasta:
            # add query sequence
            #query_id = 


            for line in results:
                if line.strip(): 
                    break
            for line in results:
                if '>' in line:
                    fasta.write(line)   
                if 'Sbjct' in line:
                    line = ''.join([i for i in line if not i.isdigit()]) 
                    line = line.replace('Sbjct    ','')
                    fasta.write(line)
    return

# must also add the query sequence...

def make_all(directory): # 
    rel_path = str('./' + directory + '/')
    for path, directory, file in os.walk(rel_path):
        for f in file:
            if '.fasta' not in f and 'summary' not in f:
                to_fasta("BLAST-results/" + str(f) )
                print(f'Producing FASTA of file {f}')
            else:
                print(f"Skipped file {f}; it is already a FASTA or a summary file")           
    print(f"Finished summarising dir {directory}")
    return 

