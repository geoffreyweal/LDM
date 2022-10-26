"""
LDM.py, 22/10/2022, Geoffrey R. Weal

This program is designed to perform Literature data mining. This program is designed to

1. Scrap literature search websites like Google Scholar for literature.
2. Download the papers for those literatures as PDFs
3. Highlight relavant text in those PDFs

This program uses the `ScrapPaper` program that were originally developed by M. R. Rafsanjani. See https://github.com/rafsanlab/ScrapPaper and https://doi.org/10.1101/2022.03.08.483427

"""

import os
from time import sleep, time

from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

time_limit = 60.0
def download_pdf(URL_address, file_name, path_loc, waiting_time=10):
	"""
	This method will open a firefox web browser and collect the full content from the site.

	Parameters
	----------
	URL_address : str.
		This is the tewaharoa URL to search.

	Results
	-------
	website : string
		This is the content of the website
	"""

	# First, determine the number of files currently in the liteature pdf folder
	original_files = os.listdir(path_loc)
	original_number_of_files = len(original_files)

	# Second, load the Chrome driver
	options = ChromeOptions()
	chrome_prefs = {
	    "download.prompt_for_download": False,
	    "plugins.always_open_pdf_externally": True,
	    "download.open_pdf_in_system_reader": False,
	    "profile.default_content_settings.popups": 0,
	    "download.default_directory": path_loc
	}
	options.add_experimental_option("prefs", chrome_prefs)
	driver = Chrome(ChromeDriverManager().install(), options=options)

	# Third, load the webpage to download the pdf
	driver.get(URL_address)

	# Fourth, wait until the pdf file has downloaded
	finished = False
	intial_time = time()
	while ((time() - intial_time) <= time_limit):
		try:
			while ((time() - intial_time) <= time_limit):
				if len(os.listdir(path_loc)) > original_number_of_files:
					break
				sleep(1)
			while ((time() - intial_time) <= time_limit):
				for file in os.listdir(path_loc):
					if file.endswith('.crdownload'):
						break
				else:
					break
			finished = True
		except:
			try:
				alert = Alert(driver)
				alert.dismiss()
			except:
				pass
			print('waiting')
			sleep(waiting_time)
		if finished:
			break
	
	if ((time() - intial_time) <= time_limit):

		# Fifth, wait for a bit and then close the driver
		sleep(1)
		driver.close()

		# Sixth, rename the pdf file.
		original_filename = tuple(set(os.listdir(path_loc)) - set(original_files))
		if not (len(original_filename) == 1):
			exit('issue, new pdf files: '+str(original_filename))
		original_filename = original_filename[0]
		split_title = []
		for e in file_name:
			if e.isalnum():
				split_title.append(e)
			else:
				split_title.append('_')
		split_title = ''.join(split_title)
		split_title = [word for word in split_title.split('_') if (len(word) > 0)]
		new_filename = '_'.join(split_title)+'.pdf'
		os.rename(path_loc+'/'+original_filename, path_loc+'/'+new_filename)

		# Seventh, return pdf filename
		return True, new_filename

	else:

		original_filenames = tuple(set(os.listdir(path_loc)) - set(original_files))
		for original_filename in original_filenames:
			os.remove(path_loc+'/'+original_filename)

		driver.close()

		return False, None


