"""
Wraps numpy.where but makes it more IDL-like. 

"""

from __future__ import print_function
import numpy as np

def andwhere(data, val1, test1, val2=None, test2=None, return_indices=False):
    """ Performs an 'and' where search, i.e., where(input > 3 and input < 4).
    Using the parameter names, where(data test1 val1 and data test2 val2).
    Can also do a single test, i.e., where(inputs > 3).

    Example
    -------
    To check data > 1.1 and data < 2.5,
    > out = where(data=[1,2,3], val1=1.1, test1='>', val2='2.5', test2='<')
    > print(out)
    [1]  # index
    > print(data[out])
    [2]  # value at index 1

    Parameters
    ----------
    data : list or array

    val1 : int, float, or str
        First value you wish to check 'data' against.
    test1 : str
        Either '<', '>', '<=', '>=', or '=='.
    val2 :
        Second value you wish to check 'data' against.
    test2 : str
        Either '<', '>', '<=', '>=', or '=='.
    return_indices : {True, False}
        If True, returns only the indices of valid 'data' entries. If
        False, returns only the values of 'data' corresponding to those
        entries.

    Returns
    -------

    """
    # Transform the list to numpy array.
    data = np.array(data)

    # Transform the first equality tests.
    if test1 == '<':
        indices1 = np.where(data < val1)[0]
    elif test1 == '>':
        indices1 = np.where(data > val1)[0]     
    elif test1 == '<=':
        indices1 = np.where(data <= val1)[0]    
    elif test1 == '>=':
        indices1 = np.where(data >= val1)[0]   
    elif test1 == '==':
        indices1 = np.where(data >= val1)[0]        
    else:
        print("Invalid equality check, {}".format(test1))

    data_cut1 = data[indices1]
     
    # If only one equality check entered, finish. 
    if val2 == None and test2 == None:
        if return_indices:
            return indices1
        else:
            return data_cut1
    
    # If a second check was entered, continue

    # Transform the second equality tests.
    if test2 == '<':
        indices2 = np.where(data_cut1 < val2)[0]
    elif test2 == '>':
        indices2 = np.where(data_cut1 > val2)[0]    
    elif test2 == '<=':
        indices2 = np.where(data_cut1 <= val2)[0]       
    elif test2 == '>=':
        indices2 = np.where(data_cut1 >= val2)[0]   
    elif test2 == '==':
        indices2 = np.where(data_cut1 >= val2)[0]           
    else:
        print("Invalid equality check, {}".format(test2))

    data_cut2 = data_cut1[indices2]
    
    if return_indices:
        # Returns the first indices because those correspond to 
        # the original input array.
        return indices1[indices2]
    else:
        return data_cut2
