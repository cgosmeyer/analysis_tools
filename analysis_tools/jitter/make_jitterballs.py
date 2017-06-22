#! /usr/bin/env python 

"""Makes PNGs of JIF files. 

Authors:

    C.M. Gosmeyer, Sep. 2014

Use: 

    >>> python make_jitterballs.py

Notes:
 
    Original git history in detectors/wfc3_contam/make_jitterballs.py
"""

import os
import glob
import shutil
import pylab
from astropy.io import fits



def make_jitterballs(origin='', destination=''):
    """
    """
    
    jif_list = glob.glob(origin + '*jif.fits')
    
    for jif in jif_list:
        
        rootname = (jif.split('/')[len(jif.split('/'))-1]).split('.fits')[0]
        print rootname
        
        jif_open = fits.open(jif)
        jif_data = jif_open[1].data
        
        pylab.ioff()
        fig = pylab.figure()
        pylab.gray()
        pylab.imshow(jif_data)
        pylab.savefig(destination + rootname + '.png')
        jif_open.close()
        pylab.ion()



if __name__=='__main__':
    origin = ''
    dest = ''
    make_jitterballs(origin=origin, destination=dest)