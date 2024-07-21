# Module which can provide mapping of genes of interest in wheat
# A. Vargas Richards, 07/2024

import pandas as pd
import requests
from bs4 import BeautifulSoup

def fetch_position(geneid):
    str1 = 'https://plants.ensembl.org/Triticum_aestivum/Location/View?db=core;g='
    url = str1 + str(geneid)
    gene_data = requests.get(url)
    html_content = gene_data.text
    soup = BeautifulSoup(html_content, 'html.parser')
    summary_heading = soup.find('h1', class_='summary-heading')
    if summary_heading:
        gene_info = summary_heading.text
        #print(summary_heading.text)
    else:
        print("Element not found")
    #print(gene_info)
    chromosome, range = gene_info.split(':')
    chromosome = chromosome.split(' ')[1]
    start,stop = range.split('-')
    parsed_start = start.replace(",","")
    parsed_stop = stop.replace(",","")
    start = int(parsed_start)
    stop = int(parsed_stop)
    #print(f' Chromosome is {chromosome}')
    #print(f'Position range is {range}')
    return chromosome, start, stop

def main_routine(infile, outfile):
    goi = pd.read_csv('genes_of_interest.csv')
    goi.columns = ["Label", "ID"]
    goi_data = goi["ID"].apply(fetch_position)
    goi_data = pd.DataFrame(data = goi_data.tolist(), columns=["Chromosome", "Start", "Stop"])
    goi_mapped = pd.concat([goi_data,goi], axis=1)
    goi_mapped.to_csv(outfile, sep=',')    
    return goi_mapped

# main_routine(infile='genes_of_interest.csv', outfile='mapped_goi.csv')
