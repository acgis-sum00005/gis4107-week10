# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        test_water_stn_converter.py
#
# Purpose:     Tests for functions in water_stn_converter.py
#
# Author:      David Viljoen
#
# Created:     09/11/2021
#-------------------------------------------------------------------------------

import json
import water_stn_converter as wsc


def test_load_json_file_to_dict():
    expected = ''
    wsc.in_json_filename = ''
    wsc.load_json_file_to_dict()
    actual = ''
    assert actual == expected


def test_get_values_from_feature():
    """Docstring"""
    expected = ""
    actual = ""

