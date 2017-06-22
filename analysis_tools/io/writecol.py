"""
Module for writing files, more in style of IDL's "writecol" procedure. 

Author:

    C.M. Gosmeyer


"""

from __future__ import print_function
from __future__ import with_statement
import numpy as np
import os
import re
import sys

#-----------------------------------------------------------------------------#

def writecol(filename, data, header=[], deliminator=' ', headerstarter='# ', 
    writer='a+', overwrite=False):
    """ Write the a list of lists into a text file, where each sublist is 
    a column. 

    Parameters
    ----------
    filename : str
        Name of the file to write to.
    data : list of lists
        Can contain any type. The lists will become the columns and must 
        all be the same length.
    header : list
        Optional. The names of the columns.
    deliminator : str
        Optional. How to divide the columns. A single space by default.
    headerstarter : str
        Optional. String with which to start a header. '#' by default.
    writer : str
        Optional. The file writing preference. 'a+' by default.
    overwrite : {True, False}
        Optional. Whether to overwrite (if writer = 'w') or append (if
        writer = 'a') if the file already exists. False by default.
        Meant as a dummy-proof in case you didn't enter the 'writer' you
        intended.

    """

    # Check for overwriting
    if os.path.isfile(filename) and not overwrite:
        print("File '{}' already exists and overwrite is set to False. Halting..."\
            .format(filename))
        return

    elif os.path.isfile(filename) and overwrite:
        print("File '{}' already exists but overwriting/appending with '{}'..."\
            .format(filename, writer))

    else:
        print("File '{}' is being created...".format(filename))

    # Record number of columns.
    ncols = len(data)

    # Check that all columns are same length.
    if not all(len(col) == len(data[0]) for col in data):
        print("Error: columns not all same length.") 
        return 
    else:
        # Record number of rows.
        nrows = len(data[0])

    # Check that a header, if given, matches number of columns.
    if header != [] and len(header) != ncols:
        print("Error: length of header, {}, does not match number of columns, {}."\
            .format(len(header), ncols)) 
        return

    with open(filename, writer) as f:

        # Write a header if one given.
        if header != []:
            headerline = headerstarter
            for j in range(ncols):
                if j == ncols-1:
                    headerline += header[j] + '\n'
                else:
                    headerline += header[j] + deliminator 
            f.write(headerline)

        # Write each sublist as a column.
        for i in range(nrows):
            line = ''
            for j in range(ncols):
                if j == ncols-1:
                    line += str(data[j][i]) + '\n'
                else:
                    line += str(data[j][i]) + deliminator
            
            f.write(line)


