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
import os
import water_stn_converter as wsc

path = os.path.join(os.path.dirname(__file__), 'data/water_stn.json')

def test_load_json_file_to_dict():
    expected = "01AD002"
    dict = wsc.load_json_file_to_dict(path)
    actual = dict['features'][0]['attributes']['Station_Number']
    assert actual == expected


def test_get_values_from_feature():
    dict = wsc.load_json_file_to_dict(path)
    feature = dict['features'][0]['attributes']
    expected = ("01AD002", "Saint John River at Fort Kent", "-68.59583", "47.25806")
    actual = wsc.get_values_from_feature(feature)
    assert actual == expected
