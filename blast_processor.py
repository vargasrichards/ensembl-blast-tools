from Bio import SearchIO

def parse_blast(input_file):
    blast_results = SearchIO.parse(input_file, "blast-tab")
    print(blast_results)
    return blast_results

parse_blast('./BLAST-cadenza/TraesCS4A02G182800')
