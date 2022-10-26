'''
run.py, Geoffrey Weal, 26/10/2022

This program will allow the user to perform a literature mining task
'''
import os

from LDM.LDM.LDM import LDM

class CLICommand:
	"""Will run the literature mining task.
	"""

	@staticmethod
	def add_arguments(parser):
		pass
	
	@staticmethod
	def run(args):
		Run_method()

def Run_method(time_between_250_cancels=60):
	"""
	This method will run the literature mining task.
	"""

	# First, get the current path
	path = os.getcwd()

	# Second, check if the search_keyword_filename file exists
	search_keyword_filename = 'searches.txt'
	if not os.path.exists(search_keyword_filename):
		print('Error running the LDM')
		print('You need a "searches.txt" file that contains all the search phrases you would like this programs to search for.')
		exit('This program will exit without beginning.')

	# Third, gather all the search phrases from the search_keyword_filename file. 
	searches = []
	with open(path+'/'+search_keyword_filename) as FILE:
		for line in FILE:
			search = line.rstrip()
			searches.append(search)

	# Fourth, run the Literature Data Mining (LDM) Program
	LDM(searches, search_type='VUW')