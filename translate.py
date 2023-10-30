from urllib.parse import quote


def trans(file_name, *args):
    path = '/' + '/'.join([args, file_name])
    encoded_file_name = quote(path)
    print(encoded_file_name)
    return encoded_file_name
