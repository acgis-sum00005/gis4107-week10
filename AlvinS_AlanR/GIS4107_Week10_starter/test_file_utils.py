import os

import file_utils

def test_get_file_content_existing():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "demo.txt")
    content = file_utils.get_file_content(file_name)
    assert content == "Alan and Alvin"

def test_get_file_content_nonexistent():
    file_name = "nonexistent.txt"
    result = file_utils.get_file_content(file_name)
    assert result == "nonexistent.txt does not exist"
