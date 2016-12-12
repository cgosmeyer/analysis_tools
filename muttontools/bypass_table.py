"""
Module for tools to work with Astropy Tables without having to use Astropy 
Table functions.

Author: 

    C.M. Gosmeyer

Date:

    Dec. 2016

"""

import astropy
from astropy.table import Table
from collections import OrderedDict


#-----------------------------------------------------------------------------#

def decompose_table(tab, return_type=list, include_meta=False):
    """
    Breaks an Astropy Table into lists or ordered dictionaries.

    Parameters
    ----------
    tab : Table
        An Astropy Table of some sort.
    return_type : {list, dict}
        Type to return. If 'list', column names and rows will be returned 
        as list of lists. If 'dict', column names will be keys and rows 
        will be values of an OrderedDict.
    include_meta : {True, False}
        Set to True to return the meta data as additional list (if list
        'return_type' selected) or key-value (if dict 'return_type' 
        selected).

    Returns
    -------

    """

    # Check that 'tab' is in fact an astropy table
    try:
        # Retrieve column names.
        colnames = tab.colnames
    except AttributeError:
        print("input for parameter 'tab' must be an astropy table.Table")

    else:
        if return_type == list:
            master_list = []

            for colname in colnames:
                master_list.append(list(tab[colname].data))

            if include_meta:
                 return [colnames, master_list, tab.meta]
            else:
                 return [colnames, master_list]

        elif return_type == dict:
            master_dict = OrderedDict()
            
            for colname in colnames:
                master_dict[colname] = list(tab[colname].data)
            
            if include_meta:
                master_dict['meta'] = tab.meta

            return master_dict


#-----------------------------------------------------------------------------#

def build_table(columns, colnames, *args, **kwargs): 
    """
    A one-line function to build a non-complicated Table.
    Primarily written because I can never remember 'names' parameter.

    Parameters
    ----------
    columns : list of lists
        The lists are the columns corresponding to the column names.
    colnames : list
        The names of the columns.

    Returns
    -------
    tab : Table
        Sparkly new Astropy Table.
    """
    tab = Table(columns, names=colnames, *args, **kwargs)

    return tab


#-----------------------------------------------------------------------------#

def antitable(func):
    """ Decorator to be placed before any function that returns an Astropy
    Table, using :func:`decompose_table`. Will convert that table 
    into an OrderedDict.

    Use
    ---
        @antitable
        function_creating_table(args)

    Parameters
    ----------
    func : function
        The orginal function. Must return an Astropy Table.

    Returns
    -------
    func_wrapper : function
        The wrapped function, now returning an OrderedDict where once it 
        returned an Astropy Table.
    """
    def func_wrapper(*args, **kwargs):
        tab = func(*args, **kwargs)
        ordered_dict = decompose_table(tab, return_type=dict)
        return ordered_dict
    return func_wrapper


