
"""
Nose tests for file reader and writer.

Use:

    >>> 

Test directory includes the test files:

	*
	*
"""

from muttontools.col_readwrite import readcol, writecol
from nose.tools import *

# Tests for readcol

def test_nominal_file():
	assert readcol(filename='nominal.txt') == ([['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']], ['x', 'y'])

def test_skips_custom_comment_lines():
	assert readcol(filename='comments_custom.txt', comment='%') == ([], [])	
	assert readcol(filename='comments_custom2.txt', comment='%') == ([['1', '2', '3'], ['.1', '.2', '.3']], ['x', 'y'])

def test_exits_gracefully_if_no_file():
	assert readcol(filename='noexistence.txt') == ([], [])

def test_finds_header_and_data_if_not_default():
    assert readcol(filename='nondefault_start.txt', headerstart=4, datastart=6) == ([['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']], ['x', 'y'])

def test_reads_empty_file_gracefully():
    assert readcol(filename='empty.txt') == ([], [])

def test_can_mix_space_and_tab():
    assert readcol(filename='mixed_space_tab.txt') == ([['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']], ['x', 'y'])

def test_can_read_custom_deliminator():
   assert readcol(filename='custom_deliminator.txt', deliminator="|") == ([['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']], ['x', 'y'])

# Tests for writecol
#def test_exits_gracefully_if_cols_headerlen_mismatched():

#def test_doesnot_overwrite_file_if_False():

#def test_does_overwrite_file_if_True():

#def cleanup():
#	""" 
#    Removes all generated test files.
#	"""


#def test_appends_to_file():
