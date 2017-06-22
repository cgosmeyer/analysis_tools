"""
Converts yyyy-mm-dd to MJD by wrapping Astropy.Time.

Author:

    C.M. Gosmeyer

Date:

    13 Dec. 2016

"""

from astropy.time import Time
import numpy as np

def tomjd(dates, format='iso'):  
    """ Converts yyyy-mm-dd to MJD.

    Parameters
    ----------
    dates : list or array of strings.
        Items in the format 'yyyy-mm-dd'.
    format : str
        The format of the input dates. The default corresponds to 
        yyyy-mm-dd.

        See http://docs.astropy.org/en/stable/time/
        if you can find it.

    Returns
    -------
    mjds : array
        The converted MJD dates.
    """
    # check that numpy array
    dates = np.array(dates)

    mjds = Time(dates, format='iso').mjd 

    return mjds

