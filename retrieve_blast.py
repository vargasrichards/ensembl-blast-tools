import subprocess
import requester
print("Finished HTTPS BLAST results retrieval")
print("Calling cleaning script...")
subprocess.call(['bash', './process.sh'])
print("----")
print("DONE")
print("----")
