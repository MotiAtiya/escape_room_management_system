from .printer import display_menu
from .validators import parse_from_range
from .user_input import ask

def get_action(menu):
    display_menu(menu)
    menu_parser = parse_from_range(1, len(menu))
    choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
    title = menu[choice][0]
    action = menu[choice][1]
    return title, action

def enter_to_continue():
    input("\n\nPress Enter to continue... ")
