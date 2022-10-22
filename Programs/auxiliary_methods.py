"""
auxiliary_methods.py, 22/10/2022, Geoffrey R. Weal

This programs contain general methods that are use across the LDM program
"""

import time, random

def wait():
	"""
	This method is designed to allow the program to wait for a few seconds.
	"""
	#print("Waiting for a few secs...")
	time.sleep(random.randrange(1, 6))
	#print("Waiting done. Continuing...\n")