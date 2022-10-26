"""
auxiliary_methods.py, 22/10/2022, Geoffrey R. Weal

This programs contain general methods that are use across the LDM program
"""

import os
from random import randrange
from time   import sleep
from tqdm   import trange

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchWindowException, NoAlertPresentException, UnexpectedAlertPresentException

def wait():
	"""
	This method is designed to allow the program to wait for a few seconds.
	"""
	#print("Waiting for a few secs...")
	sleep(randrange(10, 30))
	#print("Waiting done. Continuing...\n")

def short_wait():
	"""
	This method is designed to allow the program to wait for a few seconds.
	"""
	#print("Waiting for a few secs...")
	sleep(randrange(1, 6))
	#print("Waiting done. Continuing...\n")

def timer(time_to_wait):
	print('Waiting '+str(time_to_wait)+' seconds')
	for _ in trange(time_to_wait):
		sleep(1)

def get_source_data_from_firefox(URL_address, doing_what, waiting_time=5, dismiss_alert=True):
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

	# First, load firefox
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #, firefox_options=options)

	# Second, open the tewaharoa website
	driver.get(URL_address)

	# Third, check to see if any alerts popped up when loading the page
	alert = Alert(driver)
	try:
		alert.text
		alert_exists = True
	except (NoSuchWindowException, NoAlertPresentException, UnexpectedAlertPresentException): 
		alert_exists = False

	if alert_exists:
		if dismiss_alert:
			alert.dismiss()
		else:
			print('NOTICE: Firefox presented an alert that poped up when loading this page')
			print(alert.text)
			print('Either cancel this popup or deal with it in the Firefox Browser')
			input("Then press Enter to continue...")

	# Fourth, minimise the window and wait.
	#driver.minimize_window()

	# Fifth, check to see if the page has loaded
	if doing_what == 'search':
		while True:
			sleep(waiting_time)

			# 5.1: Gather the content from the website and close the browser
			while True:
				try:
					website = driver.page_source
					break
				except:
					try:
						alert = Alert(driver)
						alert.dismiss()
					except:
						pass
					print('waiting')
					sleep(waiting_time)

			try:
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
			except:
				try:
					alert = Alert(driver)
					alert.dismiss()
				except:
					pass
				print('waiting')
				sleep(waiting_time)


			# Fifth, obtain the number of results
			search_results_num = section[len(section) - point - start_of_results:len(section) - point + end_of_results]
			try:
				search_results_num = int(search_results_num.replace(',',''))
				break
			except:
				try:
					alert = Alert(driver)
					alert.dismiss()
				except:
					pass
				print('waiting')
				sleep(waiting_time)

	elif doing_what == 'doi':
		import pdb; pdb.set_trace()

	driver.close()

	# Fourth, return the content from the website
	return website





