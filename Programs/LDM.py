"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

try:
	from LDM.Programs.search_internet   import get_data_about_google_scholar_search, scrap_google_scholar_for_literature
	from LDM.Programs.auxiliary_methods import wait
except:
	from search_internet   import get_data_about_google_scholar_search, scrap_google_scholar_for_literature
	from auxiliary_methods import wait

def LDM(searches):
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
		finished_successfully, page_total_num, page_num, search_results_num = get_data_about_google_scholar_search(URL_input)
		if not finished_successfully:
			print("\nOpss! ReCaptcha is probably preventing the code from running.")
			print("Please wait a minute and then run this program again.")
			print('Program will now finish')
			return
		URL_inputs.append([search, URL_input, page_total_num, page_num])
		print(f"Total page number: {page_total_num}")
		print(f"Total search results: {search_results_num}.\n")

	# Second: Peform lituerature data mining
	print('------------------------------------------------')
	print('Main Step: Literature Data Mining'.upper()+'\n')
	all_literature_results = []
	search_index = 0

	temp_counter = 0

	while True:
		# Third: Perform as much scrapping as possible before Google prevents this momentarily
		while True:

			# 3.1: Get URL info
			search, URL_input, page_total_num, page_num = URL_inputs[search_index]
			page_num_up = page_num + 1
			print('Looking at Search: '+str(search)+'; Page: '+str(page_num_up))

			# 3.2: Scrap Google Scholar data.
			finished_scrap, literature_results = scrap_google_scholar_for_literature(URL_input, page_num_up)
			title_element, link_url, ref_element = literature_results

			# 3.3: Append URL to all_literature_results list if it is not already in the list.
			if not link_url in all_literature_results:
				all_literature_results.append(link_url)

			if finished_scrap:
				URL_inputs[search_index][3] += 1
			else:
				break

			search_index += 1
			if search_index == len(URL_inputs):
				search_index = 0

			temp_counter +=1
			if temp_counter == 6:
				import pdb; pdb.set_trace()

		# Fourth: While we need to wait for Google to let us scrap, download PDF of literature.

		# Perform higlighting

		print('halt moment')
		import pdb; pdb.set_trace()





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






