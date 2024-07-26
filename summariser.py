# Extracts the overview of results against a query seq
# A. Vargas Richards, 22.07.2024

import pandas as pd, os

def overview(file):
    print(f'File tuple is {file}')
    parent_directory, filename = file.split('/')
    summary_file = str('summary' + filename)
    # file = str(parent_directory + '/' + summary_file)
    with open(file, 'r') as input:
        with open(str(parent_directory + '/' + summary_file), 'w') as summary:
            for line in input:
                if line[0] == 'E' and line[1] == 'G':
                    print(line)
                    summary.write(line)

    return

def summarise_all(directory):
    for (root,dirs,files) in os.walk(directory, topdown=True):
        print (f'Root is {root}')
        print (f'Dirs is {dirs}')
        print (f'files is {files}')
        print ('--------------------------------')
    return 

def parse_summary(summary_file): # reads in the summary file and converts it to a pandas dataframe which is more easily manipulated.
    summary_table = pd.DataFrame(columns=["Variety", "Identifier", "Score", "E-value"])
    with open(summary_file) as summary:
        for line in summary:
            #print(f"Line split 0 is {line.split(' ')[0]}")
            #print(f"Line split 1 is {line.split(' ')[1]}")
            #print(f"Number of values to unpack is {line.split('  ')}")
            variety = line.split(' ')[0]
            scaff_id = variety.split(':')[1]
            variety_name = scaff_id.split('_')[0]
            score = line.split(' ')[4]
            Eval = line.split(' ')[7]
            row = pd.DataFrame(data=[variety_name, scaff_id, score, Eval])
            summary_table = pd.concat([summary_table, row])
    print(f"Summary table computed as \n{summary_table}")
    return summary_table

#-----------------------------------------------
#test_file = 'BLAST-results/TraesCS5B02G153200'
#overview(test_file)
#parse_summary('BLAST-results/summaryTraesCS5B02G153200')

# def detect_differential(summary_table, filter_condition): # detects the 
