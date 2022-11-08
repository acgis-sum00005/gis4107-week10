def get_file_content(file_name):
    try:
        with open(file_name) as file:
            return file.readline()
    except FileNotFoundError:
        return file_name + " does not exist"

def write_to_file(file_name, content):
    """Write something to a file.

    Args:
        file_name (str): The name of the file.
        content (str): What to write to the file.
    """
    with open(file_name, 'w') as outfile:
        outfile.write(content)

def get_file_second_line(file_name):
    with open(file_name) as file:
        return file.readlines()[1]
