def get_file_content(file_name):
    try:
        with open(file_name) as file:
            return file.readline()
    except FileNotFoundError:
        return file_name + " does not exist"