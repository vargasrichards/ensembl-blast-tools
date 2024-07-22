# Main script called by user.

# A. Vargas Richards, 22.07.2024

import subprocess
import requester
import make_fasta

print("Finished HTTPS BLAST results retrieval")
print("Calling cleaning script...")
subprocess.call(['bash', './process.sh'])
print("----")
print("DONE CLEANING FILES")
print("----")

print("Generating FASTA files...")

make_fasta.to_fasta(blast)