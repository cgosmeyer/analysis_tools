#! /usr/bin/env python

"""Matches up JIF files in directory to FLT files in separate 
(or same) directory.


Authors:

    C.M. Gosmeyer, Sep. 2014

Use: 

    >>> python match_jifs_to_flts.py

Notes:

    Original git history in detectors/wfc3_contam/match_jifs_to_flts.py
"""

import glob
from wfc3_contam_tools import get_filter_name


def match_jifs_to_flts(origin_flt='', origin_jif='', dest=''):
    """Matches up JIF files in directory to FLT files in separate 
    (or same) directory.
    
    Parameters:
        origin_flt : string
            Location of FLT files.
        origin_jif : string
            Location of JIF files.
        dest : string
            Where to generate output files.
    
    Returns:
        nothing
    
    Ouputs:
        prints to screen
    """
    
    flt_files = glob.glob(origin_flt + '*flt.fits')    
    jif_files = glob.glob(origin_jif + '*jif.fits')
    
    print "Number FLTs: " + str(len(flt_files))    
    print "Number JIFs: " + str(len(jif_files))
    
    print "FLT files: "
    print flt_files
    print "JIF files: "
    print jif_files
    
    flt_rootnames = {}
    jif_rootnames = []
    
    for flt in flt_files:
        rootname = ((flt.split('/')[len(flt.split('/'))-1]).split('_flt.fits')[0])[0:8]
        filter = get_filter_name('', flt)
        flt_rootnames[rootname] = filter

    for jif in jif_files:
        rootname = ((jif.split('/')[len(flt.split('/'))-1]).split('_jif.fits')[0])[0:8]
        jif_rootnames.append(rootname)

    print "FLT rootnames: "
    print flt_rootnames
    print "JIF rootnames: "
    print jif_rootnames

    flt_matched = {}
    flt_unmatched = {}
    
    for flt in flt_rootnames.keys():
        if flt in jif_rootnames:
            flt_matched[flt] = flt_rootnames[flt]
        else:
            flt_unmatched[flt] = flt_rootnames[flt]
    
    # Sort the unmatched FLTs by filter.
    unmatched_filter_set = set(flt_unmatched.values())
    
    print "The unmatched FLTs (ie, JIFs that are missing): "
    for filter in unmatched_filter_set:
        for filename in flt_unmatched.keys():
            if flt_unmatched[filename] == filter:
                print filter, filename


    # Sort the matched FLTs by filter.
    matched_filter_set = set(flt_matched.values())
    
    print "The matched FLTs: "
    for filter in matched_filter_set:
        for filename in flt_matched.keys():
            if flt_matched[filename] == filter:
                print filter, filename



if __name__=='__main__':
    origin_flt = ''
    origin_jif = ''
    dest = ''
    match_jifs_to_flts(origin_flt=origin_flt, \
                       origin_jif=origin_jif, \
                       dest=dest)