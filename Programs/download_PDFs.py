"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import requests
from HTMLParser import HTMLParser

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/15.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20210916 Firefox/95.0'})

def download_pdf(url, file_name, headers):
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)



def get_pdf_from_acs(input_URL):
	output_URL = input_URL.replace('full','pdf')
	return output_URL

def get_pdf_from_rsc(input_URL):
	output_URL = input_URL.replace('articlehtml','articlepdf')
	return output_URL

def get_pdf_from_sciencedirect(input_URL):

	page = requests.get(input_URL, headers=headers, timeout=None)
	soup = BeautifulSoup(page.content, "html.parser")

	soup.find('umsdataelement',{'class':'data'}).text

	soup.find('umsdataelement').text


	return 