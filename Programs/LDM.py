"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import os
from time import sleep
from tqdm import trange

import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/15.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20210916 Firefox/95.0'})

try:
	from LDM.Programs.search_internet   import get_data_about_google_scholar_search, scrap_google_scholar_for_literature
	from LDM.Programs.download_PDFs     import download_pdf
	from LDM.Programs.auxiliary_methods import wait
except:
	from search_internet   import get_data_about_google_scholar_search, scrap_google_scholar_for_literature
	from download_PDFs     import download_pdf
	from auxiliary_methods import wait

def LDM_Part_1(searches):
	"""
	This method will perform the tasks needed for literature data mining

	Parameters
	----------
	searches : list of str.
		This is a list of all the searches you would like to perform. 
	"""

	# First: Gathering information about searches to perform
	print('------------------------------------------------')
	print('Prelim Step: Gathering data about searches'.upper()+'\n')
	URL_inputs = []
	for search in searches:
		print('Gathering search data on: '+str(search))
		sentence = [word.lower() for word in search.split()]
		URL_input = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+'+'.join(sentence)+'&btnG='
		while True:
			finished_successfully, page_total_num, page_num, search_results_num = get_data_about_google_scholar_search(URL_input)
			if not finished_successfully:
				print("\nOpss! ReCaptcha is probably preventing the code from running.")
				print('Will wait a minute and then try again')
				timer(60)
				print('Will try again\n')
			else:
				break
		URL_inputs.append([search, URL_input, page_total_num, page_num])
		print(f"Total page number: {page_total_num}")
		print(f"Total search results: {search_results_num}.\n")

	literature_url_filename = 'literature_urls.txt'
	if os.path.exists(literature_url_filename):
		os.remove(literature_url_filename)
	with open(literature_url_filename,'w') as FILE:
		pass

	# Second: Peform lituerature data mining
	print('------------------------------------------------')
	print('Main Step: Literature Data Mining'.upper()+'\n')
	all_literature_results = []
	search_index = 0
	download_and_highlight_start_index = 0

	temp_counter = 0

	while True:

		# Third: Perform as much scrapping as possible before Google prevents this momentarily

		# 3.1: Get URL info
		search, URL_input, page_total_num, page_num = URL_inputs[search_index]
		page_num_up = page_num + 1
		print('Looking at Search: '+str(search)+'; Page: '+str(page_num_up))

		# 3.2: Scrap Google Scholar data.
		finished_scrap, literature_results = scrap_google_scholar_for_literature(URL_input, page_num_up)

		if finished_scrap:

			# 3.3.1: Append URL to all_literature_results list if it is not already in the list.
			for title_element, link_url, ref_element in literature_results:
				if not link_url in all_literature_results:
					all_literature_results.append(link_url)
					with open(literature_url_filename,'a') as FILE:
						FILE.write(link_url+'\n')

			# 3.3.2: Update the page number to obtain data from
			URL_inputs[search_index][3] += 1

			# 3.3.3: Update the search index number
			search_index += 1
			if search_index == len(URL_inputs):
				search_index = 0
		
		else:
			
			# 3.3.4: Wait a bit of time as time needed
			print("\nOpss! ReCaptcha is probably preventing the code from running.")
			print('Will wait a minute and then try again')
			timer(60)
			print('Will try again\n')




