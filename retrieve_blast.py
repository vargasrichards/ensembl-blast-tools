# Main script called by user.
# 
# A. Vargas Richards, 22.07.2024

import subprocess
import requester
import make_fasta
import summariser 

print("Finished HTTPS BLAST results retrieval")
print("Calling cleaning script...")
subprocess.call(['bash', './process.sh'])
print("----")
print("DONE CLEANING FILES")
print("----")
print("Generating summary files")

summariser.summarise("BLAST-results")

print("Generating FASTA files...")

# make_fasta.to_fasta("BLAST-results")
make_fasta.make_all("BLAST-results")
print("-----")
print("Finished making FASTA files")
print("-----")

print("Proceeding with Multiple Sequence Alignment using MUSCLE")

#subprocess.call(
