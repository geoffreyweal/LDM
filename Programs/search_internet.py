"""
search_internet.py, 22/10/2022, Geoffrey R. Weal

This program is designed to search google scholar for literature.
"""

import re
import requests
from bs4 import BeautifulSoup

def get_data_about_google_scholar_search(URL_input):
	"""
	This method is designe to determine the number of pages of results that were obtained.

	Parameters
	----------
	URL_input : str.
		This is the google scholar URL to search.

	Results
	-------
	page_total_num : int
		This is the total number of pages of results obtained from Google Scholar.
	"""

	# First, get the URL to load
	page_num = 0
	URL_edit = str(URL_ori + "&start=" + str(page_num))

	try:

		# Second, load the google scholar page and extract the information from it
		page = requests.get(URL_edit, headers=headers, timeout=None)
		soup = BeautifulSoup(page.content, "html.parser")
		wait()
		general_search_results = soup.find_all("div", class_="gs_ab_mdw")
		print(general_search_results)
		search_results = general_search_results[1].text

		# Third, obtain the general search data, including total number of pages with results.
		if "About" in search_results:
			search_results_split = search_results.split("results")[0].split("About")[1]
		elif "results" in search_results:
			search_results_split = search_results.split("results")[0]
		else:	
			search_results_split = search_results.split("result")[0]

	except AttributeError:

		print("Opss! ReCaptcha is probably preventing the code from running.")
		print("Please consider running in another time.\n")
		return

	# Fourth, obtain the total number of pages
	search_results_num = int(''.join(filter(str.isdigit, search_results_split)))
	page_total_num = int(search_results_num / 10) + 1
	print(f"Total page number: {page_total_num}")
	print(f"Total search results: {search_results_num}.\n")
	wait()

	# Fifth, return the total number of pages
	return page_total_num, page_num

def scrap_google_scholar_for_literature(URL_ori, page_num):
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
	finished_scrap : bool.
		This indicates if the scrapping worked. If not, will need to wait a bit before continuing.
	literature_results : list
		This is the list of results obtained from scrapping results for this page number.
	"""

	# First, get the URL page to load
	print(f"Going to page {page_num_up}.\n")
	URL_edit = str(URL_ori + "&start=" + str(page_num_up) + "0")

	# Second, load the google scholar page and extract the information from it
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'Mozilla/15.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20210916 Firefox/95.0'})
	page = requests.get(URL_edit, headers=headers, timeout=None)
	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find("div", id="gs_res_ccl_mid")
	wait()

	# Third, extract the literature data from this Google Scholar page
	literature_results = []
	finished_scrap = False
	try:
		job_elements = results.find_all("div", class_="gs_ri")
		for job_element in job_elements:
			ref_element = job_element.find("div", class_="gs_a").text
			links = job_element.find("a") 
			link_url = links["href"]
			title_element = links.text.strip()
			print(title_element)
			print(link_url)
			print(ref_element)
			print()
			literature_results.append((title_element, link_url, ref_element))
		finished_scrap = True
	except AttributeError:
		print("Opss! ReCaptcha is probably preventing the code from running.")
		print("Please consider running in another time.\n")
		break

	# Fourth, return finished_scrap and literature_results
	return finished_scrap, literature_results




