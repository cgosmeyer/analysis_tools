
"""
Nose tests for file column-based reader, `analysis_tools.io.readcol`.

Use:

    >>> nosetests

Can be made part of git pre-commit hook, living in .git/hooks/pre-commit-nosetests

References:

http://offbytwo.com/2008/05/22/running-nosetests-as-a-git-pre-commit-hook.html
"""

from __future__ import print_function
from analysis_tools.io.readcol import readcol
from analysis_tools.io.writecol import writecol
from nose.tools import *
from IPython.utils.capture import capture_output

import os

abs_path = os.path.split(os.path.abspath(__file__))[0]


def test_reads_nominal_file():
    assert readcol(filename=os.path.join(abs_path, 'test_files/nominal.txt')) == (['x', 'y'], [['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']])

def test_skips_custom_comment_lines():
    assert readcol(filename=os.path.join(abs_path, 'test_files/comments_custom.txt'), comment='%') == ([], []) 
    assert readcol(filename=os.path.join(abs_path, 'test_files/comments_custom2.txt'), comment='%') == (['x', 'y'], [['1', '2', '3'], ['.1', '.2', '.3']])

def test_exits_gracefully_if_no_file():
    assert readcol(filename=os.path.join(abs_path, 'test_files/noexistence.txt')) == ([], [])

def test_finds_header_and_data_if_not_default():
    assert readcol(filename=os.path.join(abs_path,'test_files/nondefault_start.txt'), headerstart=4, datastart=6) == (['x', 'y'], [['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']])

def test_reads_empty_file_gracefully():
    assert readcol(filename=os.path.join(abs_path, 'test_files/empty.txt')) == ([], [])

def test_can_mix_space_and_tab():
    assert readcol(filename=os.path.join(abs_path, 'test_files/mixed_space_tab.txt')) == (['x', 'y'], [['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']])

def test_can_read_custom_deliminator():
   assert readcol(filename=os.path.join(abs_path, 'test_files/custom_deliminator.txt'), deliminator="|") == (['x', 'y'], [['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']])

def test_can_read_single_column_file():
    assert readcol(filename=os.path.join(abs_path, 'test_files/single_col.txt')) == (['x'], [['1', '2', '3', '4']])    

def test_can_read_no_header():
    assert readcol(filename=os.path.join(abs_path,'test_files/noheader.txt'), headerstart=0, datastart=0) == (['0', '1'], [['1', '2', '3', '4'], ['.1', '.2', '.3', '.4']])
