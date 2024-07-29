# Extracts the overview of results against a query seq
# A. Vargas Richards, 22.07.2024

import pandas as pd, os

def summarise(file):
    #print(f'File tuple is {file}')
    #parent_directory, filename = file.split('/')
    summary_file = str('summary' + file)
    file = str('BLAST-results' + '/' + file)
    with open(file, 'r') as input:
        with open(str('BLAST-results' + '/' + summary_file), 'w') as summary:
            for line in input:
                if line[0] == 'E' and line[1] == 'G':
                    print(line)
                    summary.write(line)
    return

def summarise_all(directory):
    for root,dirs,files in os.walk(directory, topdown=True):
        for file in files:
            summarise(file)
    return 

def tabulate(summary_file): # produces a sorted table of the results
    summary_table = pd.DataFrame(columns=["Variety", "Identifier", "Score", "E-value"])
    
    with open(summary_file) as summary:
        for line in summary:
            parts = [part for part in line.split(' ') if part]
            #print(parts)
            variety = parts[0]
            scaff_id = variety.split(':')[1]
            variety_name = scaff_id.split('_')[0]
            score = parts[3]
            eval = str(parts[4]).replace('\n','')
            row = pd.DataFrame([[variety_name, scaff_id, score, eval]], 
                               columns=["Variety", "Identifier", "Score", "E-value"])
            summary_table = pd.concat([summary_table, row], ignore_index=True)

    sorted_summary = summary_table.sort_values("E-value") # sort by E_values
    os.makedirs('CSVs', exist_ok=True)  
    csv_name = 'CSVs/' + summary_file + '.csv'
    sorted_summary.to_csv(csv_name)  
    #print(sorted_summary)
    return sorted_summary


def tabulate_all(directory):
    for root,dirs,files in os.walk(directory, topdown=True):
        for file in files:
            if 'summary' in file: # checking for the correct file type...
                tabulate(file)
    return 

#-----------------------------------------------
#test_file = 'BLAST-results/TraesCS5B02G153200'
#overview(test_file)
#tabulate('BLAST-results/summaryTraesCS5B02G153200')

# def detect_differential(summary_table, filter_condition): # detects the 
