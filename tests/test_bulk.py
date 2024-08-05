

def func(x):
    import sys, os
    sys.path.append('..')
    print(os.listdir())
    import subprocess
    import requester
    import make_fasta
    import summariser 
    import call_msa
    try:

        requester.fetch_blast(
        varieties = ['claire', 'paragon', 'cadenza', 'robigus'],
        species = 'Triticum_aestivum_',
        batch_id = 'dH2MUh3d5qVTSKJc',
        first = 23302378,
        last = 23302413)

        print("Finished HTTPS BLAST results retrieval")
        print("Calling cleaning script...")
        subprocess.call(['bash', './process.sh'])
        print("----------------------------")
        print("DONE CLEANING FILES")
        print("----------------------------")
        print("Generating summary files")
        summariser.summarise_all("BLAST-results")
        print("Generating FASTA files...")
        make_fasta.make_all("BLAST-results")
        print("----------------------------")
        print("Finished making FASTA files")
        print("----------------------------")
        print("Proceeding with Multiple Sequence Alignment using MUSCLE")

        # perhaps wait a bit here.... 
        call_msa.call_msa("BLAST-results")
        print("Finished MSA")
        return 0 
    except:
        return 1
    
def test_answer():
    assert(func(2) == 0)

