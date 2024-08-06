# Calls MUSCLE on the results of the BLAST search.
# A. Vargas Richards, NIAB 29.07.2024

# easily customisable for more specialised forms of MSA.

import subprocess, os

def call_msa(results_folder): # calls muscle on all of the 
    os.mkdir(str(results_folder) + "/MSA_results")
    for root, dirs, files in os.walk(results_folder):
        for file in files:
            if ".fasta" in file:
                print(f"Attemnpting subprocess.Popen for {file}")
                outfile = "BLAST-results/MSA_results/" + str(file)
                infile = "BLAST-results/" + str(file)
                align_process = subprocess.Popen(["muscle", "-in", infile, "-out", outfile])
                align_process.wait()

    return 

