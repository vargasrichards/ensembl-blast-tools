# gets range of the full scaffold to which there was a map.
# Note that this may be significantly different from the length of the alignment against the query seq.
# Designed for use on the Ensembl plants web app.

# A. Vargas Richards, 21.07.2024

import requests # to get the necessary html content
from bs4 import BeautifulSoup # used to parse the html and select the important information.

def get_range(id): 
    url = 'https://plants.ensembl.org/Multi/Search/Results?species=all;idx=;q=' + str(id)
    html_content = requests.get(url).text # fetch the content
    soup = BeautifulSoup(html_content, 'html.parser') 
    twocol_div = soup.find('div', class_='twocol') # lines 14-19: some fairly messy HTML selection. Likely to be characteristic to the Ensembl plants platform.
    a_tag = twocol_div.find('a', href=lambda x: x and ':' in x) if twocol_div else None
    href_value = a_tag['href'] if a_tag else None
    pos_details = href_value.split('=')[1]
    id_verif, pos = (pos_details.split(';')[0]).split(':')
    start,stop = pos.split('-')
    assert id == id_verif, "ERROR: The output sequence identifier does not match the input sequence identifier." # added safety check to make sure correct seq retrieved
    print(f'Sequence {id_verif} starts at {start} and ends at {stop}')
    return start, stop, id_verif # return the start point, end point and id of the seq of interest. 

