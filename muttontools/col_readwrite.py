
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

    future improvements:
    - option to return a dictionary??
    - rewrite as class?
    - how make fewer loops?? 
    """
    # Make sure file exists.
    #try:    
    #    f = open(filename, 'r')
    #except IOError:
    #    print("File {} does not exist.".format(filename))
    #    return [], []

    #print("reading {}".format(filename))
    cols = []
    i = 0
     
    # Make sure that \t, \n, etc are still being split 
    if deliminator != "\s+":
        deliminator = '[' + deliminator + '\s\+]'

    try: 
        with open(filename, 'r') as f:
            # not too happy with the with then for structure
            # but better to use with so that file always is closed.
            # how to return custom output if exception occurs? 
            for line in f:

                print("reading {}".format(filename))

                print(line)
                linestrip = re.split(deliminator, line)
                while '' in linestrip:
                    linestrip.remove('')
                
                print(i, headerstart, datastart)
                print(linestrip)

                # First test that line is not empty.
                if linestrip != []:

                    # Second test whether the first line is in fact
                    # a custom comment.
                    # If the user chooses to have a comment above the header,
                    # and that header is denoted by the same comment marker,
                    # it is on the user to choose correctly the 'headerstart'.

                    if linestrip[0] != comment:

                        # If there is a header, retrieve the column names.
                        if i == headerstart and headerstart != datastart:
                                # need to fix so that '#' is headercomment
                                # Figure out how many columns and their names.
                            if linestrip[0] == '#':
                                ncols = len(linestrip)-1
                                linestrip.remove('#')
                            else:
                                ncols = len(linestrip)
                            print('ncols: {}'.format(ncols))
                            header = linestrip
                            cols = [[] for j in range(ncols)]

                            # Remove comment if first character.
                            if header[0][0] == '#':
                                header[0] = header[0][1:]
                            print("header: {}".format(header))

                        # If there is no header, just name the columns
                        # by number.
                        elif i == datastart and datastart == headerstart:
                            ncols = len(linestrip)
                            header = list(np.arange(ncols))
                            cols = [[] for j in range(ncols)]

                        elif i >= datastart and linestrip != []:
                            for item, j in zip(linestrip, range(ncols)):
                                cols[j].append(item)
                        i+=1

        #f.close()

        # Check whether the file was empty or no valid columns read.
        if cols == []:
            print("No valid columns found for file {}.".format(filename))
            return [], []
        else:
            return cols, header

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

    data :

    header : 

    deliminator : str

    headerstarter : str

    writer : str

    overwrite : {True, False}


    Returns
    -------

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


