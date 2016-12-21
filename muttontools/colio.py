
"""
Module for reading and writing files, more in style of IDL's 
"readcol" and "writecol" procedures. 

Must be capable of appending to files.

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

def readcol(filename, headerstart=0, datastart=1, comment=' ', 
    deliminator="\s+"):
    """ Reads the columns of a text file. Returns the columns as a 
    list of list and the header as a list.

    Parameters
    ----------
    filename : str
        Name of the text file.
    headerstart : int 
        The row of the header. By default, row=0.
    datastart : int 
         The row the data begins. By default, row=1
    comment : str
         The character denoting a comment line, to be ignored when reading
         columns. By default nothing. 
    deliminator : str
         The column divider. By default, spaces or tabs. 

    Returns
    -------
    header : list of strings
        List of the column names if they exist in row specified by 
        'headerstart'. If first column name contains a '#' it will 
        be removed. If no column names exist, then returns a list 
        of string numbers, starting at '0'. 
    cols : list of lists
        List of the columns, each their own list. If no columns found,
        returns an empty list. 

    future improvements:
    - option to return a dictionary??

    """

    # Try and Except to exit gracefully and return empty lists
    # if the file does not exist.
    # (but if end up not returning empty lists, could try to 
    # re-write the with loop into the try-with)
    try: 
        # Open using with so that if error occurs the file will
        # be closed properly.
        with open(filename, 'r') as f:
            print("reading {}".format(filename))

            # Initialize counts and lists.
            cols = []
            row_count = 0

            # Make sure that \t, \n, etc will still be split out.
            if deliminator != "\s+":
                deliminator = '[' + deliminator + '\s\+]'

            # not too happy with the with then for structure
            # but better to use with so that file always is closed.
            # how to return custom output if exception occurs? 
            for line in f:

                # Change line into list of entires, split by the 
                # deliminator.
                linestrip = re.split(deliminator, line)

                # Remove all empty strings.
                while '' in linestrip:
                    linestrip.remove('')

                # First test that line is not empty.
                # Second test whether the first line is in fact
                # a custom comment.
                # If the user chooses to have a comment above the header,
                # and that header is denoted by the same comment marker,
                # it is on the user to choose correctly the 'headerstart'.
                if linestrip != [] and linestrip[0][0] != comment:

                    # If there is a header, retrieve the column names.
                    if row_count == headerstart and headerstart != datastart:
                        # Figure out how many columns and their names.
                        if linestrip[0] == '#':
                            ncols = len(linestrip)-1
                            linestrip.remove('#')
                        else:
                            ncols = len(linestrip)
                        print('ncols: {}'.format(ncols))
                        header = linestrip
                        # Initilize empty list for each column.
                        cols = [[] for row in range(ncols)]

                        # Remove comment if first character.
                        if header[0][0] == '#':
                            header[0] = header[0][1:]

                    # If there is no header, just name the columns
                    # by number.
                    elif row_count == datastart and datastart == headerstart:
                        ncols = len(linestrip)
                        header = list(map(str, np.arange(ncols)))
                        # Initilize empty list for each column.
                        cols = [[] for row in range(ncols)]

                    # For all rows not in header, not empty, and not 
                    # a comment, append to column list.
                    # This is an if so that it can execute should
                    # headerstart = datastart = 0.
                    if row_count >= datastart and linestrip != []:
                        for item, row in zip(linestrip, range(ncols)):
                            cols[row].append(item)
                    row_count+=1

        # Check whether the file was empty or no valid columns read.
        if cols == []:
            print("No valid columns found for file {}.".format(filename))
            return [], []
        else:
            return header, cols

    except IOError:
        print("File {} does not exist.".format(filename))
        return [], []



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

    Returns
    -------

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

        if header != []:
            headerline = headerstarter
            for j in range(ncols):
                if j == ncols-1:
                    headerline += header[j] + '\n'
                else:
                    headerline += header[j] + deliminator 
            f.write(headerline)


        for i in range(nrows):
            line = ''
            for j in range(ncols):
                if j == ncols-1:
                    line += data[j][i] + '\n'
                else:
                    line += data[j][i] + deliminator
            
            f.write(line)


