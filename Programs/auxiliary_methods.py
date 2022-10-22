"""
auxiliary_methods.py, 22/10/2022, Geoffrey R. Weal

This programs contain general methods that are use across the LDM program
"""

import random
from time import sleep

def wait():
	"""
	This method is designed to allow the program to wait for a few seconds.
	"""
	#print("Waiting for a few secs...")
	sleep(random.randrange(1, 6))
	#print("Waiting done. Continuing...\n")

def timer(time_to_wait):
	print('Waiting '+str(time_to_wait)+' seconds')
	for _ in trange(time_to_wait):
		sleep(1)