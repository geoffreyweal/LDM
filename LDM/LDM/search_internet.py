"""
search_internet.py, 22/10/2022, Geoffrey R. Weal

This program is designed to search google scholar for literature.
"""

from bs4 import BeautifulSoup

from LDM.LDM.auxiliary_methods import wait, short_wait, get_source_data_from_firefox

def get_number_of_results_from_tewaharoa(sentence):
	"""
	This method is designe to determine the number of pages of results that were obtained.

	Parameters
	----------
	sentence : list of str.
		This is the list of the search sentence of interest.

	Results
	-------
	page_total_num : int
		This is the total number of pages of results obtained from Google Scholar.
	"""

	# First, get the content of the website
	URL_ori = 'https://tewaharoa.victoria.ac.nz/discovery/search?query=any,contains,'+'%20'.join(sentence)+'&tab=all&search_scope=MyInst_and_CI&vid=64VUW_INST:VUWNUI&offset=0'
	website = get_source_data_from_firefox(URL_ori, doing_what='search', waiting_time=1, dismiss_alert=True)

	# Second, locate the component of the website that will have the number of results.
	start_of_web_index = website.find('<span class="results-count">')
	end = website[start_of_web_index:].find('>Results<')
	section = website[start_of_web_index:start_of_web_index+end]

	# Third, obtain the part of the results that is the end of the number
	section_reverse = section[::-1]
	point = section_reverse.find(',')
	end_section = section[len(section) - point:]
	end_of_results = end_section.find('<')

	# Fourth, obtain the part of the results that is the start of the number
	section_reverse = section[0:len(section) - point:][::-1]
	start_of_results = section_reverse.find('>')

	# Fifth, obtain the number of results
	search_results_num = section[len(section) - point - start_of_results:len(section) - point + end_of_results]
	try:
		search_results_num = int(search_results_num.replace(',',''))
	except:
		print('Issue: Te Waharoa could not be loaded, give website longer to load')
		exit()
	# Sixth, get the number of pages
	page_total_num = int(search_results_num / 10) + 1

	# Fifth, return the total number of pages
	return page_total_num, search_results_num, URL_ori

# --------------------------------------------------------------------------------------------------
import re
suffix_link = '&context=PC&vid=64VUW_INST:VUWNUI&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=all&query=any,contains,NOTHING_HERE&facet=rtype,exclude,newspaper_articles&facet=rtype,exclude,reviews&offset=0'
suffix_link_1 = '&context=PC&vid=64VUW_INST:VUWNUI&lang=en&search_scope=MyInst_and_CI&adaptor=Primo Central&tab=all&query=any%2Ccontains%2CAnna%20Garden&facet=rtype%2Cexclude%2Cnewspaper_articles&facet=rtype%2Cexclude%2Creviews&offset=0'
suffix_link_2 = '&facet=rtype,exclude,newspaper_articles&facet=rtype,exclude,reviews&offset=0'

#https://tewaharoa.victoria.ac.nz/discovery/fulldisplay?docid=cdi_acs_journals_10_1021_acscatal_5b01918&context=PC&vid=64VUW_INST:VUWNUI&lang=en&search_scope=MyInst_and_CI&adaptor=Primo Central&tab=all&query=any%2Ccontains%2CAnna%20Garden&facet=rtype%2Cexclude%2Cnewspaper_articles&facet=rtype%2Cexclude%2Creviews&offset=0
def scrap_tewaharoa_for_literature(URL_ori, page_num, get_DOI=False):
	"""
	This method is designed to scrap the literature results from Google Scholar.

	Parameters
	----------
	URL_ori : str.
		This is the google scholar URL to search.
	page_num : int
		This is the search page number to look at.

	Results
	-------
	literature_results : list
		This is the list of results obtained from scrapping results for this page number.
	"""

	# First, get the URL page to load
	URL_edit = URL_ori.replace('offset=0','offset='+str((page_num-1)*10))

	# Second, grab the results from the website from opening firefox
	website = get_source_data_from_firefox(URL_edit, doing_what='search', waiting_time=5, dismiss_alert=True)

	# Third, convert website into object-oriented format.
	soup = BeautifulSoup(website, "html.parser")
	results = soup.find("div", id="searchResultsContainer")

	# Fourth, extract the literature data from this Google Scholar page
	literature_results = []
	job_elements = results.find_all("div", class_="list-item-wrapper")
	for job_element in job_elements:

		# 4.1: Get the title of the literature
		title = job_element.find("h3")
		title = str(title)
		title_reverse = title[::-1]
		end_point = title_reverse.find('</span><!-- --></prm-highlight>'[::-1]) + len('</span><!-- --></prm-highlight>')
		scanning_title_reverse = title_reverse[end_point:]
		start_point = 0
		while True:
			scanning_start_point = scanning_title_reverse.find('>')
			start_point += scanning_start_point
			if (scanning_title_reverse[scanning_start_point:scanning_start_point+6] == '>kram<'):
				start_point += len('>kram<')
				scanning_title_reverse = scanning_title_reverse[scanning_start_point+len('>kram<'):]
			elif (scanning_title_reverse[scanning_start_point:scanning_start_point+7] == '>kram/<'):
				start_point += len('>kram/<')
				scanning_title_reverse = scanning_title_reverse[scanning_start_point+len('>kram/<'):]
			else:
				break

		title = str(title_reverse[end_point:end_point+start_point:][::-1])
		title = title.replace('<mark>','').replace('</mark>','')

		# 4.2: Get the doi for this literature
		if get_DOI:
			info_page = job_element.find("h3")
			info_page = info_page.find("a")
			info_page = str(info_page)
			
			indices_object = re.finditer(pattern='ng-href="https://tewaharoa.victoria.ac.nz/discovery/fulldisplay?', string=info_page)
			indices = [index.start() for index in indices_object]

			for start_of_web_index in indices:
				end_of_web_index = info_page[start_of_web_index+len('ng-href="'):].find('&amp;')
				info_page_orig = info_page[start_of_web_index+len('ng-href="'):start_of_web_index+len('ng-href="')+end_of_web_index]
				info_page_full = info_page_orig + suffix_link_1
				found_info_webpage = True
				break
			else:
				found_info_webpage = False

			if found_info_webpage:
				info_website = get_source_data_from_firefox(info_page_full, doing_what='doi', waiting_time=5, dismiss_alert=True)
				soup = BeautifulSoup(info_website, "html.parser")
				details = soup.find("div", id="details")
				details = str(details)
				doi_point = details.find('>DOI: ')
				DOI_value = details[doi_point+len('>DOI: ')::]
				doi_end_point = DOI_value.find('<')
				DOI_value = DOI_value[:doi_end_point:]
			else:
				DOI_value = None
		else:
			DOI_value = None

		# 4.3: Get the PDF link to get the literature resource.
		direct_pdf_download_tewaharoa = str(job_element)
		start_of_web_index = direct_pdf_download_tewaharoa.find('https://libkey.io/libraries')
		end_of_web_index = direct_pdf_download_tewaharoa[start_of_web_index:].find('"')
		pdf_link = direct_pdf_download_tewaharoa[start_of_web_index:start_of_web_index+end_of_web_index]

		# 4.3: If a PDF link is given, record this link
		#if not len(pdf_link) == 0:
		literature_results.append((title, pdf_link, DOI_value))


	# Fifth, return finished_scrap and literature_results
	return literature_results



