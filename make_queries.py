# Script for making a fasta file of multiple query sequences of interest for input into BLAST
# Takes as input the gene IDs of the query sequence of interest
# A. Vargas Richards, 08.08.2024

import textwrap, os, requests, sys, make_fasta

gene_list = []
def make_list(path):
    with open(path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                gene_list.append(stripped_line)
    print(gene_list)
    return gene_list

gene_list = make_list('genes_list.txt')


def to_fasta(gene_list): 
    for gene in gene_list:
        if gene != None:
            with open('queries.fasta', 'w') as query_file:
                query_file.write(f">{gene}\n")
                query = textwrap.wrap(query, 60)
                query = '\n'.join(query)
                query_file.write(query + "\n")

    return 

def request_seqs(seqs):
    filestring = ''
    for gene in seqs:
        
        server = "https://rest.ensembl.org"
        ext = "/sequence/id/"+ str(gene) + "?"
        
        r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
        
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        text = r.text
        wrapped_text = textwrap.wrap(text, 60)
        wrapped_text = '\n'.join(wrapped_text)
        fasta_element = '>' + str(gene) + '\n' + str(wrapped_text) + '\n'
        filestring += fasta_element


    with open('query_sequences.fasta', 'w') as f:
        print(filestring)
        f.write(filestring)
    return 

request_seqs(gene_list)