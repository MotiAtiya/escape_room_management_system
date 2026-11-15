from .printer import display_option_title, display_function_title, display_bookings
from .menu import get_action, enter_to_continue

def new_booking(rooms, bookings):
    pass


def search_booking(bookings):
    pass


def customer_bookings(bookings):
    pass


def bookings_in_date(bookings):
    pass


def change_booking(rooms, bookings):
    pass


def cancel_booking(bookings):
    pass


def bookings_management(rooms, bookings):
    menu = {
        1: ("Create New Booking", lambda: new_booking(rooms, bookings)),
        2: ("Display All Bookings", lambda: display_bookings(bookings)),
        3: ("Search Booking", lambda: search_booking(bookings)),
        4: ("Display Customer Bookings", lambda: customer_bookings(bookings)),
        5: ("Display Bookings in Date", lambda: bookings_in_date(bookings)),
        6: ("Change Booking Details", lambda: change_booking(rooms, bookings)),
        7: ("Cancel Booking", lambda: cancel_booking(bookings)),
        8: ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Products Management")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action()
        except ValueError as e:
            print("Error:", e)
        finally:
            enter_to_continue()
