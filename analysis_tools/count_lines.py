#! /usr/bin/env python

""" Script to count all lines of actual code in a Python file.
Skips all comment and blank lines.

"""
from __future__ import print_function
import argparse
import glob
import os

#-----------------------------------------------------------------------------#

def count_code_lines(dir, ext):
    """

    Future:
    - should add option to print out number of comment lines
    - option of comment line starter

    References:
    http://stackoverflow.com/questions/9076672/how-to-count-lines-of-code-in-python-excluding-comments-and-docstrings
    """

    scripts = glob.glob(os.path.join(dir, '*.{}'.format(ext)))

    # should remove self from list.
    if os.path.join(dir, 'count_code_lines.py') in scripts:
        scripts.remove(os.path.join(dir, 'count_code_lines.py'))
        print("Removed {}".format(os.path.join(dir, 'count_code_lines.py')))
    
    all_code_line_count = 0

    for script in scripts:
        code_line_count = 0
        # Open the script.
        with open(script) as f:
            docstring = False
            lines = f.readlines()
            for line in lines:
                # Check if in a comment
                

                line = line.strip()

                if line == "" \
                   or line.startswith("#") \
                   or line.startswith(";") \
                   or line == '\n' \
                   or docstring and not (line.startswith('"""') or line.startswith("'''"))\
                   or (line.startswith("'''") and line.endswith("'''") and len(line) >3)  \
                   or (line.startswith('"""') and line.endswith('"""') and len(line) >3) :
                    continue

                # this is either a starting or ending docstring
                elif line.startswith('"""') or line.startswith("'''"):
                    docstring = not docstring
                    continue

                else:
                    #print(line)
                    code_line_count += 1


        print("Code lines in script {} are {}".format(script, code_line_count) )
        all_code_line_count += code_line_count

    print("Code lines in all scripts in directory {} are {}".format(dir, all_code_line_count) )

#-----------------------------------------------------------------------------#

def parse_args():
    """Parses command line arguments.
    
    Parameters
    
        nothing
        
    Returns:
        args : object
            Containing the image and destination arguments.
            
    Outputs:
        nothing
    """
    dir_help = "Path to directory containing Python scripts. CWD by default."
    ext_help = "Extension of the file. py, pro, etc."

    parser = argparse.ArgumentParser()
    parser.add_argument('--d', dest = 'dir',
                        action = 'store', type = str, required = False,
                        help = dir_help, default='.')
    parser.add_argument('--e', dest = 'ext',
                        action = 'store', type = str, required = False,
                        help = ext_help, default='py')


    args = parser.parse_args()

    return args

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

if __name__=='__main__':

    args = parse_args()
    dir = args.dir
    ext = args.ext

    count_code_lines(dir, ext)
