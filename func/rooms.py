from .printer import display_option_title, display_function_title, display_rooms
from .menu import get_action, enter_to_continue


def room_details(rooms):
    pass


def add_room(rooms):
    pass


def update_room(rooms):
    pass


def active_or_inactive_room(rooms):
    pass


def rooms_management(rooms):
    menu = {
        "1": ("Display All Rooms", display_rooms),
        "2": ("Display Room Details", room_details),
        "3": ("Add Room", add_room),
        "4": ("Update Room", update_room),
        "5": ("Active or Inactive Room", active_or_inactive_room),
        "6": ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Products Management")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action(rooms)
        except ValueError as e:
            print("Error:", e)
        finally:
            enter_to_continue()
