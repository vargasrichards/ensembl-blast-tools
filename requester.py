import requests, os, math, time

# seqids = pd.read_csv("gene_ids")
# https://plants.ensembl.org/Triticum_aestivum_robigus/Download/Tools/Blast?tl=dH2MUh3d5qVTSKJc-23302406
# https://plants.ensembl.org/Triticum_aestivum_robigus/Download/Tools/Blast?tl=dH2MUh3d5qVTSKJc-23302378

# there have been issues with the requester in the past with HTML content being introduced

def fetch_blast(varieties, species, batch_id, first, last):
	print(f'Fetching BLAST for {varieties} of {species} with batch ID {batch_id} from job {first} to job {last}')
	num_varieties = len(varieties)
	#print(f'Number of varieties calculated as {num_varieties}')
	pos = 0
	status = 1
	# os.mkdir('') # could make a parent directory to make clearing files easier.
	os.mkdir(str('BLAST-' + str(varieties[0])))
	cnt = 1
	for id in range(first, last):
		pos_old = pos
		pos = math.floor(num_varieties*((id-first)/(last-first)))
		variety = varieties[pos]
		if pos != pos_old:
			os.mkdir(str('BLAST-') + variety)
			cnt = 1
		# print(f'pos is {pos}')
		# print(f'variety  = {variety}')
		specifier = str(species + str(variety))
		ext = "https://plants.ensembl.org/" + specifier + "/Download/Tools/Blast?tl=" + str(batch_id) + '-' + str(id)
		try:
			r = requests.get(ext)
			status = 0
		except:
			status = 1
		while status != 0:
			r.raise_for_status()
			time.sleep(.2)
			print('Retrying URL...')
			try:
				r = requests.get(ext)
				status = 0
			except:
				status = 1
		results_file = str('./' + str('BLAST-' + variety) + '/' + 'num' + str(cnt) + '_' + str(id) + '.txt') 
		with open(results_file, 'w') as f:
			for line in r.text.splitlines():
				print(line)
				if filter_line(line) == 0:
					f.write(line + '\n')
			#f.writelines(r.text)
		cnt += 1
	return

def filter_line(line): # filters lines which are suspected to be HTML
    html_tags = ['<', '!', 'src', 'script', '{', '}']
    if any(tag in line for tag in html_tags):
        print('HTML detected')
        return 1
    else:
        return 0

