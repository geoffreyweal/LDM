"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import csv


import pandas as pd

import time
from LDM.Programs.search_internet import get_data_about_google_scholar_search

# ===== DEFINE GENERAL FUNCTIONS =====

search_from, URL_edit= "", ""

def wait():
	print("Waiting for a few secs...")
	time.sleep(4)
	print("Waiting done. Continuing...\n")

# ------------------------------------------

def LDM(searches):
	"""
	This method will perform the tasks needed for literature data mining

	Parameters
	----------
	searches : list of str.
		This is a list of all the searches you would like to perform. 
	"""

	URL_inputs = []
	for search in searches:
		sentence = [word.lower() for word in search.split()]
		URL_input = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+'+'.join(sentence)+'&btnG='

		page_total_num, page_num = get_data_about_google_scholar_search(URL_input)

		URL_inputs.append([URL_input, page_total_num, page_num])

	all_literature_results = []

	search_index = 0

	while True:

		# Perform Scrap
		while True:

			URL_input, page_total_num, page_num = URL_inputs[search_index]

			page_num_up = page_num + 1

			finished_scrap. literature_results = scrap_google_scholar_for_literature(URL_input, page_num_up)

			all_literature_results.append(literature_results)

			if finished_scrap:

				URL_inputs[index1][2] += 1

			search_index += 1
			if search_index == len(URL_inputs):
				search_index = 0

		# Perform download

		# Perform higlighting



'''

	for i in range(page_total_num):

		page_num_up = page_num + i

		scrap_google_scholar_for_literature(URL_input, page_num_up)



'''







'''

	# SETTING UP THE CSV FILE

	outfile = open("scrapped_gscholar.csv","w",newline='',encoding='utf-8')
	writer = csv.writer(outfile)
	df = pd.DataFrame(columns=['Title','Links','References'])

	# SETTING & GETTING PAGE NUMBER

				df2 = pd.DataFrame([[title_element, link_url, ref_element]], columns=['Title','Links','References'])
				df = pd.concat([df, df2], ignore_index=True)

	print("Saving results.\n")
	df.index += 1
	df.to_csv('scrapped_gscholar.csv',encoding='utf-8')
	outfile.close()





'''






