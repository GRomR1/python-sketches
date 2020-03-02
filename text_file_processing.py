from csv import DictWriter, DictReader
import os


def read_content(path):
    """Read content from text file
    :param path - path to the file
    :return data - read data
    """
    with open(path, "r") as f:
        return f.read()


def save_content(c, path):
    """Save content to text file
    :param c - content (String or ByteArray)
    :param path - path to the file
    :return nothing
    """
    if isinstance(c, str):
        with open(path, "w", encoding='utf-8') as f:
            f.write(c)
    elif isinstance(c, bytes):
        with open(path, "wb") as f:
            f.write(c)


def save_to_csv(data, path):
    """Save list of dictionaries into CSV-text file with UTF-8 and ';' delimiter
    :param data - content (List of Dictionary)
    :param path - path to the file
    :return nothing
    """
    if data:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            columns = list(data[0].keys())
            columns.sort()
            writer = DictWriter(file, fieldnames=columns, delimiter=';')
            writer.writeheader()
            writer.writerows(data)


def open_csv(path):
    """ Get content from CSV file
    :return list of columns data from CSV
    """
    with open(path, newline='', encoding='utf-8') as file:
        reader = DictReader(file, delimiter=';')
        # print(reader.fieldnames)
        return list(reader)


def get_files_from_dir(dir_path):
    """ Get files from directory
    :param dir_path - path or name of directory
    :return list names of files
    """
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]


    
