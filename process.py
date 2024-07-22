# Python script for processing preliminary results
# A. Vargas Richards, 07.2024

import os, re, shutil
from tempfile import mkstemp

n = 10 # parameter should be set intelligently in future.

for i in range(1, n + 1):
    unified_dir = os.path.dirname(f'BLAST-results/unified_{i}.txt')
    os.makedirs(unified_dir, exist_ok=True)
    with open(f'BLAST-results/unified_{i}.txt', 'w') as unified_file:
        for blast_file in [f for f in os.listdir('.') if re.match(f'BLAST.*num{i}.*txt', f)]:
            with open(blast_file, 'r') as bf:
                shutil.copyfileobj(bf, unified_file)

search_pattern = re.compile(r'Query= (TraesCS[^ ]*)')

def clean_content(content):
    content = re.sub(r'<[^>]*>', '', content)
    content = content.replace('\r', '')
    return content

for root, _, files in os.walk('.'): # inefficient strategy
    for file in files:
        file_path = os.path.join(root, file)
        temp_fd, temp_path = mkstemp()

        with open(file_path, 'r') as f, os.fdopen(temp_fd, 'w') as temp_file:
            print(f'Opening file at {file_path}')
            content = f.read()
            cleaned_content = clean_content(content)
            temp_file.write(cleaned_content)

        with open(temp_path, 'r') as temp_file:
            for line in temp_file:
                match = search_pattern.search(line)
                if match:
                    new_name = match.group(1)
                    if new_name:
                        new_path = os.path.join(root, new_name)
                        os.rename(file_path, new_path)
                        print(f"Renamed {file_path} to {new_path}")
                    else:
                        print(f"No valid new name found in {file_path}")
                    break

        os.remove(temp_path)
