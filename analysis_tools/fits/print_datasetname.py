#! /usr/bin/env python

"""Prints to screen list of dataset names from the FLTs in a directory.

Useful if you want to re-download the FLTs from MAST.

Author:

    C.M. Gosmeyer, Jan. 2014

Use:

    cd to directory containing the FLT files. Then,
    
    >>> python get_datasetname.py
    
Outputs:
   
   Prints to screen list of dataset names.  

Notes:

    Original git history in detectors/wfc3_contam/get_datasetname.py  
"""

import argparse
import glob
import os


def print_datasetname(file_type='flt'):
    """Prints to screen list of dataset names from the FLTs in a 
    directory.

    Useful if you want to re-download the FLTs from MAST.

    Parameters:
        file_type : string
            The type of FITS file. e.g., raw or flt. By default flt.

    Returns:
        nothing

    Outputs:
        Prints to screen list of dataset names.  
    """

    file_list = glob.glob('*' + file_type + '.fits')
    dataset_name_list = []
    for file in file_list:
        file_split = file.split('_' + file_type + '.fits')
        dataset_name_list.append(file_split[0])

    for dataset in dataset_name_list:
        print dataset


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

    type_help = 'The type of FITS file. e.g., raw or flt. By default flt.'
        
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', dest = 'type',
                        action = 'store', type = str, required = True,
                        help = type_help, default='flt')
    args = parser.parse_args()
     
    return args


if __name__ == '__main__':

    args = parse_args()
    file_type = args.type

    file_type = file_type.lower()

    if file_type not in ['flt', 'ima', 'jit', 'jif', 'raw', 'spt']:
        print "Incorrect FITS file type: ", file_type
    else:
        print_datasetname(file_type)
