import os


def create_cache_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        clear_cache_dir(path)


def clear_cache_dir(path):
    if os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
