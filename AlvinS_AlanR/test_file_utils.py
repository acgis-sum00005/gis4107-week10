import os

import file_utils

script_folder = os.path.dirname(os.path.abspath(__file__))

def test_get_file_content_existing():
    file_name = os.path.join(script_folder, "data", "demo.txt")
    content = file_utils.get_file_content(file_name)
    assert content == "Alan and Alvin"

def test_get_file_content_nonexistent():
    file_name = "nonexistent.txt"
    result = file_utils.get_file_content(file_name)
    assert result == "nonexistent.txt does not exist"

def test_write_to_file():
    file_name = os.path.join(script_folder, "data", "TestFile.txt")
    content = "Here is some text"
    file_utils.write_to_file(file_name, content)
    assert file_utils.get_file_content(file_name) == content
