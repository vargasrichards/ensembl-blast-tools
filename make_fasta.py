# Make a fasta file from the BLAST results using simple filter rules
# This can then be used for more specialised MSA and downstream analysis + visualisation
# A. Vargas Richards, 07.2024

import textwrap, os, requests, sys

def get_geneid(gene_id):
    server = "https://rest.ensembl.org"
    ext = f"/sequence/id/{gene_id}?"
    r = requests.get(server + ext, headers={"Content-Type": "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit() 
    return r.text

def get_query(blast_results): 
    print(f'Getting query seq for {blast_results}')
    query = None
    query_id = None
    with open(blast_results, 'r') as results:
        for line in results:
            if 'Query=' in line:
                query_id = line.split('=')[1].strip()
                query = get_geneid(query_id)
                break
    if query:
        return query, query_id
    else:
        return None, None

def get_geneid(gene_id):
    server = "https://rest.ensembl.org"
    ext = f"/sequence/id/{gene_id}?"
    r = requests.get(server + ext, headers={"Content-Type": "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit() 
    return r.text

def to_fasta(blast_results): 
    query, query_id = get_query(blast_results)
    fasta_file = blast_results + '.fasta'
    if query != None:

        with open(blast_results, 'r') as results:
            with open(fasta_file, 'w') as fasta:
                fasta.write(f">Query:{query_id}\n")
                query = textwrap.wrap(query, 60)
                query = '\n'.join(query)
                fasta.write(query + "\n")
                for line in results:
                    if '>' in line:
                        fasta.write(line)
                    elif 'Sbjct' in line:
                        line = ''.join([i for i in line if not i.isdigit()]) 
                        line = line.replace('Sbjct    ', '').strip()
                        fasta.write(line + "\n")
        print(f"Produced FASTA: {fasta_file}")
    return 

def make_all(directory): 
    rel_path = f'./{directory}/'
    for root, dirs, files in os.walk(rel_path):
        for file in files:
            if not file.endswith('.fasta') and 'summary' not in file:
                file_path = os.path.join(root, file)
                to_fasta(file_path)
            else:
                #print(f"Skipped file {file}; it is already a FASTA or a summary file")
                pass
    print(f"Finished summarising directory {directory}")



