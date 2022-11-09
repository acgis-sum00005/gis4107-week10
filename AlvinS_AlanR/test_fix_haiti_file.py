#-------------------------------------------------------------------------------
# Name:        test_fix_haiti_file.py
#
# Purpose:	   Test functions in fix_haiti_file.py
#
# Author:      David Viljoen
#
# Created:     08/11/2021
#-------------------------------------------------------------------------------

import csv
import os
import fix_haiti_file as fh
import file_utils as fu


def test_fix_code_typical_code():
    """Given HT12345-01, expecting HT1245-01"""
    assert fh._fix_code("HT12345-01") ==  "HT1245-01"

script_folder = os.path.dirname(os.path.abspath(__file__))

def test_fix_file():
    """"Haiti_Admin_Names.csv contains ADMIN_CODES in the first column
        Haiti_Admin_Names_fixed.csv contains a fixed version.
		TIP:  expected will be a "fixed" row of data
		      actual will be the row extracted from the fixed file
	"""
    expected = "HT0522-01,Artibonite,Terre Neuve,Doland"
    output_file = os.path.join(script_folder, "data",  "Haiti_Admin_Names_fixed.csv")
    input_file = os.path.join(script_folder, "data",  "Haiti_Admin_Names.csv")
    fh.fix_file(input_file, output_file, 0)
    actual = fu.get_file_second_line(output_file)
    assert expected == actual
