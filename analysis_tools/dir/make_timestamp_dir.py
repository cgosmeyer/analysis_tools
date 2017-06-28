
""" Module for creating time-stamped directory. YYYY.MM.DD

Author:

    C.M. Gosmeyer, Jan. 2016
    
"""

import os
import time


def make_timestamp_dir(dest):
    """Creates time-stamped directory. YYYY.MM.DD

    If already exists, creates directory with an underscore integer, 
    1-50.

    Parameters:
        dest : string
            Path to where the time-stamp directory should be created.

    Returns:
        path_to_time_dir : string
            Path to and including the time-stamped directory.

    Outputs:
        Directory at 'dest' with a time-stamped name.
    """
    time_tuple = time.localtime()
    year = str(time_tuple[0])
    month = str(time_tuple[1])
    day = str(time_tuple[2])

    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day        
        
    time_dir = year + '.' + month + '.' + day 
    path_to_time_dir = os.path.join(dest, time_dir)
    
    # If one does not exist for today, create the time-stamp dir.
    if not os.path.isdir(path_to_time_dir + '/'):
        os.mkdir(path_to_time_dir + '/')
        return path_to_time_dir + '/'
    
    # If one already exists for today, create it with underscore index 1-50.
    else:
        for num in range(1,50):
            path_to_time_dir_num = path_to_time_dir + '_' + str(num) + '/'
            if not os.path.isdir(path_to_time_dir_num):
                os.mkdir(path_to_time_dir_num)
                return path_to_time_dir_num