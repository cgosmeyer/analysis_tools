#! /usr/bin/env python

"""Fetches all FITS from a directory that observed the given keyvalue to
a destination directory.
Can specify what tyep of FITS file to fetch (i.e., raw or flt).

Authors:

    C.M. Gosmeyer, Aug 2015

Use: 

    >>> python fetch_fits_by_keyvalue.py '<keyvalue>' '<keyword>' '<fits type>' '<orig_dir/>' '<dest_dir/>'
    
Example: 

    >>> python fetch_fits_by_keyvalue.py 'F547M' 'FILTER' 'flt' '/grp/hst/wfc3/cgosmeyer/tests/' '.'

Notes:

    Original git history in detectors/wfc3_contam/fetch_fits_by_keyvalue.py

"""

import argparse
import glob
import os
import shutil
import sys
from astropy.io import fits


def fetch_fits_by_keyvalue(keyvalue='', keyword='', fits_type='', orig_dir='', dest_dir=''):
    """
    
    Parameters:
        keyvalue : string
            Name of value of the keyword we want to match. 
            i.e., 'P330E' if keyword='TARGNAME'
        keyword : string
            Name of the header keyword.
        fits_type : string
            The type of FITS file. For example, 'raw' or 'flt'.
            If do '', will fetch all types.
        orig_dir : string
            The original location of the files to be copied.
        dest_dir : string
            The destination for the files to be copied to.
            
    Returns:
        nothing
        
    Outputs:
        nothing
    """
    if dest_dir == '':
        dest_dir = os.getcwd()

    keyvalue = str(keyvalue)
    keyvalue = keyvalue.lower()
    
    keyword = str(keyword)
    keyword = keyword.upper()
    
    fits_type = str(fits_type)
    fits_type = fits_type.lower()
    
    match_list = []
    filename_list = glob.glob(orig_dir+'*'+fits_type+'.fits')
    print filename_list
    
    print "Searching in {0} for *{1}.fits".format(orig_dir, fits_type)
    
    for filename in filename_list:
        header = fits.getheader(filename)
        actual_keyvalue = header[keyword]
        
        actual_keyvalue = str(actual_keyvalue)
        actual_keyvalue = actual_keyvalue.lower()
        
        if keyvalue == actual_keyvalue:
            match_list.append(filename)
            
    for filename in match_list:
        if filename not in glob.glob(dest_dir + '*'):
            print "Copying {0} to {1}".format(filename, dest_dir)
            shutil.copy(filename, dest_dir)


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

    kv_help = 'Key value that you want to match to.'
    kw_help = 'Header keyword that is storing the key value.'
    type_help = 'Type of FITS file, e.g., raw or flt. By default, selects all types.'
    orig_help = 'The origin of the files to be copied. CWD by default.'
    dest_help = 'The destination where the files will be copied to. CWD by default.'
        
    parser = argparse.ArgumentParser()
    parser.add_argument('--kv', dest = 'keyvalue',
                        action = 'store', type = str, required = True,
                        help = kv_help)
    parser.add_argument('--kw', dest = 'keyword',
                        action = 'store', type = str, required = True,
                        help = kw_help)              
    parser.add_argument('--type', dest = 'type',
                        action = 'store', type = str, required = False,
                        help = type_help, default = 'flt')
    parser.add_argument('--orig', dest = 'orig',
                        action = 'store', type = str, required = False,
                        help = orig_help, default = '')
    parser.add_argument('--dest', dest = 'dest',
                        action = 'store', type = str, required = False,
                        help = dest_help, default = '')
    args = parser.parse_args()
     
    return args


#-------------------------------------------------------------------------------#    

if __name__ == '__main__':

    args = parse_args()

    keyvalue = args.keyvalue
    keyword = args.keyword
    fits_type = args.type
    orig_dir = args.orig
    dest_dir = args.dest
    
    fetch_fits_by_keyvalue(keyvalue, keyword, fits_type, orig_dir, dest_dir)