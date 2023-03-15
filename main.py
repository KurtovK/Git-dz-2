def get_file_extension(file_name):
    if "." not in file_name:
        raise ValueError("Невозможно определить расширение файла")
    return file_name.split(".")[-1]
def print_file_extension(file_name):
    try:
        extension = get_file_extension(file_name)
        print(extension)
    except Exception as e:
        print(e)