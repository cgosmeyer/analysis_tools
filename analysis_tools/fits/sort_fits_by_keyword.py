#! /usr/bin/env python

"""Moves all files in directory into subdirectories sorted by given
header keyword. 

Authors:

    C.M. Gosmeyer, Sep. 2014

Use: 

    >>> python sort_fits_by_keyword.py '<keyword>'

Notes:

    Original git history in detectors/wfc3_contam/sort_fits_by_keyword.py
"""
from __future__ import print_function

import argparse 
import glob
import os
import shutil
import sys
from astropy.io import fits

def sort_fits_by_keyword(keyword=''):
	"""Moves files into directory named for their filter.
	
	Parameters:
        keyword : string
            The header keyword you want to sort files by.
	        
	Returns:
        nothing
	    
	Outputs:
        nothing
	"""
	keyword = str(keyword)
	keyword = keyword.upper()
	
	keyvalue_list = []
	filename_list = glob.glob('*fits')
	
	for filename in filename_list:
		header = fits.getheader(filename)
		keyvalue = header[keyword]
		
		keyvalue = str(keyvalue)
		
		if keyvalue not in keyvalue_list:
		    keyvalue_list.append(keyvalue)
		
		existing_keyvalue_dir = glob.glob(keyvalue)
		if existing_keyvalue_dir == []:
			print(' ... ')
			print("Making new directory, {}".format(keyvalue))
			os.mkdir(keyvalue)
		
		if filename not in glob.glob(keyvalue+'/*'):	
		    print("Moving {} to directory, {}".format(filename, keyvalue))
		    shutil.move(filename, keyvalue + '/' + filename)
		else:
		    print('ERROR. File {} already in directory {}'.format(filename, keyvalue))


#-------------------------------------------------------------------------------#    

def parse_args():
    """Parses command line arguments.
    
    Parameters:
        nothing.
        
    Returns:
        args : object
            Containing the image and destination arguments.
            
    Outputs:
        nothing.
    """

    kw_help = 'Header keyword that you want to sort FITS files by into directories.'
        
    parser = argparse.ArgumentParser()
    parser.add_argument('--kw', dest = 'kw',
                        action = 'store', type = str, required = True,
                        help = kw_help)              
    args = parser.parse_args()
    
    return args

     
#-------------------------------------------------------------------------------#   

if __name__ == '__main__':

    args = parse_args()

    keyword = args.kw
    sort_fits_by_keyword(keyword)