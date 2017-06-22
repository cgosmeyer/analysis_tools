#! /usr/bin/env python

import glob
from get_keyval import get_keyval



if __name__ == '__main__':
    filters = glob.glob('F*')
    for filter in filters:
        files = glob.glob(filter + '/i*flt.fits')
        if files != []:
            expt = get_keyval(files[0], 'pa_v3')
            print filter, files[0], expt
