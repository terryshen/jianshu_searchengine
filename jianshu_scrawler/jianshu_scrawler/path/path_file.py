import os


def get_root_path():
    # dir_path = os.path.join(os.path.dirname(os.getcwd()), 'users')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    return dir_path


def get_files_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    dir_path = os.path.join(dir_path, 'output')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(dir_path, 'files')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def get_files_path_userid(user_id):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    dir_path = os.path.join(dir_path, 'output')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(dir_path, 'files', user_id)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def get_logs_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    dir_path = os.path.join(dir_path, 'output')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(dir_path, 'logs')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def get_user_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    dir_path = os.path.join(dir_path, 'output')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dir_path = os.path.join(dir_path, 'user')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def get_user_path_file(file_name):
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.dirname(file_path)
    file_path = os.path.join(file_path, 'output', 'user', file_name)
    return file_path


def get_crawleduser_path_file(file_name):
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.dirname(file_path)
    file_path = os.path.join(file_path, 'output', 'user', file_name)
    return file_path

