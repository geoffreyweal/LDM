"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import requests
import csv
import re
import random
import time
import pandas as pd
from sys import exit
from bs4 import BeautifulSoup

# ===== DEFINE GENERAL FUNCTIONS =====

search_from, URL_edit= "", ""

def wait():
	print("Waiting for a few secs...")
	time.sleep(random.randrange(1, 6))
	print("Waiting done. Continuing...\n")

# ------------------------------------------

URL_input = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=anna+garden&btnG='

def get_data_about_google_scholar_search(URL_input):

	page_num = 0
	URL_edit = str(URL_ori + "&start=" + str(page_num))

	try:

		page = requests.get(URL_edit, headers=headers, timeout=None)
		soup = BeautifulSoup(page.content, "html.parser")
		wait()

		general_search_results = soup.find_all("div", class_="gs_ab_mdw")
		print(general_search_results)

		search_results = general_search_results[1].text

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

	search_results_num = int(''.join(filter(str.isdigit, search_results_split)))
	page_total_num = int(search_results_num / 10) + 1
	print(f"Total page number: {page_total_num}")
	print(f"Total search results: {search_results_num}.\n")

	wait()

	return page_total_num, page_num



def scrap_google_scholar_for_literature(URL_input, page_total_num, page_num):

	literature_results = []

	page_num = 0
	for i in range(page_total_num):

		page_num_up = page_num + i
		print(f"Going to page {page_num_up}.\n")
		URL_edit = str(URL_ori + "&start=" + str(page_num_up) + "0")

		headers = requests.utils.default_headers()
		headers.update({'User-Agent': 'Mozilla/15.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20210916 Firefox/95.0'})
		
		page = requests.get(URL_edit, headers=headers, timeout=None)
		soup = BeautifulSoup(page.content, "html.parser")
		wait()

		results = soup.find("div", id="gs_res_ccl_mid")

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

		except AttributeError:
			print("Opss! ReCaptcha is probably preventing the code from running.")
			print("Please consider running in another time.\n")
			break

	return literature_results






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



def LDM(searches):
	"""
	This method will perform the tasks needed for literature data mining

	Parameters
	----------
	searches : list of str.
		This is a list of all the searches you would like to perform. 
	"""

	



















