#! /usr/bin/env python

"""Returns the key value of the given header keyword of the given FITS
file. Checks the 0th header unless otherwise specified. 

Author:

    C.M. Gosmeyer, Mar. 2014

Use:

    >>> python get_keyval.py --f 'example.fits' --kw 'filter'
    
"""

import argparse
from astropy.io import fits


def get_keyval(filename='', keyword='', ext=0):
    """

    Parameters:
        filename : string
            Name of file you want filter name of.
            If '', assumes you want to glob over directory
            in 'origin'. 
        keyword : string
            Header keyword whose key value you want.
        ext : integer
            Extension in which to search for keyword.
            
    Returns:
        keyvalue : string
            The key value of the given header keyword. 
        
    Outputs:
        nothing
 
    Notes:
        This assumes all the FITS in the directory are of the same filter.
    """
    if filename != '' or filename[len(filename)-4:] == 'fits':  ## how slice just the last few?
        fits_file = fits.open(filename)
    else:
        print "No filename given!"
        return None
    
    try: 
        keyvalue = fits_file[0].header[keyword]
        fits_file.close()
        return keyvalue
        
    except:
        print "Keyword does not exist in the extension " + str(ext)
        return None 

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

    f_help = 'Name of the FITS file.'
    kw_help = 'Header keyword.'
    e_help = 'Extension in which to search for keyword. 0 default.'
        
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', dest = 'f',
                        action = 'store', type = str, required = True,
                        help = f_help)
    parser.add_argument('--kw', dest = 'kw',
                        action = 'store', type = str, required = True,
                        help = kw_help, default = '')              
    parser.add_argument('--e', dest = 'e',
                        action = 'store', type = str, required = False,
                        help = e_help, default = 0)
    args = parser.parse_args()
     
    return args


#-------------------------------------------------------------------------------#    

if __name__ == '__main__':
    args = parse_args()    

    filename = args.f
    keyword = args.kw
    ext = args.e
    
    keyword = keyword.lower()
    
    keyvalue = get_keyval(filename, keyword, ext)
    
    print keyvalue