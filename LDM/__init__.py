# The information about the LDM program

__name__    = 'LDM'
__version__ = '0.5'
__author__  = 'Dr. Geoffrey Weal, Dr. Chayanit Wechwithayakhlung, Dr. Michael Price, Dr. Daniel Packwood, Dr. Paul Hume, Prof. Justin Hodgkiss'

import sys, importlib

if sys.version_info[0] == 2:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires Python3. You are attempting to execute this program in Python2.'+'\n'
	toString += 'Make sure you are running the LDM program in Python3 and try again'+'\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)
if sys.version_info[1] < 4:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires Python 3.4 or greater.'+'\n'
	toString += 'You are using Python '+str('.'.join(sys.version_info))
	toString += '\n'
	toString += 'Use a version of Python 3 that is greater or equal to Python 3.4.\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)

# ------------------------------------------------------------------------------------------------------------------------
# A check for ASE

numpy_spec = importlib.util.find_spec("numpy")
numpy_found = (numpy_spec is not None)
if not numpy_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires numpy.'+'\n'
	toString += '\n'
	toString += 'Install ase by typing the following into your terminal:\n'
	toString += 'pip3 install --user --upgrade numpy\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

# ------------------------------------------------------------------------------------------------------------------------

scipy_spec = importlib.util.find_spec("scipy")
scipy_found = (scipy_spec is not None)
if not scipy_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires scipy.'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade scipy\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

# ------------------------------------------------------------------------------------------------------------------------

packaging_spec = importlib.util.find_spec("packaging")
packaging_found = (packaging_spec is not None)
if not packaging_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "packaging" program.'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade packaging\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

# ------------------------------------------------------------------------------------------------------------------------

tqdm_spec = importlib.util.find_spec("tqdm")
tqdm_found = (tqdm_spec is not None)
if not tqdm_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "tqdm" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade tqdm\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

bs4_spec = importlib.util.find_spec("bs4")
bs4_found = (bs4_spec is not None)
if not bs4_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "bs4" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade bs4\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

selenium_spec = importlib.util.find_spec("selenium")
selenium_found = (selenium_spec is not None)
if not selenium_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "selenium" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade selenium\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

webdriver_manager_spec = importlib.util.find_spec("webdriver_manager")
webdriver_manager_found = (webdriver_manager_spec is not None)
if not webdriver_manager_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "webdriver_manager" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade webdriver_manager\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

fitz_spec = importlib.util.find_spec("fitz")
fitz_found = (fitz_spec is not None)
if not fitz_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "fitz" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade fitz\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

tqdm_spec = importlib.util.find_spec("xlsxwriter")
tqdm_found = (tqdm_spec is not None)
if not tqdm_found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the LDM Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The LDM program requires the "xlsxwriter" program..'+'\n'
	toString += '\n'
	toString += 'Install scipy by typing the following into your terminal:\n'
	toString += '\n'
	toString += 'pip3 install --user --upgrade xlsxwriter\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'

# ------------------------------------------------------------------------------------------------------------------------

__author_email__ = 'geoffrey.weal@vuw.ac.nz'
__license__ = 'GNU AFFERO GENERAL PUBLIC LICENSE'
__url__ = 'https://github.com/geoffreyweal/LDM'
__doc__ = 'See https://github.com/geoffreyweal/LDM for the documentation on this program'

from LDM.Program.LDM import LDM
__all__ = ['LDM']

# ------------------------------------------------------------------------------------------------------------------------
