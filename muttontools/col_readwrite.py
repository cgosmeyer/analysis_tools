
"""
Module for reading and writing files, more in style of IDL's 
"readcol" and "writecol" procedures. 

Must be capable of appending to files.

Author:

    C.M. Gosmeyer


"""

from __future__ import print_function
import numpy as np
import os
import re

#-----------------------------------------------------------------------------#

def readcol(filename, headerstart=0, datastart=1, comment='#', 
    deliminator="\s+"):
    """

    future improvements:
    - allow  user to pick to skip a comment line (if comes after datastart)
    - allow user to pick a deliminator 
    - option to return a dictionary??
    """
    print("reading {}".format(filename))
    cols = []
    f = open(filename, 'r')

    i = 0
    for line in f:
        linestrip = re.split("\s+", line)
        while '' in linestrip:
            linestrip.remove('')
        
        # If there is a header, retrieve the column names.
        if i == headerstart and headerstart != datastart:
            # Figure out how many columns and their names.
            if linestrip[0] == '#':
                ncols = len(linestrip)-1
                linestrip.remove('#')
            else:
                ncols = len(linestrip)

            header = linestrip
            cols = [[] for j in range(ncols)]
            # Remove comment if first character.
            if header[0][0] == '#':
                header[0] = header[0][1:]

        # If there is no header, just name the columns
        # by number.
        elif i == datastart and datastart == headerstart:
            ncols = len(linestrip)
            header = list(np.arange(ncols))
            cols = [[] for j in range(ncols)]

        elif i > datastart and linestrip != []:
            if linestrip[0] != comment:
                for item, j in zip(linestrip, range(ncols)):
                    cols[j].append(item)

        i+=1

    f.close()

    #print(header)
    #print(cols)

    return cols,header

#cols,header= readcol('test.txt') 


#-----------------------------------------------------------------------------#

def writecol(filename, data, header=[], deliminator=' ', headerstarter='# ', 
    writer='a+', overwrite=False):
    """
    - have a check for overwriting. give user a warning?
    """

    f = open(filename, writer)
    ncols = len(data)
    nrows = len(data[0])

    if header != []:
        headerline = headerstarter
        for j in range(ncols):
            if j == ncols-1:
                headerline += header[j] + '\n'
            else:
                headerline += header[j] + deliminator 
        f.write(headerline)


    for i in range(nrows):
        print(i)
        line = ''
        for j in range(ncols):
            if j == ncols-1:
                line += data[j][i] + '\n'
            else:
                line += data[j][i] + deliminator
        
        f.write(line)

    f.close()

#writecol('test2.txt', cols, header )


