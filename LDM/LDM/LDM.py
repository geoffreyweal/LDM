"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import os, shutil
from time import sleep
from tqdm import tqdm

#from LDM.Programs.search_internet   import get_number_of_results_from_google_scholar, scrap_google_scholar_for_literature
from LDM.Programs.search_internet   import get_number_of_results_from_tewaharoa, scrap_tewaharoa_for_literature
from LDM.Programs.download_pdf      import download_pdf
from LDM.Programs.highlight_pdf     import highlight_pdf
from LDM.Programs.auxiliary_methods import wait, timer

def LDM(searches, search_type='Google Scholar'):
	"""
	This method will perform the tasks needed for literature data mining

	Parameters
	----------
	searches : list of str.
		This is a list of all the searches you would like to perform. 
	"""

	# First: Determine how information about searches will be perform
	if search_type == 'Google Scholar':
		get_number_of_results = get_number_of_results_from_google_scholar
		scrap_for_literature  = scrap_google_scholar_for_literature
	elif search_type == 'VUW':
		get_number_of_results = get_number_of_results_from_tewaharoa
		scrap_for_literature  = scrap_tewaharoa_for_literature
	else:
		exit('search must be either:')

	# Second: Get all the keywords from the search
	all_keywords = []
	for search in searches:
		keywords = search.split()
		for keyword in keywords:
			if not (keyword in all_keywords):
				all_keywords.append(keyword)

	# Second: Determine the number of search results.
	print('------------------------------------------------')
	print('Prelim Step: Gathering data about searches'.upper()+'\n')
	URL_inputs = []
	for search in searches:
		print('Gathering search data on: '+str(search))
		sentence = [word.lower() for word in search.split()]
		page_total_num, search_results_num, URL_input = get_number_of_results(sentence)
		URL_inputs.append([search, URL_input, page_total_num, 0])
		print(f"Total page number: {page_total_num}")
		print(f"Total search results: {search_results_num}\n")

	literature_url_filename = 'literature_urls.txt'
	if os.path.exists(literature_url_filename):
		os.remove(literature_url_filename)
	with open(literature_url_filename,'w') as FILE:
		pass

	could_not_download_literature_urls_filename = 'could_not_download_literature_urls.txt'
	if os.path.exists(could_not_download_literature_urls_filename):
		os.remove(could_not_download_literature_urls_filename)
	with open(could_not_download_literature_urls_filename,'w') as FILE:
		pass

	other_literature_filename = 'other_literature.txt'
	if os.path.exists(other_literature_filename):
		os.remove(other_literature_filename)
	with open(other_literature_filename,'w') as FILE:
		pass

	path_loc = os.path.join(os.getcwd(), 'Literature_PDFs')
	literature_pdf_folder = 'Literature_PDFs'
	if os.path.exists(literature_pdf_folder):
		shutil.rmtree(literature_pdf_folder)
	os.makedirs(literature_pdf_folder)

	# Second: Peform lituerature data mining
	print('------------------------------------------------')
	print('Main Step: Literature Data Mining'.upper()+'\n')
	all_literature_results = []
	search_index = 0
	download_and_highlight_start_index = 0
	while True:

		# Third: Perform as much scrapping as possible before Google prevents this momentarily

		# 3.1: Get URL info
		search, URL_input, page_total_num, page_num = URL_inputs[search_index]
		page_num_up = page_num + 1
		print('Looking at Search: '+str(search)+'; Page: '+str(page_num_up))

		# 3.2: Scrap Google Scholar data.
		literature_results = scrap_for_literature(URL_input, page_num_up, get_DOI=False)

		# 3.3.1: Append URL to all_literature_results list if it is not already in the list.
		pbar = tqdm(literature_results)
		for title, link_url, doi in pbar:

			# First, save the details on disk.
			if (link_url is None) or (len(link_url) == 0) or link_url.isspace():
				with open(other_literature_filename,'a') as FILE:
					FILE.write(str(title)+'\n')
			else:
				with open(literature_url_filename,'a') as FILE:
					if doi is None:
						FILE.write(str(title)+' --> '+str(link_url)+'\n')
					else:
						FILE.write(str(title)+' ('+str(doi)+') --> '+str(link_url)+'\n')

				# Second, make a note of this url so as to not download it again.
				pbar.set_description('Downloading: '+str(title))
				if not link_url in all_literature_results:
					all_literature_results.append(link_url)

				# Third, save the pdf for this entry if possible. 
				downloading_complete, filename = download_pdf(link_url, title, path_loc, waiting_time=1)
				
				# Fourth, highlight the keywords of interest in this pdf.
				if downloading_complete:
					highlight_pdf(filename, path_loc, all_keywords)
					os.rename(path_loc+'/'+filename, path_loc+'/'+filename.replace('_', ' '))
				else: 
					with open(could_not_download_literature_urls_filename,'a') as FILE:
						if doi is None:
							FILE.write(str(title)+' --> '+str(link_url)+'\n')
						else:
							FILE.write(str(title)+' ('+str(doi)+') --> '+str(link_url)+'\n')

		pbar.set_description('Finished Downloading PDFs.')
		sleep(1)
		pbar.close()

		# 3.3.2: Update the page number to obtain data from
		URL_inputs[search_index][3] += 1

		# 3.3.3: Update the search index number
		search_index += 1
		if search_index == len(URL_inputs):
			search_index = 0
		




