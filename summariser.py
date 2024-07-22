# Extracts the overview of results against a query seq
# A. Vargas Richards, 22.07.2024

def overview(file):
    parent_directory, filename = file.split('/')
    summary_file = str('summary' + filename)
    #file = str(parent_directory + '/' + summary_file)
    with open(file, 'r') as input:
        with open(str(parent_directory + '/' + summary_file), 'w') as summary:
            for line in input:
                if line[0] == 'E' and line[1] == 'G':
                    summary.write(line)

    return

overview('BLAST-results/TraesCS5B02G153200')