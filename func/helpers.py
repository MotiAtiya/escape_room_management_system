import os


def clear_screen():
    # Clear the terminal screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')


def get_next_id(array):
    latest_id = max(array, key=lambda a: a['id'])
    return latest_id['id'] + 1

